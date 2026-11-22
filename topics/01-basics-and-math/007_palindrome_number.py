"""
Lecture 007: Check if a Number is Palindrome or Not (LeetCode 9: Palindrome Number)
Course: Code & Debug DSA Python Course - Part 7
Date: 2026-11-22

Intuition & Approach:
- A number is a palindrome if it reads the same forward and backward.
- Negative numbers (e.g., -121) are NOT palindromes because of the leading minus sign.
- Extract digits from right to left using `num % 10` and reconstruct the reversed number:
    `reversed_num = (reversed_num * 10) + last_digit`
    `num = num // 10`
- Compare the reversed number with the original number.

Complexity Analysis:
- Time Complexity:  O(log10(N)) - The while loop runs equal to the number of digits d = floor(log10(N)) + 1.
- Space Complexity: O(1) - Only a few integer variables (constant auxiliary space).
"""

def is_palindrome(n: int) -> bool:
    """
    Checks if an integer n is a palindrome using mathematical digit reversal.
    """
    # Negative numbers are never palindromes (e.g. -121 reversed is 121-)
    if n < 0:
        return False
    
    # 0 is a palindrome
    if n == 0:
        return True

    original = n
    reversed_num = 0
    temp = n

    while temp > 0:
        last_digit = temp % 10
        reversed_num = (reversed_num * 10) + last_digit
        temp = temp // 10

    return reversed_num == original


def test_palindrome():
    test_cases = [
        (121, True),
        (-121, False),
        (10, False),
        (12321, True),
        (0, True),
        (7, True),
        (12345, False)
    ]
    for num, expected in test_cases:
        actual = is_palindrome(num)
        assert actual == expected, f"Failed for {num}: expected {expected}, got {actual}"
        print(f"Number: {num:<8} -> {'Palindrome' if actual else 'Not Palindrome'} (Expected: {expected})")
    print("\nAll test cases passed successfully!")


if __name__ == "__main__":
    test_palindrome()
