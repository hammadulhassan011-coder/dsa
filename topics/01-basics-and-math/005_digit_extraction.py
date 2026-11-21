"""
Lecture 005: Extraction of Digits Using Loops
Course: Code & Debug DSA Python Course - Part 5
Date: 2026-11-21

Intuition & Approach:
- To extract the last digit of a number, use modulo operator: `last_digit = n % 10`
- To remove the last digit and move to the next, use integer division: `n = n // 10`
- Repeat in a while loop until the number becomes 0.

Complexity:
- Time Complexity:  O(log10(N)) - number of iterations equals number of digits
- Space Complexity: O(1) - in-place extraction
"""

def extract_digits(n: int) -> list[int]:
    """
    Extracts and prints digits from right to left.
    Returns a list of extracted digits.
    """
    if n == 0:
        return [0]

    num = abs(n)
    digits = []
    while num > 0:
        last_digit = num % 10
        digits.append(last_digit)
        num = num // 10
    
    return digits


if __name__ == "__main__":
    n = 2432
    print(f"Original number: {n}")
    print("Extracted digits (from right to left):")
    digits = extract_digits(n)
    for d in digits:
        print(d)
