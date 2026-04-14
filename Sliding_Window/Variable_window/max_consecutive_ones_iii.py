
#https://leetcode.com/problems/max-consecutive-ones-iii/
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l=0
        r=0
        maxlen=0
        zerocnt=0
        #in q - they ahev asked us to return max number of consecutive ones in the array if I can flip atmost k zeroes..
        #we are dng the reverse enginnerign and not conecntrating on1  ..but 0 where we are conecntraiting on the condn of atmost zeroes..so that we get the maxlen which also has 1's covered up.


        while r<len(nums):
            if nums[r]==0:   #here we are coutnign the zero's
                zerocnt+=1
            while zerocnt>k:  #and checking the condnd of if it isn't atmost zeroes 
                if nums[l]==0: #this says that if l ptr value is zero..we are gng to decrement the zerocnt
                    zerocnt-=1
                l+=1
            maxlen=max(maxlen,r-l+1)
            r+=1
        
        return maxlen
