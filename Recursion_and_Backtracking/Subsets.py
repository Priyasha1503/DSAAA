
#https://leetcode.com/problems/subsets/


'''Since they have given should not contain duplicates and can return in any order - we can use combinations rather than permutations.'''

#Way 1 - PICK & NOT-PICK

'''class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        def helper(ind,arr):

            if ind==len(nums):
                res.append(arr[:])
                return
            #pick
            arr.append(nums[ind])
            helper(ind+1,arr)
            arr.pop()
            #not pick
            helper(ind+1,arr)

            return arr
        
        helper(0,[])
        return res'''

##WAY2 - USING FOR LOOP

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        def helper(ind,arr):
            res.append(arr[:])
            for i in range(ind,len(nums)):
                arr.append(nums[i])
                helper(i+1,arr) # IF WE GIVE i ITSELF HERE RATHER THAN i+1,THEN WE WILL HAVE THE URR ITH IND NUMBER REPEATED ..WHICH MEANS IT WILL BECOME LIKE HOW WE USE FOR COMBINATION SUM PROB - WHERE WE CAN USE THAT NUMBER ANY NO. OF TIMES
                arr.pop()
        
        helper(0,[])
        return res
