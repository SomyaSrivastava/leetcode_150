# https://leetcode.com/problems/remove-duplicates-from-sorted-array/?envType=study-plan-v2&envId=top-interview-150

def removeDuplicates(self) -> int:
        
        nums = [0,0,1,1,1,2,2,3,3,4]
        
        insertion_index = 1
        unique_element_count = 1
        
        for index in range(len(nums)):
            
            key = nums[index]
            sub_index = index + 1
            
            while(sub_index < len(nums) and key != nums[sub_index]):
                
                nums[insertion_index] = nums[sub_index]
                sub_index = sub_index + 1
                insertion_index = insertion_index + 1
                unique_element_count = unique_element_count + 1
                break
    
        return unique_element_count
