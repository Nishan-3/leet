class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        """
        input nums =[2,20,4,10,3,4,5]

        output = 4 
        here this is array problem , we  are given  an arrray of integer
         and we have to return the length of the longest consecutive sequence
         of elements that can be formed 


         here consecutinve sequence is a sequence of elements in which each 
         element is exactly 1 greater than the previous element 
        

        here how can we solve in the 0(n) 
        lets think the problem 

        #here we converted into the set 


        """

        numset = set(nums)
        longest =0 
        
        for n in nums :
            if(n-1) not in numset:
                length = 1
                
                while(n+length) in numset:
                    length += 1
                longest = max(length,longest)
        return longest


"""   
here  we first made the hash or set .

so lets take an example so the input nums ={2,20,4,10,3,4,5}

here the first element is 2 we will check if we have (2-1) we dont hvae 1 so its the first element 
leng =1 
now we have 3 or not yes 
len =2 
we have 4 or not yes we do have 
len =3 
we do have 5 or not yes we do have so we solved in this way  






in this set we have so we (20-1)  not in the set so 20 is of len 1 so (20+1) 
no we dont have so the value is 1 now 

now (4-1) 3 present so no 


19  no we dont have not (4-1) we have 3 so lenght is 1 now 

"""







        
