"""
Solution to project euler question number 60
"""

## prime number is being calculated using sieve of Eratosthenes
import math
#%%
N=30
A={}
for i in range(N):
    if i <2:
        A[i] = False
    else:
        A[i] = True
upper_limit = int(math.sqrt(N))
for j in range(2,upper_limit):
    if A[j]:
        for k in range(j*j,N,j):
            A[k] = False

final_array = [num for num in list(A.keys()) if A[num]]
print(final_array)
#%%
