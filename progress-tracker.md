# 📅 Daily DSA Progress Tracker

Keep track of your daily study session, lecture numbers, problems solved, and key takeaways.

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
- [x] Watch lecture video from the [Code & Debug Course](https://youtube.com/playlist?list=PLhR2IpV1b2FwWwviBHRrR118YAaSlyhTU&si=q0sPCdlg3LjogugN)
- [x] Understand edge cases (e.g. single digit, 0, negative numbers)
- [x] Analyze Time & Space Complexity
- [x] Implement iterative and/or mathematical logic
- [x] Run assertions / test cases
- [x] Add an entry in this tracker
- [x] Commit & push to GitHub
