#longest subarray/substring where <condition>
#
arr=list(map(int,input().split()))
k=int(input("enter k:"))
Sum=0
maxLen=0
right=0
left=0
n=len(arr)
while(right<n):  #expand
    Sum+=arr[right]
    while(Sum>k):  #shrink
        Sum-=arr[left]
        left+=1
    maxLen=max(maxLen,right-left+1)
    right+=1
print(maxLen)
