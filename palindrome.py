def palindrome(s: str) -> bool:
    """
    Check if a string is a palindrome. A palindrome is a word, phrase, number, or other sequence of characters which reads the same backward or forward.

    Args:
    s (str): input string to check

    Returns:
    bool: True if the string is a palindrome, False otherwise

    Example:
    >>> palindrome("racecar")
    True
    >>> palindrome("hello")
    False
    >>> palindrome("a")
    True
    """
    for i in range(len(s)//2+1):
        if s[i] != s[len(s) - i - 1]:
            return False
    
    return True
