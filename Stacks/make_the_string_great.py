
#https://leetcode.com/problems/make-the-string-great/?envType=problem-list-v2&envId=stack

'''class Solution:
    def makeGood(self, s: str) -> str:
        stack=[]
        for i in range(0,len(s)):
            if stack!=[] and abs(ord(stack[-1]) - ord(s[i]))==32:
                #stack[-1].upper()==s[i] or stack[-1].lower()==s[i]:
                '''in the above condn we cannot gve this condn because s[i] might be smaller or
                vice versa...and taking both in or codnn as abve is resulting in the both ower case letters to also take part,in reality they dont have to get removed.So, using ord() gives us the ascii value of the char and dng minus gives us the difference 
                in doing this, for the lower case and uppercase of same har the diff will be 32. '''
                stack.pop()
            else:
                stack.append(s[i])
        stack
        return "".join(stack)
'''


###JAVA
'''
class Solution {
    public String makeGood(String s) {
        Stack <Character> stack = new Stack<>();
        for(char c:s.toCharArray()){
            if(!stack.isEmpty() && Math.abs(stack.peek()-c) == 32){
                stack.pop();
            }
            else{
                stack.push(c);
            }
        }
        StringBuilder result = new StringBuilder();
        for(char c:stack){
            result.append(c);
        }
        System.out.println(result);
        
        return result.toString();
        }
    }
    '''
