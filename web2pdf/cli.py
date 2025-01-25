"""
CLI entry point for Web2PDF converter
"""

import os
import click
from pathlib import Path
from .converter import WebToPDFConverter
from .utils.logger import setup_logger
from .utils.error_handling import handle_conversion_error
from .utils.validators import validate_url, validate_output_path

@click.command()
@click.argument("url", type=str, required=True)
@click.argument("output_path", type=click.Path(), required=True)
@click.option("--page-size", default="A4", help="Paper format (default: A4)")
@click.option("--orientation", type=click.Choice(["portrait", "landscape"]), default="portrait")
@click.option("--margin", nargs=4, type=float, default=(0.5, 0.5, 0.5, 0.5), 
             help="Margins in inches (top right bottom left)")
@click.option("--header", type=str, help="Header text template")
@click.option("--footer", type=str, help="Footer text template")
@click.option("--delay", type=int, default=0, 
             help="Milliseconds delay before PDF generation")
@click.option("--auth-user", type=str, help="Username for HTTP authentication")
@click.option("--auth-pass", type=str, help="Password for HTTP authentication")
@click.option("--proxy-server", type=str, help="Proxy server URL")
@click.option("--verbose", is_flag=True, help="Enable verbose logging")
def main(url, output_path, **options):
    """Convert webpage to PDF"""
    
    logger = setup_logger(options.get('verbose', False))
    
    try:
        # Input validation
        validate_url(url)
        validate_output_path(output_path)
        
        # Initialize converter
        converter = WebToPDFConverter(logger=logger, **options)
        
        # Execute conversion
        converter.convert(url, output_path)
        
        logger.info(f"Successfully generated PDF: {output_path}")
        
    except Exception as e:
        handle_conversion_error(e, logger)
        raise click.Abort()

if __name__ == "__main__":
    main()