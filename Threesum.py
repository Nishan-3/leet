

"""
        here we are given array nums 

        nums[i]+num[j]+num[k] == 0 
        so here 
        here input [-1,0,1,2,-1,-4]
        output [[-1,-1,2] [-1,0,1]]

        the solution mustnot contain the duplicate triplets 


        we have to sort it 

        so we will have 2 nested looops 

        one for the 2 sum and the other for the two sum + 1 sum 
        

res = [] # as we have to return the result as the list of list 
nums.sort.()
"""
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if a > 0:
                break

            if i > 0 and a == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

        return res
