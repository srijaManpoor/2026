#leetcode:51
#N queens(hard) using back tracking
'''
rules
1.each row should contain single queen
2.each column should contain single queen
3.the queens should not attack each other(8 possible ways to attack)
'''
def NQueens(n):
    def canWePlace(row,col,mat):
        #topLeft
        r,c=row,col
        while(r>=0 and c>=0):
            if(mat[r][c]=='Q'):
                return False
            r-=1
            c-=1
        #top
        r,c=row,col
        while(r>=0):
            if(mat[r][c]=='Q'):
                return False
            r-=1
        #topRight
        r,c=row,col
        while(r>=0 and c<n):
            if(mat[r][c]=='Q'):
                return False
            r-=1
            c+=1
        return True
    def backtrack(row,mat,ans,n):
        if(row==n):
            temp=[]
            for r in mat:
                temp.append(''.join(r))  #join is used for string conversion
            ans.append(temp)
            return
        for col in range(0,n):
            if(canWePlace(row,col,mat)): #it is a function call to execute 3 rules
                mat[row][col]='Q'
                backtrack(row+1,mat,ans,n)
                mat[row][col]="."
    mat=[]
    for i in range(0,n):
        list=['.']*n      #['.'] empty space is created
        mat.append(list)
    row=0
    ans=[]
    backtrack(row,mat,ans,n)
    return ans
n=int(input("enter n value:"))
print(NQueens(n))
