
#https://leetcode.com/problems/combination-sum/

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]

        def helper(ind,arr,target):
            if target<0:
                return
            if target==0:
                res.append(arr[:])
                return

            for i in range(ind,len(candidates)):
                arr.append(candidates[i])
                helper(i,arr,target-candidates[i])  #i here, not i+1 because we can consider a no. unlimitd times..not just once
                arr.pop()
        helper(0,[],target)
        return res

