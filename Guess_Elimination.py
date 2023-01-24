
from numpy import linalg,zeros


         #----Direct Input-----
'''co=np.array([ 
    [2,3,4,1],
    [5,6,3,2],
    [7,8,6,5],
    [4,7,4,3],
],float)'''

'''b=np.array([4,3,7,6],float)

n=len(b)'''

                  #----Direct Input end-----


             #-------user input--------

co=[]
b=[]
print("Num of row: ")
row=int(input())
print("Num of col: ")
col=int(input())



for i in range(row):
    arr=[]
    for j in range(col):
        print("A[",i,"][",j,"] :")
        n=float(input())
        arr.append(n)
    co.append(arr)



for i in range(1):
    for j in range(row):
        print("B[",i,"][",j,"] :")
        m=float(input())
        b.append(m)
n=len(b)

print(linalg.solve(co, b))
                 #-------user input end--------
        
for k in range(n-1):
    for i in range(k+1, n):
        ratio=co[i][k]/co[k][k]
        for j in range(k, n):
            co[i][j] = co[i][j] - ratio*co[k][j]
        b[i] = b[i]- ratio*b[k]

'''print(co)
print("  ")
print(b)'''

x=zeros(n,float)
x[n-1]=b[n-1]/co[n-1][n-1]

for i in range(n-2,-1,-1):
    sum_j=0
    for j in range(i+1,n):
        sum_j+=co[i][j]*x[j]
    x[i]=(b[i]-sum_j)/co[i][i]


print("     ")
print(co)
print(x)

