# 0-1 Knapsack
# dynamic programming
# inputs:
# w = array of weights
# v = array of values
# c = capacity
# n = # of items

# output:
# taken value
def knapsack(w,v,c,n):
    # temp[row][col]
    temp = [[0 for i in range(c + 1)] for j in range(n+1)]

    for i in range(1, n+1):
        for j in range(c+1):
            if w[i-1] > j:
                temp[i][j] = temp[i-1][j]
            else:
                temp[i][j] = max((v[i-1] + temp[i-1][j-w[i-1]]), temp[i-1][j])
    
    return temp[n-1][c]

def main():
    weights = [5,5,5,5]
    vals = [20,40,30,10]
    answer = knapsack(weights,vals, 10, 4)
    assert answer == 70.0

if __name__ == "__main__":
    main()