"""
TextUtils - A Simple Text Processing Library

Provides utilities for common text operations.
"""

__version__ = "0.1.0"
__author__ = "TextUtils Contributors"

from .core import (
    reverse_string,
    count_words,
    to_title_case,
    remove_whitespace,
    is_palindrome
)

__all__ = [
    'reverse_string',
    'count_words',
    'to_title_case',
    'remove_whitespace',
    'is_palindrome'
]

