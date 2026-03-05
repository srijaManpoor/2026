def TwoSum(nums,target):
    n=len(nums)
    d={}
    for i in range(0,n):
        a=nums[i]
        b=target-a
        if(b in d):
            return [i,d[b]]
        d[a]=i
nums=list(map(int,input().split()))
target=int(input())
print(TwoSum(nums,target))
