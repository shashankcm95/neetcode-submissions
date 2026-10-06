class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count = 0
        cur_count = 0
        for num in nums:
            if num == 1:
                cur_count += 1
            else:
                max_count = max(cur_count, max_count)
                cur_count = 0
        return max(cur_count, max_count)

        