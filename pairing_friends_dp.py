import sys

def pair_friends(n):
    pf = [0]*(n+1)
    pf[0] = 0
    pf[1] = 1
    pf[2] = 2
    for i in range(3,n+1):
        pf[i] = pf[i-1] + (i-1)*pf[i-2]
    return pf[n]

if __name__ == "__main__":
    # print(pair_friends(int(sys.argv[1])))
    print(pair_friends(4))