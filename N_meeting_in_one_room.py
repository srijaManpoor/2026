#geeksforgeeks
#N meetings in one room
def MaximumMeetings(start,end):
    mat=[]
    n=len(start)
    for i in range(0,n):
        mat.append([start[i],end[i]])
    mat.sort(key=lambda x:x[1])   #sort timing intervals according to endtime
    cnt=1  #coz endtime in 1st column
    endTime=mat[0][1]  #storing end time
    for row in range(1,n):
        if(mat[row][0]>endTime):  #comparing starting with previous end time
            cnt+=1
            endTime=mat[row][1]
    return cnt
start=list(map(int,input().split()))
end=list(map(int,input().split()))
print(MaximumMeetings(start,end))
