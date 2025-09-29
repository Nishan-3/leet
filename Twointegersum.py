class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        

        """
        here given an array or integer  that is sorted in non -decending order 
        here what is the logic -> we should return the 1-indexed of two numbers .
        index1<index2 
        here in example 
        input = [1,2,3,4] target = 3 
        output =[1,2]

        two pointer so 

        o(n) -time -> loop 
        o(1) spcae we are not using any extra memory 

        so here is the logic we keep 2 pointers left and right in the extreme sides 
        also we will check if the sum of 2 pointers is greater than target then we will 
        decrease the right pointer else we will increase the left as this is sorted we can take advantage of it 
        also here is the thing we need the index of the elemnts so  we have to returnt he index in the 1-indexed 
        that is we have to returnt he index that starts from the first        


        """
        output =[]
        l,r = 0 , len(numbers)-1

        while l < r :
            if numbers[l]+numbers[r] > target:
                r -=1 
            elif numbers[l]+numbers[r] <target:
                l +=1
            else:
                return [l+1,r+1]
         

            

        
