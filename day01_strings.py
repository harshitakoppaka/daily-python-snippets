"""
Day 01 - String Utilities
"""

def reverse_string(s: str) -> str:
    """Return the reversed version of a string."""
    return s[::-1]


def is_palindrome(s: str) -> bool:
    """Check if a string is a palindrome (case-insensitive)."""
    s = s.lower().replace(" ", "")
    return s == s[::-1]


if __name__ == "__main__":
    print(reverse_string("hello"))
    print(is_palindrome("madam"))
    print(is_palindrome("nurses run"))
