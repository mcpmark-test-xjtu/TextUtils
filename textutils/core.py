"""
Core text processing functions
"""


def reverse_string(text: str) -> str:
    """
    Reverse a string.
    
    Args:
        text: Input string to reverse
        
    Returns:
        Reversed string
        
    Example:
        >>> reverse_string("hello")
        'olleh'
    """
    return text[::-1]


def count_words(text: str) -> int:
    """
    Count the number of words in a text.
    
    Args:
        text: Input text
        
    Returns:
        Number of words
        
    Example:
        >>> count_words("Hello world")
        2
    """
    return len(text.split())


def to_title_case(text: str) -> str:
    """
    Convert text to title case.
    
    Args:
        text: Input text
        
    Returns:
        Text in title case
        
    Example:
        >>> to_title_case("hello world")
        'Hello World'
    """
    return text.title()


def remove_whitespace(text: str) -> str:
    """
    Remove all whitespace from text.
    
    Args:
        text: Input text
        
    Returns:
        Text without whitespace
        
    Example:
        >>> remove_whitespace("hello world")
        'helloworld'
    """
    return ''.join(text.split())


def is_palindrome(text: str, ignore_case: bool = True, ignore_spaces: bool = True) -> bool:
    """
    Check if text is a palindrome.
    
    Args:
        text: Input text to check
        ignore_case: Whether to ignore case differences
        ignore_spaces: Whether to ignore spaces
        
    Returns:
        True if text is a palindrome, False otherwise
        
    Example:
        >>> is_palindrome("racecar")
        True
        >>> is_palindrome("A man a plan a canal Panama")
        True
    """
    processed = text
    
    if ignore_spaces:
        processed = processed.replace(' ', '')
    
    if ignore_case:
        processed = processed.lower()
    
    return processed == processed[::-1]

