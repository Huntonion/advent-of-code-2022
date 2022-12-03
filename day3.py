with open("inputs/day3.txt") as file:
    score = 0
    for line in file:
        firstHalf, secondHalf = line[0:len(line)//2],line[len(line)//2:]
        a=list(set(firstHalf)&set(secondHalf))
        if(a[0].isupper()):
            score+= ord(a[0])-38
        elif(a[0].islower()):
            score+= ord(a[0])-96
    print(score)

#part2
with open("inputs/day3.txt") as file:
    score = 0
    rucksacks = []
    rucksacksGroup = []
    i = 0
    for line in file:
        rucksacks.append(line.rstrip())
        i=i+1
        if(i == 3):
            i=0
            a=list(set(rucksacks[0])&set(rucksacks[1])&set(rucksacks[2]))
            rucksacks = []
            if(a[0].isupper()):
                score+= ord(a[0])-38
            elif(a[0].islower()):
                score+= ord(a[0])-96
    print(score)

        