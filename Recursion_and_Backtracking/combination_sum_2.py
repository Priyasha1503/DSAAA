
#https://leetcode.com/problems/combination-sum-ii/

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res=[]
        candidates.sort()
        def helper(ind,arr,target):
            if target<0:
                return
            if target==0:
                res.append(arr.copy())
                return
            
            for i in range(ind,len(candidates)):
                if candidates[i] > target:
                    break
                if i>ind and candidates[i]==candidates[i-1]:
                    continue
                arr.append(candidates[i])
                helper(i+1,arr,target-candidates[i])
                arr.pop()
        helper(0,[],target)
        return res
