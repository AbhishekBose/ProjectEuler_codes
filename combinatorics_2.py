MAX_N = 100
MAX_VALUE = 10**6

#%%


# def factorial(n):
#     if n==0:
#         val = 1
#     if n ==1:
#         val = 1
#     else:
#         val= n*factorial(n-1)
#     if n not in fact_list.keys():
#         fact_list[n]=val
#     print(val)
#     return val
def factorial(val):
    fact_list=[]
    fact_list.append(1)
    for i in range(1,val+1):
        # print(i)
        fact_list.append(i*fact_list[i-1])
    
    return fact_list[val]

#%%

def Ncr(n,r):
    ncr = factorial(n)/float((factorial(r)*factorial(n-r)))
    return ncr

if __name__ == "__main__":
    print(factorial(1))
    print(MAX_VALUE)
    count=0
    try:
        for n in range(2,MAX_N+1):
            for r in range(2,n+1):
                ncr = Ncr(n,r)
                if ncr > MAX_VALUE:
                    count+=1
    except Exception as e:
        print(str(e))
        print('n is:: ',n)
        print('r is::', r )
    print(count)

