# import sys

# sys.stdin = open("DP/input.txt", "rt")

# def DFS(x,y):
#     if dy[x][y]>0:
#         return dy[x][y]
#     if x==0 and y==0:
#         return arr[0][0]
#     else:
#         if y==0:
#             dy[x][y]=DFS(x-1,y)+arr[x][y]
#         elif x==0:
#             dy[x][y]=DFS(x,y-1)+arr[x][y]
#         else:
#             dy[x][y]=min(DFS(x-1,y),DFS(x,y-1))+arr[x][y]
#         return dy[x][y]
#     ###메모이제이션 해야한다는 것을 주의해라 ! 
# if __name__=="__main__":
#     n=int(input())
#     arr=[list(map(int,input().split())) for _ in range(n)]
#     dy=[[0]*n for _ in range(n)]
#     print(DFS(n-1,n-1))
