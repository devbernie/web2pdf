"""
Input validation utilities
"""

from urllib.parse import urlparse
import os
import click

def validate_url(url: str):
    """Validate input URL format"""
    
    parsed = urlparse(url)
    if not parsed.scheme or not parsed.netloc:
        raise click.BadParameter("Invalid URL format. Must include http:// or https://")
        
    if parsed.scheme not in ("http", "https"):
        raise click.BadParameter("Only HTTP/HTTPS URLs are supported")

def validate_output_path(path: str):
    """Validate output path permissions"""
    
    output_dir = os.path.dirname(os.path.abspath(path))
    if not os.path.exists(output_dir):
        raise click.FileError(f"Directory does not exist: {output_dir}")
        
    if not os.access(output_dir, os.W_OK):
        raise click.FileError(f"Write permission denied for directory: {output_dir}")