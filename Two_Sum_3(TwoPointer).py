nums=list(map(int,input().split()))
target=int(input())
nums.sort()
def TwoSum(nums,target):
    n=len(nums)
    left=0
    right=n-1
    while(left<right):
        Sum=nums[left]+nums[right]
        if(Sum==target):
            return([left,right])
        elif(Sum>target):
            right-=1
        elif(Sum<target):
            left+=1
print(TwoSum(nums,target))
