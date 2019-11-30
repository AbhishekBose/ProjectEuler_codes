def catalan(n):
    if n<=1:
        return 1
    else:
        res = 0
        for i in range(n):
            res += catalan(i)*catalan(n-i-1)
        return res

if __name__ == "__main__":
    print(catalan(3))