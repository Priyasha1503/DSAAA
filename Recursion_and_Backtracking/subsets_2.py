
#https://leetcode.com/problems/subsets-ii/

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort()    #always have to sort - in the remove duplicates logic   ---In rec and backtarcking, remove duplicates pattern - step1
        def helper(ind,arr):
            res.append(arr[:])
            for i in range(ind,len(nums)):
                if ind<i and nums[i]==nums[i-1]:   # --- remove duplciates pattern - step2
                    continue     
                arr.append(nums[i])
                helper(i+1,arr)
                arr.pop()

        helper(0,[])
        return res
