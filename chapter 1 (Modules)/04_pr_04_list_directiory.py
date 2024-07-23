''' Q - Write a python program to print the contents of a directiory 
using os module .Search online for the function which does that

'''
import os
print(os.listdir())

# def minimum_time_to_solve(N, time, search, K):
#     dp=[float('inf')] * N
#     dp[N-1]=time[N-1]
# for i in range(N-2, -1 , -1):
#     dp[i]= time[i]+dp[i+1]
    
#     for j in range(i+1,min(i+k+1,N)):
#         dp[i]= min(dp[i],search[i] + dp[j])
        
#          return dp[0]
               
        
N=4
time=[3,1,8,7]
search = [4,4,6,2]
k=2
print(minimum_time_to_solve(N, time, search, K))