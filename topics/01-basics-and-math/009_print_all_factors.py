"""
Lecture 009: Print All Factors / Divisors of a Given Number
Course: Code & Debug DSA Python Course - Part 9
Date: 2026-11-24

Approaches:
1. Extreme Brute Force:
   - Iterate i from 1 to n.
   - If n % i == 0, append i.
   - Time Complexity:  O(n)
   - Space Complexity: O(k) where k is the number of factors of n.

2. Better Approach (Iteration up to n // 2):
   - No factor of n (except n itself) can be greater than n // 2.
   - Iterate i from 1 to (n // 2), then append n.
   - Loop iterations cut in half!
   - Time Complexity:  O(n/2) ≈ O(n)
   - Space Complexity: O(k)

3. Optimal Approach (Pair Factorization up to sqrt(n)):
   - Factors appear in pairs: if i divides n, then n // i also divides n.
   - Only iterate i from 1 up to floor(sqrt(n)).
   - Time Complexity:  O(sqrt(n)) + O(k log k) for sorting
   - Space Complexity: O(k)
"""

# --- Approach 1: Extreme Brute Force ---
def find_factors_brute_force(n: int) -> list[int]:
    """
    Checks every integer from 1 to n.
    Time Complexity:  O(n)
    Space Complexity: O(k)
    """
    if n <= 0:
        return []
    
    factors = []
    for i in range(1, n + 1):
        if n % i == 0:
            factors.append(i)
    return factors


# --- Approach 2: Better Approach (up to n // 2) ---
def find_factors_better(n: int) -> list[int]:
    """
    Checks integers up to n // 2, then appends n.
    Time Complexity:  O(n/2) ≈ O(n)
    Space Complexity: O(k)
    """
    if n <= 0:
        return []
    if n == 1:
        return [1]

    factors = []
    for i in range(1, (n // 2) + 1):
        if n % i == 0:
            factors.append(i)
    factors.append(n)
    return factors


# --- Approach 3: Optimal Square-Root Approach ---
def find_factors_optimal(n: int) -> list[int]:
    """
    Iterates up to sqrt(n), collecting pairs (i, n // i).
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
        (10, [1, 2, 5, 10]),
        (33, [1, 3, 11, 33]),
        (36, [1, 2, 3, 4, 6, 9, 12, 18, 36]),
        (1, [1]),
        (13, [1, 13]),
        (100, [1, 2, 4, 5, 10, 20, 25, 50, 100])
    ]
    for num, expected in test_cases:
        bf = find_factors_brute_force(num)
        better = find_factors_better(num)
        opt = find_factors_optimal(num)
        assert bf == expected, f"BF failed for {num}: expected {expected}, got {bf}"
        assert better == expected, f"Better failed for {num}: expected {expected}, got {better}"
        assert opt == expected, f"Opt failed for {num}: expected {expected}, got {opt}"
        print(f"Factors of {num:<4}: {better}")
    print("\nAll test cases passed successfully across all 3 approaches!")


if __name__ == "__main__":
    test_factors()
