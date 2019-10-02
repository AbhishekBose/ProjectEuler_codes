def pair_friends(n):
    if n==1:
        return 1
    elif n==2:
        return 2
    else:
        return pair_friends(n-1) + pair_friends(n-2)*(n-1)

if __name__ == "__main__":
    print(pair_friends(4))