"""
Lecture 008: Armstrong Number (LeetCode 1134: Armstrong Number)
Course: Code & Debug DSA Python Course - Part 8
Date: 2026-11-23

Intuition & Approach:
- An Armstrong number (or Narcissistic Number) is a number that is equal to 
  the sum of its own digits each raised to the power of the number of digits (k).
- Example: 153 has 3 digits. 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153 (Armstrong!)
- Example: 9474 has 4 digits. 9^4 + 4^4 + 7^4 + 4^4 = 6561 + 256 + 2401 + 256 = 9474 (Armstrong!)

Steps:
1. Find the number of digits `k = len(str(n))` (or using `int(log10(n)) + 1`).
2. Extract each digit from right to left using `num % 10`.
3. Raise each digit to the power of `k` and accumulate into `total_sum`.
4. Reduce `num = num // 10`.
5. Check if `total_sum == original_n`.

Complexity Analysis:
- Time Complexity:  O(log10(N)) - Finding number of digits and the extraction loop both take O(log10(N)) steps.
- Space Complexity: O(1) - Constant auxiliary space.
"""

from math import log10

def is_armstrong(n: int) -> bool:
    """
    Checks if an integer n is an Armstrong number.
    """
    if n < 0:
        return False
    if n == 0:
        return True

    original = n
    # Number of digits
    nod = int(log10(n)) + 1
    
    total_sum = 0
    temp = n
    while temp > 0:
        ld = temp % 10
        total_sum += (ld ** nod)
        temp = temp // 10

    return total_sum == original


def test_armstrong():
    test_cases = [
        (153, True),
        (370, True),
        (371, True),
        (9474, True),
        (1634, True),
        (1, True),
        (0, True),
        (123, False),
        (100, False),
        (500, False)
    ]
    for num, expected in test_cases:
        actual = is_armstrong(num)
        assert actual == expected, f"Failed for {num}: expected {expected}, got {actual}"
        print(f"Number: {num:<6} -> {'Armstrong' if actual else 'Not Armstrong'} (Expected: {expected})")
    print("\nAll test cases passed successfully!")


if __name__ == "__main__":
    test_armstrong()
