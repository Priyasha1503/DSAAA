
#https://leetcode.com/problems/contiguous-array/


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        '''maxlen=0
        for i in range(0,len(nums)):
            zero_cnt=0
            one_cnt=0
            for j in range(i,len(nums)):
                if nums[j]==0:
                    zero_cnt+=1
                else:
                    one_cnt+=1
                if zero_cnt==one_cnt:
                    maxlen = max(maxlen,j-i+1)
        return maxlen'''


        #Better appraoch1 using prefisum+hashmap
        '''#we can wither change like this all 0->-1 or do the other stated mehtod
        for i in range(0,len(nums)):
            if nums[i]==0:
                nums[i]=-1
        mpp=dict()
        mpp[0] = -1
        psum=0
        k=0
        maxlen=0
        for i in range(0,len(nums)):
            psum+=nums[i]
            remaining = psum - k
            if remaining in mpp:
                maxlen = max(maxlen,i-mpp[remaining])
            #storing psum in mpp
  
                #we are using else condn to store here because if we didnt use else and direclty store, eveytime a new one which might already be present in the mpp will also get directly updated..and oncethat gets udpated..thyen the length will be shprt for us to calculate..because i value which we will be storing in val of mpp-->that will be bigger one comapred to befpre one which we have replaced--so, that gives us shprtest length..butwe need maxlength..so, we need to put else condn -->whcih makes sure that if there is no element in the mpp then itself it will add..else it doesnt touch it if there is already element present.
            if psum not in mpp:
                mpp[psum] = i

        
        return maxlen'''

        #more better approach using prefix sum + hashmap
        mpp=dict()
        mpp[0]=-1 #here,the meaning of this is still we didnt start the itreation like we are before 0th ind i.e ,-1..and the sum currently we have till now is 0.so, o -sum is key : -1 is ind i.e, value
        maxlen=0
        psum=0 #which is the running sum/the sum till the curr index
        for i in range(0,len(nums)):
            if nums[i]==0:
                psum=psum-1 #adding -1
            else:
                psum=psum+1
            remaining =psum-0 #wheere k=0 here
            if remaining in mpp:
                start=mpp[remaining]+1
                maxlen = max(maxlen,i-start+1)
            '''If prefix sum seen before:
    length = current_index − first_occurrence
            Else:
                store first occurrence'''
                
            if psum not in mpp:
                mpp[psum] = i #meaning - the currsum it have seen till that ind till i ..it stored
        return maxlen
