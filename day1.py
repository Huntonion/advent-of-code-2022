#part1
with open("inputs/day1.txt") as file:
    sum,max = 0,0
    for line in file:
        if(line != '\n'):
            sum = sum + int(line)
            if sum > max:
                max = sum
        else:
            sum = 0
    print(max)

#part2

with open("inputs/day1.txt") as file:
    sum, max = 0,0 
    maxQueue = [0,0,0] 
    for line in file:  
        if(line != '\n'): 
            sum = sum + int(line) 
        else:                              
            if sum > min(maxQueue):
                    maxQueue[maxQueue.index(min(maxQueue))] = sum
                    print(maxQueue)
            sum = 0
    total = 0
    for el in maxQueue:
        total = total + el     
    print(total)