"""Module providing a factorial function.

The function `factorial(n)` calculates the factorial of a non‑negative
integer `n`. It implements the standard mathematical definition:

- `factorial(0) == 1`
- `factorial(1) == 1`
- For `n > 1`, `factorial(n) == n * factorial(n-1)`.

The function raises a :class:`ValueError` if a negative integer is
provided.
"""

from __future__ import annotations

__all__ = ["factorial"]


def factorial(n: int) -> int:
    """Return the factorial of a non‑negative integer.

    Parameters
    ----------
    n : int
        Non‑negative integer whose factorial is to be computed.

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
        raise ValueError("n must be a non-negative integer")
    if n <= 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# If the module is run directly, perform a simple demonstration.
if __name__ == "__main__":
    import sys
    for arg in sys.argv[1:]:
        try:
            val = int(arg)
            print(f"factorial({val}) = {factorial(val)}")
        except Exception as exc:
            print(f"Error for {arg}: {exc}")

