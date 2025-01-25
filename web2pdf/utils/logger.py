"""
Logging configuration
"""

import logging
import sys

def setup_logger(verbose: bool = False) -> logging.Logger:
    """Configure application logger"""
    
    logger = logging.getLogger("web2pdf")
    logger.propagate = False
    
    handler = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    
    logger.setLevel(logging.DEBUG if verbose else logging.INFO)
    return logger