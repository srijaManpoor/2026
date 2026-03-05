#leetcode:560
#subarray_sum_equals_k
def subarraySum(nums,k):
    n=len(nums)
    d={0:1}
    count=0
    Sum=0
    for i in range(0,n):
        Sum+=nums[i]
        if (Sum-k in d):
            count+=d[Sum-k]
        if(Sum in d):
            d[Sum]+=1
        else:
            d[Sum]=1
    return count
nums=list(map(int,input().split()))
k=int(input())
print(subarraySum(nums,k))
