#%%
def get_max(gold,m,n):
    # col = 0
    gold_table = [[0 for i in range(0,m)] for j in range(n)]
    for col in range(0,n):
        for row in range(0,m):
            if col == n-1:
                right,right_down,right_top = 0,0,0
            else:
                right = gold[row][col+1]
            if (row == 0 or col== n-1):
                right_top = 0
            else:
                right_top = gold[row-1][col+1]
            if (row == m-1 or col==n-1):
                right_down = 0
            else:
                right_down = gold[row+1][col+1]  
            gold_table[row][col] = gold[row][col] + max(right_top,right,right_down)

            
    return gold_table
        

#%%

def get_max2(gold,m,n):
    goldTable = [[0 for i in range(n)] 
                            for j in range(m)] 
    
    for col in range(n-1, -1, -1): 
        for row in range(m): 

            # Gold collected on going to 
            # the cell on the rigth(->) 
            if (col == n-1): 
                right = 0
            else: 
                right = goldTable[row][col+1] 

            # Gold collected on going to 
            # the cell to right up (/) 
            if (row == 0 or col == n-1): 
                right_up = 0
            else: 
                right_up = goldTable[row-1][col+1] 

            # Gold collected on going to 
            # the cell to right down (\) 
            if (row == m-1 or col == n-1): 
                right_down = 0
            else: 
                right_down = goldTable[row+1][col+1] 

            # Max gold collected from taking 
            # either of the above 3 paths 
            goldTable[row][col] = gold[row][col] + max(right, right_up, right_down) 
    # return goldTable

    res = 0
    for i in range(m):
        res = max(res ,goldTable[i][0])
    return res

#%%
if __name__ == "__main__":
    gold =[[0,3,3],[2,-1,4],[0,6,4]]
    # gold = [[1, 3, 1, 5], 
    # [2, 2, 4, 1], 
    # [5, 0, 2, 3], 
    # [0, 6, 1, 2]] 
    m=3
    n=3
    print(get_max2(gold,m,n))


#%%
