#%%
import numpy as np
import math

#%%
expr = lambda a,n: (((a+1)**n) + ((a-1)**n)) % a**2
# rem = lambda x,y: x%(y**2)
# %%

all_a = [i for i in range(3,1001)]
all_n = [i for i in range(1,1500,2)]
# %%
all_r=[]
for a in all_a:
    max_rem=0
    for n in all_n:
        rem = expr(a,n)
        if rem > max_rem:
            max_rem = rem
    if a==7:
        print(max_rem)
    all_r.append(max_rem)

# %%
sum_r_max = np.sum(all_r)
print(sum_r_max)
del(sum_r_max)
del(all_a)
del(all_n)
del(all_r)
# %%
