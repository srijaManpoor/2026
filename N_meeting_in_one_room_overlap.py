def eraseOverLapInterval(intervals):
    intervals.sort(key=lambda x:x[1])
    cnt=1
    endTime=intervals[0][1]
    n=len(intervals)
    for row in range(1,n):
        if(intervals[row][0]>=endTime):
            cnt+=1
            end=intervals[row][1]
    return n-cnt
intervals=[[1,2],[2,3],[3,4],[1,3]]
print(eraseOverLapInterval(intervals))
