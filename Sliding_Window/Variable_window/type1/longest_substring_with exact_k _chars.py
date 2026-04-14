
#https://www.geeksforgeeks.org/problems/longest-k-unique-characters-substring0853/1

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
            if len(mpp)==k:
                maxlen=max(maxlen,right-left+1)
            right+=1
        return maxlen        
