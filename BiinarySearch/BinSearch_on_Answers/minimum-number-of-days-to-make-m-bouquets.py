

#https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/

class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m*k>len(bloomDay):
            return -1
        def func(mid,nums): #intnetion :to chekc ewhwther the mid day will give m boq or not
            cnt=0
            total_boq=0
            for i in range(0,len(nums)):
                if nums[i]<=mid: #mid here is not index
                    cnt+=1
                else:
                    total_boq+=(cnt//k)
                    cnt=0
            total_boq+=(cnt//k)
            if total_boq>=m:
                return True
            else:
                return False
        ans=0
        low = min(bloomDay)
        high = max(bloomDay)
        while low<=high:
            mid = (low+high)//2
            res = func(mid,bloomDay)
            if res:
                ans = mid

                high=mid-1
            else:
                low=mid+1
        return ans

