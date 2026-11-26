"""
Lecture 011: Introduction to Hashing in Python (Query Frequency Search)
Course: Code & Debug DSA Python Course - Part 11
Date: 2026-11-26

Problem:
Given an array `arr` of size M and a list of query numbers `queries` of size N,
find how many times each query number appears in `arr`.

Approaches:
1. Brute Force (Nested Loops):
   - For each query in `queries`, iterate through entire `arr` counting matches.
   - Time Complexity:  O(N * M) - If N=10^5 and M=10^5, N*M = 10^10 operations (TLE!).
   - Space Complexity: O(1) - Only a scalar counter variable.

2. Optimal Approach using Hashing (Precomputation):
   - Step 1 (Precompute): Traverse `arr` once and store frequencies in a hash map. O(M) time, O(M) space.
   - Step 2 (Fetch): For each query in `queries`, look up frequency in O(1) average time. O(N) time.
   - Overall Time:  O(M + N) - drastically faster!
   - Overall Space: O(M) auxiliary space.
"""

def query_frequencies_brute_force(arr: list[int], queries: list[int]) -> dict[int, int]:
    """
    Brute force approach checking each query against the entire array.
    Time Complexity:  O(N * M)
    Space Complexity: O(1) auxiliary (excluding output)
    """
    results = {}
    for q in queries:
        count = 0
        for x in arr:
            if q == x:
                count += 1
        results[q] = count
    return results


def query_frequencies_hashing(arr: list[int], queries: list[int]) -> dict[int, int]:
    """
    Optimal approach pre-storing frequencies in a hash map.
    Time Complexity:  O(M + N)
    Space Complexity: O(M)
    """
    # Precomputation: O(M)
    freq_map = {}
    for x in arr:
        freq_map[x] = freq_map.get(x, 0) + 1

    # Query fetching: O(N)
    results = {}
    for q in queries:
        results[q] = freq_map.get(q, 0)

    return results


def test_hashing():
    m = [4, 5, 6, 3, 2, 10, 3, 4, 3, 6, 6]
    n = [4, 66, 33, 7, 3, 6]
    expected = {4: 2, 66: 0, 33: 0, 7: 0, 3: 3, 6: 3}

    res_bf = query_frequencies_brute_force(m, n)
    res_hash = query_frequencies_hashing(m, n)

    assert res_bf == expected, f"Brute force failed: {res_bf}"
    assert res_hash == expected, f"Hashing failed: {res_hash}"

    print(f"Array (size {len(m)}): {m}")
    print(f"Queries (size {len(n)}): {n}")
    print(f"Results: {res_bf}")
    print("\nAll test cases passed successfully across both approaches!")


if __name__ == "__main__":
    test_hashing()
