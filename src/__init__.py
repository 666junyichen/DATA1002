"""
DATA1002 Project Source Package

This package contains utility modules for data processing and analysis.
"""

__version__ = '1.0.0'
__author__ = 'Jun Yi Chen'

from .data_processing import (
    load_data,
    check_missing_values,
    handle_missing_values,
    detect_outliers,
    normalize_data,
    get_summary_statistics
)

__all__ = [
    'load_data',
    'check_missing_values',
    'handle_missing_values',
    'detect_outliers',
    'normalize_data',
    'get_summary_statistics'
]
