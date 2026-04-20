#leetcode:3
#Q:longest substring without repeating characters
#s=list(map(str,input().split()))
    def lengthoflongestsubarray(s):
        n=len(s)
        d={}  #S.C: O(N)
        maxLen=0
        left=0
        right=0
        while(right<n):  #T.C: O(N)
            if(s[right] in d and d[s[right]]>=left): #shrink
                left=d[s[right]]+1
            d[s[right]]=right
            maxLen=max(maxLen,right-left+1)
            right+=1
        return maxLen
    print(lengthoflongestsubarray)
