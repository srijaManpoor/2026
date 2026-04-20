#leetcode 930
#binary subarray with sum(4th pattern)
def numSubarrayWithSum(nums,goal):
    def func(nums,goal):
        if(goal<0):
            return 0
        Sum=0
        count=0
        left=0
        right=0
        n=len(nums)
        while(right<n):
            Sum+=nums[right]
            while(Sum>goal):     #shrink
                Sum-=nums[left]
                left+=1
            count+=(right-left+1)
            right+=1
        return count
    return func(nums,goal)-func(nums,goal-1)
nums=list(map(int,input().split()))
goal=int(input())
print(numSubarrayWithSum(nums,goal))
