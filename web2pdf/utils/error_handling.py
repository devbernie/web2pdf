"""
Custom error handling utilities
"""

from typing import Optional
import logging

def handle_conversion_error(error: Exception, logger: Optional[logging.Logger] = None):
    """Handle and log conversion errors"""
    
    error_mapping = {
        "TimeoutError": "Page loading timeout occurred",
        "RuntimeError": "Browser operation failed",
        "NavigationError": "Page navigation failed",
        "FileNotFoundError": "Output directory not found"
    }
    
    error_name = type(error).__name__
    user_message = error_mapping.get(error_name, "An unexpected error occurred")
    full_message = f"{user_message}: {str(error)}"
    
    if logger:
        logger.error(full_message, exc_info=True)
    else:
        print(f"ERROR: {full_message}")