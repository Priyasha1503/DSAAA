

#printing n to 1 -- i-1 approach
n=int(input())
def rec(ind,n):
  if ind<1:
    return 
  print(ind)
  rec(ind-1,n)


#priinting n to 1 -- uisng i+1 appraoch -- reverse..
n=int(input())
def rec(ind,n):
  if ind>n:
    return
  rec(ind+1,n) #we are ot returning func rec() here..we are jus calling, if we are returning then we cannot write print down f t..because it doesn't execute,it directly returns.
  print(ind)   #so, this print function executes when the fnction is called and as well returned --so, it i backtracking way
