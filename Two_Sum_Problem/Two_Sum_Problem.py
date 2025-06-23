class Solution:
    def twoSum(self, nums, target):
        num_indices = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_indices:
                return [num_indices[complement], i]
            num_indices[num] = i
        return []

def _driver():
    solution = Solution()

    nums1 = [2, 7, 11, 15]
    target1 = 9
    print(solution.twoSum(nums1, target1))

    nums2 = [2, 3, 4]
    target2 = 6
    print(solution.twoSum(nums2, target2))

    nums3 = [3, 3]
    target3 = 6
    print(solution.twoSum(nums3, target3))

if __name__ == "__main__":
    _driver()
