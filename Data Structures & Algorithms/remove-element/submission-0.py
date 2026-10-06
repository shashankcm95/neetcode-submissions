class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        last_index = len(nums) - 1
        while i <= last_index:
            if nums[i] == val:
                nums[i] = nums[last_index]
                last_index -= 1
            else:
                i += 1
        return i

        