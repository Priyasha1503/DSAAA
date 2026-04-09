
#https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        '''cnt=0
        for i in range(0,len(s)):
            for j in range(i,len(s)):
                sets=set(s[i:j+1])
                if sets=={'a','b','c'}:
                    cnt+=1
        return cnt'''

        ## BETTER APPRAOCH
        '''l,r=0,0
        sets=set()
        cnt=0
        while r<len(s):
            sets.add(s[r])
            if sets=={'a','b','c'}:
                cnt+=1
                cnt+=(len(s)-1-r)
                sets.remove(s[l])
                l+=1
            r+=1
        
        return cnt'''
        #using sliding window



        
        sets={"a","b","c"}
        left=0
        right=0
        while right<len(nums):
            
        
        #UNIQUE AND FANTASTIC APPRAOCH
        '''cnt=0
        lastseen=[-1,-1,-1]
        for i in range(0,len(s)):
            if s[i]=='a':
                lastseen[0]=i
            elif s[i]=='b':
                lastseen[1]=i
            else:
                lastseen[2]=i
            #check for min window or if every thing is ther
            if lastseen[0]!=-1 and lastseen[1]!=-1 and lastseen[2]!=-1:
                cnt=cnt+(1+min(lastseen))
        return cnt'''
