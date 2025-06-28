# Palindrome Number – LeetCode Problem 9

## 🧩 Problem Statement

Given an integer `x`, return `true` if `x` is a **palindrome**, and `false` otherwise.

A palindrome number is a number that reads the same backward as forward.

### ✅ Examples

| Input  | Output | Explanation                                  |
|--------|--------|----------------------------------------------|
| 121    | true   | Reads the same backward and forward          |
| -121   | false  | Becomes `121-` when reversed → Not same      |
| 10     | false  | Becomes `01` when reversed → Not same        |

### 🔒 Constraints

- -2³¹ ≤ x ≤ 2³¹ - 1

---

## 💡 Follow-up

**Can you solve it without converting the integer to a string?**

---

## ✅ Solution 1: Using String Conversion (Simple)

```python
class Solution(object):
    def isPalindrome(self, x):
        x_str = str(x)
        return x_str == x_str[::-1]
🧠 Logic
Convert the integer to a string.

Reverse the string and compare with the original.

📁 How to Run
Clone the repository.

Place the solution file (e.g., palindrome_number.py) in the folder.

Run:
python palindrome_number.py


📝 License
This project is licensed under the MIT License.

Author: ABHISHEK ANAND
```
