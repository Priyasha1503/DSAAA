
#https://leetcode.com/problems/combination-sum-iii/

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res=[]

        def helper_func(ind,arr,target):
            if target==0 and len(arr)==k:
                res.append(arr[:])
                return
                
            for i in range(ind,10):
                if i>target:
                    break
                arr.append(i)
                helper_func(i+1,arr,target-i)
                arr.pop()

        helper_func(1,[],n)
        return res
