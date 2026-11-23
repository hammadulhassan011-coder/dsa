"""
Lecture 009: Print All Factors / Divisors of a Given Number
Course: Code & Debug DSA Python Course - Part 9
Date: 2026-11-24

Approaches:
1. Brute Force (Self-Coded without watching solution):
   - Iterate i from 1 to n.
   - If n % i == 0, append i to result.
   - Time Complexity:  O(n)
   - Space Complexity: O(k) where k is the number of factors of n.

2. Optimal Approach (Pair Factorization up to sqrt(n) - Coming Up Tomorrow):
   - Factors appear in pairs: if i divides n, then n // i also divides n.
   - Only iterate i from 1 up to floor(sqrt(n)).
   - Time Complexity:  O(sqrt(n))
   - Space Complexity: O(k)
"""

# --- Approach 1: Self-Coded Brute Force ---
def find_factors_brute_force(n: int) -> list[int]:
    """
    Brute force: Checks every integer from 1 to n.
    Time Complexity:  O(n)
    Space Complexity: O(k) where k is the count of factors.
    """
    if n <= 0:
        return []
    
    factors = []
    for i in range(1, n + 1):
        if n % i == 0:
            factors.append(i)
    return factors


# --- Approach 2: Optimal Square-Root Approach ---
def find_factors_optimal(n: int) -> list[int]:
    """
    Optimal: Iterates up to sqrt(n), collecting pairs (i, n // i).
    Time Complexity:  O(sqrt(n)) + O(k log k) for sorting
    Space Complexity: O(k)
    """
    if n <= 0:
        return []
        
    factors = []
    i = 1
    while i * i <= n:
        if n % i == 0:
            factors.append(i)
            if i != n // i:
                factors.append(n // i)
        i += 1
    
    factors.sort()
    return factors


def test_factors():
    test_cases = [
        (33, [1, 3, 11, 33]),
        (36, [1, 2, 3, 4, 6, 9, 12, 18, 36]),
        (1, [1]),
        (13, [1, 13]),
        (100, [1, 2, 4, 5, 10, 20, 25, 50, 100])
    ]
    for num, expected in test_cases:
        bf = find_factors_brute_force(num)
        opt = find_factors_optimal(num)
        assert bf == expected, f"BF failed for {num}: expected {expected}, got {bf}"
        assert opt == expected, f"Opt failed for {num}: expected {expected}, got {opt}"
        print(f"Factors of {num:<4}: {bf}")
    print("\nAll test cases passed successfully!")


if __name__ == "__main__":
    test_factors()
