"""
Core PDF conversion logic using Playwright
"""

from playwright.sync_api import sync_playwright
from typing import Optional, Dict, Tuple
from pathlib import Path
from urllib.parse import urlparse
from .utils.template import create_header_footer_templates
import base64

class WebToPDFConverter:
    """Handles webpage to PDF conversion with various options"""

    VALID_PAGE_SIZES = {"A4", "Letter", "Legal", "Tabloid", "Ledger"}
    
    def __init__(
        self,
        logger,
        page_size: str = "A4",
        orientation: str = "portrait",
        margin: Tuple[float, float, float, float] = (0.5, 0.5, 0.5, 0.5),
        header: Optional[str] = None,
        footer: Optional[str] = None,
        delay: int = 0,
        auth_user: Optional[str] = None,
        auth_pass: Optional[str] = None,
        proxy_server: Optional[str] = None,
        **kwargs
    ):
        if page_size not in self.VALID_PAGE_SIZES:
            raise ValueError(f"Invalid page size: {page_size}")
        self.logger = logger
        self.page_size = page_size
        self.orientation = orientation.lower()
        self.margins = {
            "top": f"{margin[0]}in",
            "right": f"{margin[1]}in",
            "bottom": f"{margin[2]}in",
            "left": f"{margin[3]}in"
        }
        self.header_template, self.footer_template = create_header_footer_templates(header, footer)
        self.delay = delay
        self.auth = (auth_user, auth_pass) if auth_user and auth_pass else None
        self.proxy = proxy_server

    def convert(self, url: str, output_path: str):
        """Main conversion method"""
        
        with sync_playwright() as playwright:
            browser = self._launch_browser(playwright)
            page = browser.new_page()  # <-- Khai báo biến page ở đây
            
            try:
                self._configure_page(page, url)
                self._navigate_to_page(page, url)
                self._apply_delay(page)  # <-- Truyền page vào phương thức
                self._generate_pdf(page, output_path)
                
            finally:
                browser.close()

    def _launch_browser(self, playwright):
        """Configure and launch browser instance"""
        launch_options = {
            "headless": True,
            "proxy": {"server": self.proxy} if self.proxy else None
        }
        return playwright.chromium.launch(**launch_options)

    def _configure_page(self, page, url):
        """Set up page authentication and headers"""
        if self.auth:
            # Sửa thành Basic Auth đúng chuẩn
            auth_str = f"{self.auth[0]}:{self.auth[1]}"
            encoded_auth = base64.b64encode(auth_str.encode()).decode()
            page.set_extra_http_headers({
                "Authorization": f"Basic {encoded_auth}"
            })

        page.set_viewport_size({"width": 1920, "height": 1080})

    def _navigate_to_page(self, page, url):
        """Handle page navigation with error checking"""
        try:
            nav_result = page.goto(
                url,
                wait_until="networkidle",
                timeout=45000  # Tăng timeout lên 45s
            )
            if not nav_result or nav_result.status >= 400:
                raise RuntimeError(f"Failed to load page: HTTP {nav_result.status if nav_result else 'unknown'}")
                
        except Exception as e:
            self.logger.error(f"Navigation error: {str(e)}")
            # Retry logic
            self.logger.info("Retrying navigation...")
            nav_result = page.goto(url, timeout=60000)
            if not nav_result.ok:
                raise

    def _apply_delay(self, page):  # <-- Thêm page làm tham số
        """Handle delay before PDF generation"""
        if self.delay > 0:
            self.logger.debug(f"Applying delay: {self.delay}ms")
            page.wait_for_timeout(self.delay)

    def _generate_pdf(self, page, output_path):
        """Generate PDF with configured options"""
        pdf_options = {
            "path": output_path,
            "format": self.page_size,
            "landscape": self.orientation == "landscape",
            "margin": self.margins,
            "display_header_footer": bool(self.header_template or self.footer_template),
            "print_background": True,
            "prefer_css_page_size": True
        }
        
        if self.header_template:
            pdf_options["header_template"] = self.header_template
        if self.footer_template:
            pdf_options["footer_template"] = self.footer_template

        try:
            page.pdf(**pdf_options)
        except Exception as e:
            self.logger.error(f"PDF generation failed: {str(e)}")
            raise