class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lp = 1
        rp = 1
        result = [1]
        for i in range(1, len(nums)):
            lp = lp * nums[i-1]
            result.append(lp) 
        for i in reversed(range(len(nums)-1)):
            rp = rp * nums[i+1]
            result[i] = result[i] * rp
        # for i in range(len(l)):    
        #     result.append(l[i] * r[i])

        return result

        # 1, 2, 4, 6
        # 1, 1, 2, 8


        # i/p = [1, 2, 4, 6]

        # l = [1, 1, 2, 8]
        # r = [48 ,24 , 6, 1]

        # o/p = [48, 24, 12, 8]
        # lp = 48* 24 * 12 * 8
        
        