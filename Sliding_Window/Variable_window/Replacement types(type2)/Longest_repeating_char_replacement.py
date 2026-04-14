
#https://leetcode.com/problems/longest-repeating-character-replacement/

from collections import Counter

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''maxlen=0
        for i in range(0,len(s)):
            cnt=0
            for j in range(i,len(s)):
                substr=s[i:j+1]
                length=j-i+1
                c=Counter(substr)
                max_freq=0
                for x in c:
                    if c[x]>max_freq:
                        max_freq=c[x]
                if length-max_freq<=k:
                    maxlen=max(maxlen,length)
        return maxlen'''


        maxlen=0
        left=0
        right=0
        mpp=dict()
        max_freq=0
        while right<len(s):
            mpp[s[right]]=mpp.get(s[right],0)+1
            if mpp[s[right]]>max_freq:
                max_freq=mpp[s[right]]
            while right-left+1 -max_freq>k:   #How many characters we need to replace to make the whole substring same
                mpp[s[left]]-=1
                if mpp[s[left]]==0:
                    del mpp[s[left]]
                left+=1
                max_freq=0
                for x in mpp:
                    if mpp[x]>max_freq:
                        max_freq=mpp[x]
            maxlen=max(maxlen,right-left+1)
            right+=1
        
        return maxlen

