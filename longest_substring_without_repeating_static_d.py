#leetcode:3
#longest length of substring without repeating
#static dict length
def lengthOfLongestSubarray(S):
    n=len(S)
    d=[-1]*256  #S.C: O(1)
    maxLen=0
    left=0
    right=0
    while(right<n):   #T.C: O(N)
        if(d[ord(S[right])]!=-1 and d[ord(S[right])]>=left):
            left=d[ord(S[right])]+1
        d[ord(S[right])]=right
        maxLen=max(maxLen,right-left+1)
        right+=1
    return maxLen
S=input("enter string:")
print(lengthOfLongestSubarray(S))
