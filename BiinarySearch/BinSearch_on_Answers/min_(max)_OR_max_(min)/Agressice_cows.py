

#https://www.geeksforgeeks.org/problems/allocate-minimum-number-of-pages0937/1

class Solution:
    def findPages(self, arr, k):
        # code here
        
        def func(mid,nums): #mid value is the our target sum here
            sums=0 #25
            max_pages=0
            student_cnt=0
            for i in range(0,len(nums)): #0#1
                sums+=nums[i]
                if sums>mid:
                    max_pages=max(max_pages,sums-nums[i])
                    student_cnt+=1
                    sums=nums[i]
            if sums<mid:
                max_pages=max(max_pages,sums-nums[i])
                student_cnt+=1
                    
                
            return [student_cnt,max_pages]
            
        
        low=max(arr)
        high=sum(arr)
        min_of_all=float('inf')
        while low<=high:
            mid=(low+high)//2                                                                              
            stud_cnt,pages=func(mid,arr)
            if stud_cnt<=k:
                min_of_all = min(min_of_all,pages)
                high=mid-1
            else:
                low=mid+1
        return min_of_all
            
        
        
        
        
        
        
        
        
        
