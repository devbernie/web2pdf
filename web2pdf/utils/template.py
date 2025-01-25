"""
Header/footer template generation
"""

from html import escape
from typing import Optional, Tuple  # Thêm dòng này

def create_header_footer_templates(
    header_text: Optional[str] = None,
    footer_text: Optional[str] = None
) -> Tuple[str, str]:
    """Generate HTML templates for headers/footers"""
    
    header_template = ""
    footer_template = ""

    if header_text:
        header_template = f"""
        <div style="font-size: 8px; margin: 0 auto; text-align: center;">
            {escape(header_text)}
        </div>
        """
        
    if footer_text:
        footer_template = f"""
        <div style="font-size: 8px; margin: 0 auto; text-align: center;">
            Page <span class="pageNumber"></span> of <span class="totalPages"></span>
            <br>{escape(footer_text)}
        </div>
        """
        
    return header_template.strip(), footer_template.strip()