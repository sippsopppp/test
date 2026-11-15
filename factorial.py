"""Factorial calculation module.

This module provides a simple recursive implementation of the factorial
function. It raises a :class:`ValueError` if a negative number is
supplied.
"""


def factorial(n: int) -> int:
    """Return the factorial of *n*.

    Parameters
    ----------
    n : int
        The number to compute the factorial of. ``n`` must be a
        non‑negative integer.

    Returns
    -------
    int
        The factorial of ``n``.

    Raises
    ------
    ValueError
        If ``n`` is negative.
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative values.")
    if n == 0:
        return 1
    return n * factorial(n - 1)

