# https://leetcode.com/problems/remove-element/description/

class Solution:
    def removeElement(self) -> int:
        nums = [0,1,2,2,3,0,4,2]
        val = 2
        
        k = 0
        
        for index in range(len(nums)):
            if nums[index] == val:
                nums[index] = 9999
            else:
                k = k + 1
        
        nums.sort()
        print(nums)
        return k
q = Solution()
q.removeElement()
