#first elf                Second elf
#ROCK PAPER SCISSORS | ROCK PAPER SCISSORS
# A    B       C     | X     Y      Z
#part1
with open("inputs/day2.txt") as file:
    rockScore, paperScore, scissorsScore = 1,2,3
    totalScore = 0
    lost,draw, won = 0, 3, 6
    for line in file:
        firstElfChoice, secondElfChoice = line.rstrip()[0], line.rstrip()[2]
        if(firstElfChoice == 'A' and secondElfChoice == 'X'):
            totalScore += draw + rockScore
        elif(firstElfChoice == 'B' and secondElfChoice == 'X'):
            totalScore += lost + rockScore
        elif(firstElfChoice == 'C' and secondElfChoice == 'X'):
            totalScore += won + rockScore
        elif(firstElfChoice =='A' and secondElfChoice == 'Y'):
            totalScore += won + paperScore
        elif(firstElfChoice =='B' and secondElfChoice == 'Y'):
            totalScore += draw + paperScore
        elif(firstElfChoice =='C' and secondElfChoice == 'Y'):
            totalScore += lost + paperScore
        elif(firstElfChoice =='A' and secondElfChoice == 'Z'):
            totalScore += lost + scissorsScore
        elif(firstElfChoice =='B' and secondElfChoice == 'Z'):
            totalScore += won + scissorsScore
        elif(firstElfChoice =='C' and secondElfChoice == 'Z'):
            totalScore += draw + scissorsScore
    print(totalScore)

#first elf                Second elf
#ROCK PAPER SCISSORS | ROCK PAPER SCISSORS
# A    B       C     |     it depends.
    #part2
with open("inputs/day2.txt") as file:
    rockScore, paperScore, scissorsScore = 1,2,3
    totalScore = 0
    lost,draw, won = 0, 3, 6
    for line in file:
        firstElfChoice, secondElfChoice = line.rstrip()[0], line.rstrip()[2]
        if(firstElfChoice == 'A' and secondElfChoice == 'X'):
            totalScore += lost + scissorsScore
        elif(firstElfChoice == 'B' and secondElfChoice == 'X'):
            totalScore += lost + rockScore
        elif(firstElfChoice == 'C' and secondElfChoice == 'X'):
            totalScore += lost + paperScore
        elif(firstElfChoice =='A' and secondElfChoice == 'Y'):
            totalScore += draw + rockScore
        elif(firstElfChoice =='B' and secondElfChoice == 'Y'):
            totalScore += draw + paperScore
        elif(firstElfChoice =='C' and secondElfChoice == 'Y'):
            totalScore += draw + scissorsScore
        elif(firstElfChoice =='A' and secondElfChoice == 'Z'):
            totalScore += won + paperScore
        elif(firstElfChoice =='B' and secondElfChoice == 'Z'):
            totalScore += won + scissorsScore
        elif(firstElfChoice =='C' and secondElfChoice == 'Z'):
            totalScore += won + rockScore
    print(totalScore)