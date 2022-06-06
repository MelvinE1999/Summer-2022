# fractional Knapsack

# inputs:
# w = array of weights
# v = array of values
# c = capacity
# n = # of items

# output:
# taken value
def fractionalKnapsack(w,v,c,n): 
    load = 0 # holds taken weight 
    takenVal = 0.0
    valuePerWeight = [0.0] * n
    for i in range(n): # theta (n)
        if w[i] == 0:
            valuePerWeight[i] = v[i]
            continue
        valuePerWeight[i] = v[i] / w[i]

    # sorts all arrays by v / w in decreasing order
    valuePerWeight, weights, values = list(zip(*reversed(sorted(zip(valuePerWeight,w,v)))))

    # gaurdian for potential negative and 0 cap cases
    if load >= c:
        return takenVal

    for i in range(n):
        if weights[i] <= (c - load): # item completely fits
            load += weights[i]
            takenVal += values[i]
        else: # taking a fraction of the item
            takenVal += (valuePerWeight[i] * (c - load))
            load = c
            break
        
    return takenVal

def main():
    weights = [5,5,5,5]
    vals = [20,40,30,10]
    answer = fractionalKnapsack(weights,vals, 10, 4)
    assert answer == 70.0
    assert fractionalKnapsack([0,0,2], [0,1,2], 2, 3) == 3.0

if __name__ == "__main__":
    main()