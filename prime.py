"""
Solution to project euler question number 60
"""

## prime number is being calculated using sieve of Eratosthenes
import math
from random import randrange

#%%
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
#Assuming upper limit to be 1000, generate all primes from 2 to 1000
primes = return_all_primes(10000)
#%%
def check_is_prime(n):
    count=0
    for i in range(1,n+1):
        if n%i==0:
            count+=1
        if count>2:
            return False
    return True
#%%
#Rabin miller test for prime
def probably_prime(n,k=3):
    if n < 2: return False
    for p in primes:
        if n < p * p: return True
        if n % p == 0: return False
    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s //= 2
    for _ in range(k):
        a = randrange(2, n - 1)
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

#%%
def check_if_comb_prime(n1,n2):
    comb1 = int(str(n1)+str(n2))
    comb2 = int(str(n2)+str(n1))
    if probably_prime(comb1) and probably_prime(comb2):
        return True
    else:
        return False
        





#%%
#iterate through list for every possible combination. Naive solution
def get_prime_sum():
    for i in range(0,len(primes)):
        w=primes[i]
        for j in range(i+1,len(primes)):
            x = primes[j] 
            # if x < w:
            #     continue
            if check_if_comb_prime(w,x):
                for k in range(j+1,len(primes)):
                    y = primes[k]
                    # if y<x:
                    #     continue
                    if check_if_comb_prime(w,y) and check_if_comb_prime(x,y):
                        for l in range(k+1,len(primes)):
                            z = primes[l]
                        # if z<y:
                        #     continue
                            if check_if_comb_prime(w,z) and check_if_comb_prime(x,z) and check_if_comb_prime(y,z):
                                for m in range(0,len(primes)):
                                    a = primes[m]
                            # if a<z:
                            #     continue
                                    if check_if_comb_prime(w,a) and check_if_comb_prime(x,a) and check_if_comb_prime(y,a) and check_if_comb_prime(z,a):
                                        return w+x+y+z+a

#%%
print(get_prime_sum())

#%%
