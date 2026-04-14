
#https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/



class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left=0
        right=0
        zero_cnt=0
        maxlen=0
        while right<len(nums):
            if nums[right]==0:
                zero_cnt+=1
            while zero_cnt>1:  #if can be writen here for optimization as well , but since here we are chekcing for 1 element itslef -- if is more fine
            #MEANING OF ABOVE LOOP - CHECKING IF IT ISN'T ATMOST MORE THAN 1 ZERO
                if nums[left]==0:
                    zero_cnt-=1
                left+=1
            maxlen=max(maxlen,right-left+1)
            right+=1
        
        return maxlen-1

        
