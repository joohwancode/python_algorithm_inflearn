import sys

sys.stdin = open("DP/input.txt", "rt")

n=int(input())
arr=list(map(int,input().split()))
arr.insert(0,0)
dy=[0]*(n+1)
dy[1]=1
res=0
for i in range(2,n+1):
    max=0
    for j in range(i-1,0,-1): ## 감소하면서 앞으로 전진하다. 1까지라 0까지 돈다. 
        if arr[j]<arr[i] and dy[j]>max:
            max=dy[j]
    dy[i]=max+1 ##dy[j]에 하나씩 달라붙는것이기 때문에 이렇게 +1을 해준다. 
    if dy[i]>res:
        res=dy[i]
print(res)



# x = int(input())

# arr = list(map(int, input().split()))

# dp = [1 for i in range(x)]

# for i in range(x):
#     for j in range(i):
#         if arr[i] > arr[j]:
#             dp[i] = max(dp[i], dp[j]+1)

# print(max(dp))