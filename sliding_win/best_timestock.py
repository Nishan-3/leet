
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        """
        This is 2 pointer problem but the easy one so here , we have given 
        integer array prices 
        price[i] is the price of nishancoin on the ith day 
        we may use the single day to buy this and seperate day to sell it 

        we may not to choose the transaction 
        we should solve this in 0(n) time -> loop 
        and o(1) space 
        """

        l,r = 0,1
        res = 0

        while  r<len(prices):
            if prices[l] < prices[r]: 
                profit = prices[r]-prices[l]
                res = max(profit,res)
                r+=1
                
            else:
                l=r# here because if the profit is -1 then we have to slide the window . 
                r+=1
        return res



        
