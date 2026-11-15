"""A simple factorial implementation.

This module provides a ``factorial`` function that calculates the
factorial of a non‑negative integer. It raises ``ValueError`` for
negative numbers and for any non‑integer input.

The module can be run as a script to print the factorial of a
sample number (5 in this case).
"""

from typing import Union


+def factorial(n: Union[int, float]) -> int:
+    """Return the factorial of ``n``.
+
+    Parameters
+    ----------
+    n : int or float
+        The number for which the factorial should be computed.
+
+    Returns
+    -------
+    int
+        The factorial of ``n``.
+
+    Raises
+    ------
+    ValueError
+        If ``n`` is negative or not an integer.
+    """
+
+    # Input validation – only non‑negative integers are allowed
+    if not isinstance(n, int):
+        # ``float`` values that are mathematically integer are not
+        # considered valid input for this implementation.
+        raise ValueError("Input must be an integer.")
+    if n < 0:
+        raise ValueError("Input must be non‑negative.")
+
+    # Factorial of 0 and 1 is defined to be 1.
+    if n in (0, 1):
+        return 1
+
+    result = 1
+    for i in range(2, n + 1):
+        result *= i
+    return result
+
+
+if __name__ == "__main__":
+    # Demo: print factorial of 5
+    print(factorial(5))

