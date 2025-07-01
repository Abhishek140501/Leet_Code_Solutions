# 🏛️ Roman to Integer – LeetCode Problem #13

## 🧩 Problem Statement

Roman numerals are represented by seven different symbols:

| Symbol | Value |
|--------|-------|
| I      | 1     |
| V      | 5     |
| X      | 10    |
| L      | 50    |
| C      | 100   |
| D      | 500   |
| M      | 1000  |

For example:
- 2 is written as `II`.
- 12 is written as `XII`.
- 27 is written as `XXVII`.

However, some numbers require subtraction:
- 4 is written as `IV` (not `IIII`).
- 9 is written as `IX`.
- 40 is `XL`, 90 is `XC`, 400 is `CD`, 900 is `CM`.

### ✅ Objective:
Given a Roman numeral, convert it to an integer.

---

## 📥 Input
- A string `s` representing a valid Roman numeral.
- `1 <= s.length <= 15`
- Only characters: `('I', 'V', 'X', 'L', 'C', 'D', 'M')`

## 📤 Output
- An integer representing the value of the Roman numeral.

---

## 🧠 Examples

```python
Input: s = "III"
Output: 3

Input: s = "LVIII"
Output: 58
Explanation: L = 50, V = 5, III = 3

Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90, IV = 4

🚀 How It Works
Traverse the string from right to left.

If the current symbol's value is less than the previous, subtract it.

Otherwise, add it.

This handles all subtraction cases correctly like IV, IX, etc.

🏷️ Tags
String Hash Map Greedy LeetCode Easy

©️ License
This project is licensed under the MIT License.

👨‍💻 Author
Abhishek Anand


