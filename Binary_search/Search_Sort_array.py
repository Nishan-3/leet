class Solution:
    def search(self, nums: List[int], target: int) -> int:

        """
        I believe that both of the question is kinda same one 
        so lets brainstrom 

        [3,4,5,6,1,2] target =1 
        lets check the first condition 
        base case target <nums[m]
            l=m+1

            m =(l+r)//2

            here l<r? no then 
            we will use logic 

            nums[m]>
        """
        l,r = 0 , len(nums)-1
        while l <= r:
            middle = (l+r)//2
            #first condition  if target is equal to the middle value then 
            if target == nums[middle]:
                return middle
            #left sorted potion 

            if nums[l] <= nums[middle]:
                if target > nums[middle] or target < nums[l]:
                    l= middle+1
                else:
                     r = middle-1
            
            #right sorted array 
            else:
                if target < nums[middle] or target >nums[r]:
                    r = middle-1
                else:
                    l= middle+1
        
        return -1



                
                


            #this is right part


        

        
