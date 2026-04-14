
#https://algo.monster/liteproblems/340 
#the above link is for refernece didnt find any excat ones in leetcode etc platforms


class Solution:
    def longestKSubstr(self, s, k):
        # code here
        maxlen=-1
        left=0
        right=0
        mpp=dict()
        while right<len(s):
            mpp[s[right]]=mpp.get(s[right],0)+1
            while len(mpp)>k:
                mpp[s[left]]-=1
                if mpp[s[left]]==0:
                    del mpp[s[left]]
                left+=1
            maxlen=max(maxlen,right-left+1)   #no codnnd..we check for everthing unlike the condn we have for exactly k elements in the before problem
            right+=1
        return maxlen                    
                            

