
#https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def func(mid,nums): # here the mid is the capacity which we are checking whether it can get get the whole package shipped in the given days
            sums=0
            days_cnt=0
            for i in range(0,len(nums)):
                sums+=nums[i]
                if sums>mid:
                    sums=nums[i]
                    days_cnt+=1
            if sums<=mid:
                days_cnt+=1
            return days_cnt
        
        low = max(weights)
        high = sum(weights)
        ans=0
        while low<=high:
            mid = (low+high)//2
            if func(mid,weights)<=days:
                ans = mid
                high = mid-1
            else:

                low=mid+1
        return ans
            
