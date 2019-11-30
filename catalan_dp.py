def catalan(n):
    if n==0:
        return 1
    elif n==1:
        return 1
    else:
        catalan_array = [0]*(n+1)
        catalan_array[0] = 1
        catalan_array[1] = 1
        for i in range(2,n+1):
            catalan_array[i] = 0
            for j in range(0,i):
                catalan_array[i] = catalan_array[i]+(catalan_array[j]*catalan_array[i-j-1])
        return catalan_array[n]
       

if __name__ == "__main__":
    print(catalan(30))