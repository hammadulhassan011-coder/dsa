# 📅 Daily DSA Progress Tracker

Keep track of your daily study session, lecture numbers, problems solved, and key takeaways.

---

### 🌟 Day 1 — 2026-11-21

| Lecture # | Module | Problem / Concept | Difficulty | Status | Solution Files | Notes & Key Takeaways |
|:---:|---|---|:---:|:---:|---|---|
| **005** | Basics & Math | Extraction of Digits using Loops | Easy | ✅ Completed | [`1st_day2.py`](./1st_day2.py) & [`005_digit_extraction.py`](./topics/01-basics-and-math/005_digit_extraction.py) | • `n % 10` gives the last digit.<br>• `n // 10` truncates the last digit.<br>• Time Complexity: $O(\log_{10} N)$. |
| **006** | Basics & Math | Count Number of Digits in an Integer | Easy | ✅ Completed | [`1st_day.py`](./1st_day.py), [`1st_day3.py`](./1st_day3.py), [`1st_day4.py`](./1st_day4.py), [`006_count_digits.py`](./topics/01-basics-and-math/006_count_digits.py) | • **Brainstormed approach**: dynamic modulo threshold comparison.<br>• **Standard loop**: `while num > 0: num //= 10` with count accumulator ($O(\log_{10} N)$).<br>• **Optimal $O(1)$ Math**: `int(log10(n) + 1)` using `math.log10`. |

---

### 💡 Daily Practice Checklist
- [x] Watch lecture video from the [Code & Debug Course](https://youtube.com/playlist?list=PLhR2IpV1b2FwWwviBHRrR118YAaSlyhTU&si=q0sPCdlg3LjogugN)
- [x] Understand edge cases (e.g. single digit, 0, large numbers)
- [x] Implement iterative and optimized logic
- [x] Run assertions / test cases
- [x] Add an entry in this tracker
- [x] Commit & push to GitHub
