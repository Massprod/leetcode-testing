

def gcd(higher: int, lower: int) -> int:
    """
    Calculate the greatest common divisor (GCD) of two numbers using the Euclidean algorithm.

    The GCD of two integers is the largest integer that divides both numbers without leaving a remainder.

    Parameters:
    -----------
    higher : int
        The larger of the two integers (or the first integer). If the values are reversed, the function will still work.

    lower : int
        The smaller of the two integers (or the second integer). This will be reduced using the modulo operation.

    Returns:
    --------
    int
        The greatest common divisor of the two input integers.
    Example:
    --------
    >>> gcd(10, 1)
    1
    >>> gcd(999, 1923)
    3
    """
    if lower == 0:
        return higher
    return gcd(lower, higher % lower)


def convert_to_base(number: int, base: int) -> str:
    """
    Convert an integer to a string representation in the specified base.

    This function converts a given integer to its string representation in an arbitrary base (2 <= base <= 36).
    For bases larger than 10, letters (A-Z) are used to represent values 10-35.

    Parameters:
    -----------
    number : int
        The integer to convert.

    base : int
        The base to convert the number into. Must be greater than or equal to 2 and less than or equal to 36.

    Returns:
    --------
    str
        The string representation of the number in the specified base.

    Example:
    --------
    >>> convert_to_base(9, 2)
    '1001'

    >>> convert_to_base(255, 16)
    'FF'
    """
    if number == 0:
        return '0'

    digits = []
    while number:
        remainder = number % base
        if remainder >= 10:
            # Convert remainder to corresponding letter for base > 10
            digits.append(chr(55 + remainder))  # 'A' is chr(65), so 10 -> 'A', 11 -> 'B', etc.
        else:
            digits.append(str(remainder))
        number //= base

    # Join and reverse the digits to form the correct representation
    return ''.join(digits[::-1])
