# inputs:
# start = an array of start times
# finish = an array of finish times
# n = number of activities

# outputs:
# a list of selected activites
def greedyActSelection(start,finish,n):
    act_num = [i for i in range(1, n + 1)]
    ctr = 0
    solution = []

    # sort by finish time in ascending
    finish,start,act_num = zip(*sorted(zip(finish,start,act_num)))

    solution.append(act_num[0])
    for i in range(1,n):
        if start[i] >= finish[ctr]:
            solution.append(act_num[i])
            k = i
    
    return solution

def main():
    print(greedyActSelection([1,4,2,6],[4,8,5,7],4))

if __name__ == "__main__":
    main()