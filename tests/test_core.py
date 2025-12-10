"""
Tests for core text processing functions
"""

import pytest
from textutils.core import (
    reverse_string,
    count_words,
    to_title_case,
    remove_whitespace,
    is_palindrome
)


class TestReverseString:
    def test_simple_string(self):
        assert reverse_string("hello") == "olleh"
    
    def test_empty_string(self):
        assert reverse_string("") == ""
    
    def test_single_char(self):
        assert reverse_string("a") == "a"


class TestCountWords:
    def test_multiple_words(self):
        assert count_words("hello world") == 2
    
    def test_single_word(self):
        assert count_words("hello") == 1
    
    def test_empty_string(self):
        assert count_words("") == 0
    
    def test_multiple_spaces(self):
        assert count_words("hello  world  test") == 3


class TestToTitleCase:
    def test_lowercase(self):
        assert to_title_case("hello world") == "Hello World"
    
    def test_uppercase(self):
        assert to_title_case("HELLO WORLD") == "Hello World"
    
    def test_mixed_case(self):
        assert to_title_case("hElLo WoRlD") == "Hello World"


class TestRemoveWhitespace:
    def test_with_spaces(self):
        assert remove_whitespace("hello world") == "helloworld"
    
    def test_with_tabs_and_newlines(self):
        assert remove_whitespace("hello\tworld\n") == "helloworld"
    
    def test_no_whitespace(self):
        assert remove_whitespace("helloworld") == "helloworld"


class TestIsPalindrome:
    def test_simple_palindrome(self):
        assert is_palindrome("racecar") is True
    
    def test_not_palindrome(self):
        assert is_palindrome("hello") is False
    
    def test_palindrome_with_spaces(self):
        assert is_palindrome("race car") is True
    
    def test_palindrome_case_insensitive(self):
        assert is_palindrome("RaceCar") is True
    
    def test_complex_palindrome(self):
        assert is_palindrome("A man a plan a canal Panama") is True
    
    def test_case_sensitive(self):
        assert is_palindrome("Racecar", ignore_case=False) is False

