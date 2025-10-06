class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        there are n cars  travelling to the same direction on a one lane highway 
        we are given two arrrays of integers position and speed both of lenght n 

        position[i] is the position of ith car inmiles and speed[i] is the speed . 

        a car can not pass another car ahead of it  but can drive at the same speed .

        here if the car catches the fleet right ahead of destination , we will consider the 
        car fleet right .  

        [1,4] start position 1 ->4->7->10
            for 4 postion 4->6->8->.  10 
            so fleet at 10   so  1 

        [3,2]
        stack problem so lets use the brain , dimag khiyam 

        we have to itirate with right one as  it means the higher position one
        here we are using zip funtion allows you to combine multiple lists or 
        other iterables (like tuples, sets, or even strings) into one iterable of tuples
        """   

        pair =[[p,s] for p ,s in zip(position,speed)]#list comprehension in python     
        stack =[] #for the fleet 
        for p,s in sorted(pair)[::-1]: #reverse sorted order
            stack.append((target-p)/s) #here in stack we are calculationg the time 
            #so if the car wiht min position reaches the destination first then that will be fleet 

            if len(stack)>= 2 and stack[-1]<=stack[-2]:
                stack.pop()
        return(len(stack))
