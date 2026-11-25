"""
Lecture 010: Store Frequency Distribution in Dictionary (Hashing Foundation)
Course: Code & Debug DSA Python Course - Part 10
Date: 2026-11-25

Intuition & Approach:
- To count the occurrences of each element in an array/list, use a hash map (Python dictionary).
- For every element x:
  - If x already in dict: increment its count `freq[x] += 1`
  - Else: initialize count `freq[x] = 1`
- Alternative Pythonic methods:
  - Using `freq[x] = freq.get(x, 0) + 1`
  - Using `collections.Counter(arr)`

Complexity Analysis:
- Time Complexity:  O(n) - Single pass over the array of length n. Dictionary lookup/insert is O(1) average.
- Space Complexity: O(u) - Where u is the number of unique elements stored in the dictionary (at most O(n)).
"""

from collections import Counter


def count_frequency_iterative(arr: list) -> dict:
    """
    Standard approach using explicit if-else key lookup.
    """
    freq = {}
    for item in arr:
        if item in freq:
            freq[item] += 1
        else:
            freq[item] = 1
    return freq


def count_frequency_get(arr: list) -> dict:
    """
    Cleaner approach using dict.get().
    """
    freq = {}
    for item in arr:
        freq[item] = freq.get(item, 0) + 1
    return freq


def test_frequency():
    sample = [2, 3, 4, 2, 3, 5, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
    expected = {2: 2, 3: 18, 4: 1, 5: 1}
    
    res1 = count_frequency_iterative(sample)
    res2 = count_frequency_get(sample)
    res3 = dict(Counter(sample))

    assert res1 == expected, f"res1 failed: {res1}"
    assert res2 == expected, f"res2 failed: {res2}"
    assert res3 == expected, f"res3 failed: {res3}"

    print(f"Original list length: {len(sample)}")
    print(f"Frequency Distribution: {res1}")
    print("\nAll test cases passed successfully across all approaches!")


if __name__ == "__main__":
    test_frequency()
