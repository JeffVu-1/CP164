"""
-------------------------------------------------------
Functions.py - functions for Lab 5
-------------------------------------------------------
Author:  Jeff Vu
ID:      169058539
Email:   vuxx8539@mylaurier.ca
__updated__ = "0000-00-00"
-------------------------------------------------------
"""

def recurse(x, y):
    """
    -------------------------------------------------------
    Recursive function - example of tree recursion.
    Use: ans = recurse(x, y)
    -------------------------------------------------------
    Parameters:
        x - an integer (int)
        y - an integer (int)
    Returns:
        ans - the function result (int)
    -------------------------------------------------------
    """
    if x < 0 or y < 0:
        value = x - y
    else:
        value = recurse(x - 1, y) + recurse(x, y - 1)
    return value

def gcd(m, n):
    """
    -------------------------------------------------------
    Recursively find the Greatest Common Denominator of two numbers.
    Use: ans = gcd(m, n)
    -------------------------------------------------------
    Parameters:
        n - an integer (int)
        m - an integer (int)
    Returns:
        ans - the function result (int)
    -------------------------------------------------------
    """
    if m % n == 0:
        value = n
    else:
        value = gcd(n, m % n)
    return value

def vowel_count(s):
    """
    -------------------------------------------------------
    Recursively counts number of vowels in a string.
    Use: count = vowel_count(s)
    -------------------------------------------------------
    Parameters:
        s - string to examine (str)
    Returns:
        count - number of vowels in s (int)
    -------------------------------------------------------
    """
    vowels = "aeiou"
    count = 0
    if s == "":
        value = 0
    else:
        if s[0].lower() in vowels:
            count += 1
        value = count + vowel_count(s[1:])
    return value


def to_power(base, power):
    """
    -------------------------------------------------------
    Calculates base^power.
    Use: ans = to_power(base, power)
    -------------------------------------------------------
    Parameters:
        base - base to apply power to (float)
        power - power to apply (int)
    Returns:
        ans - base ^ power (float)
    -------------------------------------------------------
    """
    if power == 0:
        value = 1
    elif power < 0:
        value = 1 / base * to_power(base, power + 1)
    else:
        value = base * to_power(base, power - 1)
    return value


def is_palindrome(s):
    """
    -------------------------------------------------------
    Recursively determines if s is a palindrome. Ignores non-letters and case.
    Use: palindrome = is_palindrome(s)
    -------------------------------------------------------
    Parameters:
        s - a string (str)
    Returns:
        palindrome - True if s is a palindrome, False otherwise (boolean)
    -------------------------------------------------------
    """
    s = s.lower()
    s = ''.join([char for char in s if char.isalpha()])
    if len(s) <= 1:
        value = True
    elif s[0] != s[-1]:
        value = False
    else:
        value = is_palindrome(s[1:-1])
    return value


def bag_to_set(bag):
    """
    -------------------------------------------------------
    Copies elements of a bag to a set.
    Use: new_set = bag_to_set(bag)
    -------------------------------------------------------
    Parameters:
        bag - a list of values (list)
    Returns:
        new_set - containing one each of the elements in bag (list)
    -------------------------------------------------------
    """
    if len(bag) == 0:
        new_set = []
    else:
        new_set = bag_to_set(bag[:-1])
        if not bag[-1] in new_set:
            new_set.append(bag[-1])
        else:
            new_set = bag_to_set(bag[:-1])
    return new_set
