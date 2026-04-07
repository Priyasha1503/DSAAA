
##https://leetcode.com/problems/product-of-array-except-self/

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ''''prefixprod=[1]  # here where ver it is repfixsum, it is suffix sum and vicersa---actually,I understood at the satring wrong

        suffixprod=[1]
        res=[]
        for i in range(0,len(nums)):
            suffixprod.append(suffixprod[-1]*nums[i])                                                                      
        
        for i in range(len(nums)-1,-1,-1):
            prefixprod.append(prefixprod[-1]*nums[i])
        prefixprod=prefixprod[::-1]
        print(prefixprod,suffixprod)
        for i in range(0,len(nums)):
            res.append(suffixprod[i]*prefixprod[i-1])
        
        return res'''

        #APPROACH WITH O(1) EXTRA SPACE COMP
        res=[1]
        for i in range(0,len(nums)):
            res.append(res[-1]*nums[i])
        
        right=1 #this calcualtes product from rigth side
        for i in range(len(nums)-1,-1,-1):

            res[i] = res[i]*right
            right=nums[i]*right

        return res[:-1]



