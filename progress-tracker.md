# 📅 Daily DSA Progress Tracker

Keep track of your daily study session, lecture numbers, problems solved, and key takeaways.

---

### 🌟 Day 6 — 2026-11-26

| Lecture # | Module | Problem / Concept | Difficulty | Status | Solution Files | Notes & Key Takeaways |
|:---:|---|---|:---:|:---:|---|---|
| **011** | Basics & Math | Intro to Hashing: Query Frequency Search | Easy | ✅ Completed | [`6th_day.py`](./6th_day.py), [`6th_day1.py`](./6th_day1.py), [`5th_day3.py`](./5th_day3.py), [`011_hashing_intro.py`](./topics/01-basics-and-math/011_hashing_intro.py) | • **Brute Force (Nested Loops - `6th_day.py`):** For every query, scan entire array $\rightarrow O(m \times n)$ Time, $O(1)$ Space. Causes TLE on large arrays.<br>• **Optimal Hash Map (`6th_day1.py`):** Non-nested sequential loops $\rightarrow O(n)$ to build frequency dict + $O(m)$ for queries = **$O(m + n)$ Time**! Uses `hash_map.get(key, 0)` for $O(1)$ safe lookup.<br>• **Space Complexity:** $O(u)$ where $u$ is unique elements in $n$.<br>• **Milestone:** Module 01 (Foundations & Math) completed! 🎉 |

---

### 🌟 Day 5 — 2026-11-25

| Lecture # | Module | Problem / Concept | Difficulty | Status | Solution Files | Notes & Key Takeaways |
|:---:|---|---|:---:|:---:|---|---|
| **009** | Basics & Math | Print All Factors (Optimal $O(\sqrt{n})$) | Easy | ✅ Completed | [`5th_day.py`](./5th_day.py) & [`009_print_all_factors.py`](./topics/01-basics-and-math/009_print_all_factors.py) | • **Optimal Square-Root:** Iterate $1$ to $\lfloor\sqrt{n}\rfloor$, collecting pair factors $(i, n // i)$.<br>• **Time Complexity:** $O(\sqrt{n}) + O(k \log k)$ for sorting.<br>• **Space Complexity:** $O(k)$ for storing factors.<br>• *Important Boundary:* Loop upper bound must be `int(sqrt(num)) + 1` and check `if i != num // i` so perfect squares (e.g., 36) include 6 without duplicating it. |
| **010** | Basics & Math | Store Frequency in Dictionary (Hashing) | Easy | ✅ Completed | [`5th_day2.py`](./5th_day2.py) & [`010_frequency_distribution.py`](./topics/01-basics-and-math/010_frequency_distribution.py) | • **Hash Map / Dict Counting:** Iterate over list and count occurrences in $O(1)$ average lookup time.<br>• **Time Complexity:** $O(n)$ where $n = \text{len}(list)$.<br>• **Space Complexity:** $O(u)$ where $u$ is number of unique elements.<br>• Pythonic alternatives: `freq.get(x, 0) + 1` or `collections.Counter(arr)`. |

---

### 🌟 Day 4 — 2026-11-24

| Lecture # | Module | Problem / Concept | Difficulty | Status | Solution Files | Notes & Key Takeaways |
|:---:|---|---|:---:|:---:|---|---|
| **009** | Basics & Math | Print All Factors / Divisors of a Number | Easy | ✅ Completed | [`3rd_day2.py`](./3rd_day2.py), [`4th_day.py`](./4th_day.py), [`009_print_all_factors.py`](./topics/01-basics-and-math/009_print_all_factors.py) | • **Extreme Brute Force:** Iterates `1` to `n`. Time: $O(n)$, Space: $O(k)$.<br>• **Better Approach:** Iterates `1` to `n // 2` then appends `n`. Time: $O(n/2) \approx O(n)$, Space: $O(k)$. Cuts iterations by 50% since no factor other than $n$ exceeds $n/2$. |

---

### 🌟 Day 3 — 2026-11-23

| Lecture # | Module | Problem / Concept | Difficulty | Status | Solution Files | Notes & Key Takeaways |
|:---:|---|---|:---:|:---:|---|---|
| **008** | Basics & Math | Armstrong Number (LeetCode 1134) | Easy | ✅ Completed | [`3rd_day.py`](./3rd_day.py) & [`008_armstrong_number.py`](./topics/01-basics-and-math/008_armstrong_number.py) | • **Time Complexity:** $O(\log_{10} N)$ — calculating digit count and extraction loop.<br>• **Space Complexity:** $O(1)$ — constant auxiliary memory.<br>• An Armstrong number equals the sum of its digits each raised to power $k$ (number of digits).<br>• Accumulate `total += (ld ** nod)` and compare `total == original_n`. |

---

### 🌟 Day 2 — 2026-11-22

| Lecture # | Module | Problem / Concept | Difficulty | Status | Solution Files | Notes & Key Takeaways |
|:---:|---|---|:---:|:---:|---|---|
| **007** | Basics & Math | Check Palindrome Number (LeetCode 9) | Easy | ✅ Completed | [`2nd_day.py`](./2nd_day.py) & [`007_palindrome_number.py`](./topics/01-basics-and-math/007_palindrome_number.py) | • **Time Complexity:** $O(\log_{10} N)$ — loop runs for $d = \lfloor\log_{10} N\rfloor + 1$ digits.<br>• **Space Complexity:** $O(1)$ — constant scalar variables.<br>• Reverse number using `result = (result * 10) + (num % 10)` and `num //= 10`.<br>• Compare `result == original_n`. Negative numbers cannot be palindromes. |

---

### 🌟 Day 1 — 2026-11-21

| Lecture # | Module | Problem / Concept | Difficulty | Status | Solution Files | Notes & Key Takeaways |
|:---:|---|---|:---:|:---:|---|---|
| **005** | Basics & Math | Extraction of Digits using Loops | Easy | ✅ Completed | [`1st_day2.py`](./1st_day2.py) & [`005_digit_extraction.py`](./topics/01-basics-and-math/005_digit_extraction.py) | • `n % 10` gives the last digit.<br>• `n // 10` truncates the last digit.<br>• Time Complexity: $O(\log_{10} N)$. |
| **006** | Basics & Math | Count Number of Digits in an Integer | Easy | ✅ Completed | [`1st_day.py`](./1st_day.py), [`1st_day3.py`](./1st_day3.py), [`1st_day4.py`](./1st_day4.py), [`006_count_digits.py`](./topics/01-basics-and-math/006_count_digits.py) | • **Brainstormed approach**: dynamic modulo threshold comparison.<br>• **Standard loop**: `while num > 0: num //= 10` with count accumulator ($O(\log_{10} N)$).<br>• **Optimal $O(1)$ Math**: `int(log10(n) + 1)` using `math.log10`. |

---

### 💡 Daily Practice Checklist
- [x] Brainstorm approach before checking solution
- [x] Analyze Time & Space Complexity
- [x] Implement initial solution and test
- [x] Implement optimized approaches
- [x] Add an entry in this tracker
- [x] Commit & push to GitHub
