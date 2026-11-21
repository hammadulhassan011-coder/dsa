"""
Lecture 006: Count the Number of Digits in an Integer
Course: Code & Debug DSA Python Course - Part 6
Date: 2026-11-21

Covers 3 Approaches:
1. Self-Brainstormed Remainder Approach (pre-video intuitive solution)
2. Standard Iterative Loop Approach - O(log10(N))
3. Optimal Mathematical Approach using log10 - O(1)
"""

from math import log10

# --- Approach 1: Self-Brainstormed Remainder Check ---
def count_digits_brainstormed(n: int) -> int:
    """
    Intuition: Increase divisor by 10x each step until n % i == n.
    """
    if n == 0:
        return 1
    num = abs(n)
    i = 10
    count = 0
    while True:
        reminder = num % i
        i = i * 10
        count += 1
        if reminder == num:
            break
    return count


# --- Approach 2: Standard Iterative Division O(log10 N) ---
def count_digits_iterative(n: int) -> int:
    """
    Intuition: Continuously divide by 10 until num becomes 0.
    Time Complexity:  O(log10(N))
    Space Complexity: O(1)
    """
    if n == 0:
        return 1
    num = abs(n)
    count = 0
    while num > 0:
        num = num // 10
        count += 1
    return count


# --- Approach 3: Optimal Mathematical Formula O(1) ---
def count_digits_logarithmic(n: int) -> int:
    """
    Intuition: The number of digits in base 10 is floor(log10(n)) + 1.
    Time Complexity:  O(1)
    Space Complexity: O(1)
    """
    if n == 0:
        return 1
    return int(log10(abs(n))) + 1


if __name__ == "__main__":
    test_cases = [9834580853408, 67868, 90249, 7, 1000]
    print("Testing all 3 approaches:")
    for num in test_cases:
        c1 = count_digits_brainstormed(num)
        c2 = count_digits_iterative(num)
        c3 = count_digits_logarithmic(num)
        assert c1 == c2 == c3, f"Mismatch for {num}"
        print(f"Number: {num:<15} -> Digits: {c1}")
    print("All test cases passed across all approaches!")
