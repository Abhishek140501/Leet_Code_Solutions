# Leet_Code_Solutions

This repository contains solutions to popular LeetCode problems solved using Python. Each problem is implemented in a clean, readable format, with a focus on clarity and efficiency.

## 📘 Problem: Longest Substring Without Repeating Characters

**Problem Link:** [LeetCode #3](https://leetcode.com/problems/longest-substring-without-repeating-characters/)

### 🧩 Description

Given a string `s`, find the length of the longest substring without repeating characters.

### ✅ Examples

**Example 1:**
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.


**Example 2:**
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.



**Example 3:**
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.



### 💡 Approach

- Use a **sliding window** technique with two pointers.
- Maintain a **hash map** to store the last index of every character.
- If a character is repeated, move the `left` pointer to the next index of its previous occurrence.
- Keep track of the **maximum length** of substring without repeating characters.

### 🧠 Code (Python)

```python
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        char_index_map = {}
        left = 0
        max_length = 0

        for right in range(len(s)):
            if s[right] in char_index_map and char_index_map[s[right]] >= left:
                left = char_index_map[s[right]] + 1
            char_index_map[s[right]] = right
            max_length = max(max_length, right - left + 1)
        
        return max_length

📂 Folder Structure

Leet_Code_Solutions/
├── 3-LongestSubstringWithoutRepeatingCharacters/
│   ├── solution.py
│   └── README.md

👨‍💻 Author
Abhishek Anand

📝 License
This project is licensed under the MIT License.