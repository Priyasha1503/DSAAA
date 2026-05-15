
#https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/


class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def func(mid): # her mid is th divisor number, not any index
            sums=0
            for i in range(0,len(nums)):
                sums+=(ceil(nums[i]/mid))
            return sums




        low = 1
        high = max(nums)
        ans=0
        while low<=high:
            mid=(low+high)//2 #mid here is gng to be the divisor number
            res = func(mid)
            if res<=threshold:
                ans = mid
                high = mid-1
            else:
                low=mid+1
        return ans
