#%%
import numpy as np
import math
#%%
expr = lambda a,n: (((a+1)**n) + ((a-1)**n)) % a**2
# %%
def return_all_primes(N):
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
    return final_array

#%%
all_primes = return_all_primes(100000000)

#%%
for n in range(0,len(all_primes)):
    if n+1== len(all_primes):
        print(n)
        break
    else:
        rem = expr(all_primes[n],n+1)
        if rem > 10**10:
            print('Max rem is:::',rem)
            print('Ma value of N is::',n)
            break
    
# %%
del(all_primes)