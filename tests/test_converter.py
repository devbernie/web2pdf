"""
PDF conversion logic tests
"""

from typing import Optional
import pytest
from pathlib import Path
from web2pdf.converter import WebToPDFConverter
from web2pdf.utils.logger import setup_logger

@pytest.fixture
def converter():
    return WebToPDFConverter(logger=setup_logger(False))

def test_pdf_generation(converter, tmp_path):
    output_file = tmp_path / "test.pdf"
    converter.convert("https://example.com", str(output_file))  # Đổi URL test
    assert output_file.exists()
    
    # Kiểm tra cả nội dung PDF cơ bản
    pdf_size = output_file.stat().st_size
    assert pdf_size > 1024, f"PDF size too small: {pdf_size} bytes"
    
    # Kiểm tra signature file PDF
    with open(output_file, 'rb') as f:
        header = f.read(4)
        assert header == b'%PDF', "Invalid PDF file format"

def test_invalid_page_size():
    logger = setup_logger(False)
    with pytest.raises(ValueError):
        WebToPDFConverter(
            logger=logger,  # Thêm logger
            page_size="InvalidSize"
        )

def test_proxy_configuration():
    logger = setup_logger(False)
    converter = WebToPDFConverter(
        logger=logger,  # Thêm logger
        proxy_server="http://proxy.example.com"
    )
    assert converter.proxy == "http://proxy.example.com"