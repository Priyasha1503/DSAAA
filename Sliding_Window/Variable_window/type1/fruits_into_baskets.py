
#https://leetcode.com/problems/fruit-into-baskets/

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left=0
        right=0
        maxlen=0
        mpp=dict()
        while right<len(fruits):
            mpp[fruits[right]]=mpp.get(fruits[right],0)+1
            if len(mpp)>2:   #we can sue here while, but if is for optimization
                mpp[fruits[left]]-=1
                if mpp[fruits[left]]==0:
                    del mpp[fruits[left]]
                left+=1
            maxlen=max(maxlen,right-left+1)
            right+=1

        return maxlen 
