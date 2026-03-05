def TwoSum(nums,target):
    n=len(nums)
    for i in range(0,n):
        for j in range(i+1,n):
            if(nums[i]+nums[j]==target):
                return [i,j]
nums=list(map(int,input("enter list:").split()))
target=int(input("enter target:"))
print(TwoSum(nums,target))
