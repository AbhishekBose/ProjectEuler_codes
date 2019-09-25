"""
Solution to project euler question number 53
"""
MAX_N = 100
MAX_VALUE = 10**6

def factorial(n):
    if n==0:
        return 1
    if n ==1:
        return 1
    else:
        return n*factorial(n-1)


def Ncr(n,r):
    ncr = factorial(n)/float((factorial(r)*factorial(n-r)))
    return ncr
if __name__ == "__main__":
    print(factorial(1))
    print(MAX_VALUE)
    count=0
    try:
        for n in range(2,MAX_N+1):
            for r in range(1,n+1):
                ncr = Ncr(n,r)
                if ncr > MAX_VALUE:
                    count+=1
    except Exception as e:
        print(str(e))
        print('n is:: ',n)
        print('r is::', r )
    print(count)

