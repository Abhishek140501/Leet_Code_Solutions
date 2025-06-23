# Two Sum Problem

This project contains a Python solution to the classic **Two Sum** problem from LeetCode.

## Problem Statement

Given an array of integers `nums` and an integer `target`, return the indices of the two numbers such that they add up to the target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

## Example

```python
Input: nums = [2,7,11,15], target = 9  
Output: [0,1]  # Because nums[0] + nums[1] == 9
Solution
The solution uses a dictionary to store previously visited numbers and their indices.
For each number, we check if the complement (target - current number) exists in the dictionary.

Time Complexity: O(n)
Space Complexity: O(n)

Files
Two_Sum_Problem.py – Python file containing the solution and test cases.

How to Run
python Two_Sum_Problem.py

Author
Abhishek Anand

