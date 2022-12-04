with open("inputs/day4.txt") as file:
    counter = 0
    for line in file:
        string = line.rstrip().replace('-',',').split(',')
        numbers = [int(i) for i in string]
        if(numbers[0]>=numbers[2] and numbers[1] <= numbers[3]) or (numbers[0]<=numbers[2] and numbers[1] >= numbers[3]):
            counter+=1
    print(counter)
   
with open("inputs/day4.txt") as file:
    counter = 0
    for line in file:
        string = line.rstrip().replace('-',',').split(',')
        numbers = [int(i) for i in string]
        if(numbers[0] <= numbers[2] and numbers[1]>= numbers[2]) or (numbers[0] >= numbers[2] and numbers[0]<= numbers[3]) or (numbers[0]>=numbers[2] and numbers[1] <= numbers[3]) or (numbers[0]<=numbers[2] and numbers[1] >= numbers[3]):
            counter+=1
    print(counter)