#leetcode 424
#longest repeating character replacement
def LongestRepeatingCharacter(s,k):
    n=len(s)
    d={}
    left=0
    right=0
    maxLen=0
    maxF=0
    while(right<n):
        if(s[right] in d):
            d[s[right]]+=1
        else:
            d[s[right]]=1
        maxF=max(maxF,d[s[right]])
        while((right-left+1)-maxF>k):     #shrink
            d[s[left]]-=1
            if(d[s[left]]==0):
                del d[s[left]]       #eliminate from dict
            left+=1
        maxLen=max(maxLen,right-left+1)
        right+=1
    return maxLen
s=input("enter string:")
k=int(input("enter k :"))
print(LongestRepeatingCharacter(s,k))

    
