

#https://leetcode.com/problems/combinations/

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        res=[]
        def helper(ind,arr):
            if ind==n+1:
                if len(arr)==k:
                    res.append(arr[:])
                return
            arr.append(ind)
            helper(ind+1,arr)
            arr.pop()
            helper(ind+1,arr)
        
        helper(1,[])
        return res
