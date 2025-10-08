class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Bianary serch question -> we are given an array of distint integers
        nums , sorted in ascending order , and an integer target . 

        we have to implement   funtion to search for target within nums 
        if it exist return the true or -1
        """
        l=0
        r= len(nums)-1

        while l<=r:
            m = (l+r)//2
            if nums[m] < target:
                l=m+1
            elif nums[m] > target:
                r=m-1
            else:
                return m
        return -1


        
