class Solution:
    def findMin(self, nums: List[int]) -> int:

        """
        we have to find the minimum in rotated sorted array . 
        [1,2,3,4,5,6]-> rotated 4 times ->[6,1,2,3,4,5]->[5,6,1,2,3,4]->[4,5,6,1,2,3]->[3,4,5,6,1,2]
        what might be logic lets use the brain -> so , here mid point is 5 
        bianary search 
        so this will be 2 pointer left and right and mean of that ->r+l/2

        so how i will try to solve the problem . 

        so here what are we doing is finding the midpoint so if the nums[m]>= nums[l] then we will change the left pointer to the m+1
        and vice versa 

        for example we will do an example we will turn it 5 times 

        [2,3,4,5,6,1] -> midpoint = 4 is 4>2 yes then we will change the l pointer  at m+1 
        5<6 so increase the left pointer at 1 -> l=r=m 

        so lets take another example here 
        we will move just by 1 time 

        [6,1,2,3,4,5]-> here midpoint is 2 it is smaller than 6  we will change the right pointer to midpoint-1
        here 6>1 ie midpoint is greater than r pointer then 1 

        also the next logic and very important one if our middle point belongs to the left part we will sort the elemnt in the right 
        and if we will have our midpoint on the right part then we will find at the left. 

        nums[m] >= nums[l]:
            search Right 
        else:
            search left 

        
        """
        res = nums[0]
        l,r = 0,len(nums)-1

        while l <=r:
            if nums[l]< nums[r]:
                res = min(res,nums[l])
                break # if this condition met then we dont have to use the while condition . 

            m =(l+r)//2
            res = min(res,nums[m])
            if nums[m] >= nums[l]:
                l=m+1
            else:
                r=m-1
        return res 
            

        
