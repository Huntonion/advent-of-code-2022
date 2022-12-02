#first elf                Second elf
#ROCK PAPER SCISSORS | ROCK PAPER SCISSORS
# A    B       C     | X     Y      Z
with open("inputs/day2.txt") as file:
    rockScore, paperScore, scissorsScore = 1,2,3
    totalScore = 0
    lost,draw, won = 0, 3, 6
    for line in file:
        firstElfChoice, secondElfChoice = line.rstrip()[0], line.rstrip()[2]
        if(firstElfChoice == 'A' and secondElfChoice == 'X'):
            print(firstElfChoice + "-" + secondElfChoice +"score:draw" + str(draw)+ "played:rock" + str(rockScore)  )
            totalScore += draw + rockScore
            print("total:"+str(totalScore))
        elif(firstElfChoice == 'B' and secondElfChoice == 'X'):
            print(firstElfChoice + "-" + secondElfChoice +"score:lost" + str(lost)+ "played:rock" + str(rockScore))
            totalScore += lost + rockScore
            print("total:"+str(totalScore))
        elif(firstElfChoice == 'C' and secondElfChoice == 'X'):
            print(firstElfChoice + "-" + secondElfChoice +"score:won" + str(won)+ "played:rock" + str(rockScore))
            totalScore += won + rockScore
            print("total:"+str(totalScore))
        elif(firstElfChoice =='A' and secondElfChoice == 'Y'):
            print(firstElfChoice + "-" + secondElfChoice +"score:won" + str(won)+ "played:paper" + str(paperScore))
            totalScore += won + paperScore
            print("total:"+str(totalScore))
        elif(firstElfChoice =='B' and secondElfChoice == 'Y'):
            print(firstElfChoice + "-" + secondElfChoice +"score:draw" + str(draw)+ "played:paper" + str(paperScore))
            totalScore += draw + paperScore
            print("total:"+str(totalScore))
        elif(firstElfChoice =='C' and secondElfChoice == 'Y'):
            print(firstElfChoice + "-" + secondElfChoice +"score:lost" + str(lost)+ "played:paper" + str(paperScore))
            totalScore += lost + paperScore
            print("total:"+str(totalScore))
        elif(firstElfChoice =='A' and secondElfChoice == 'Z'):
            print(firstElfChoice + "-" + secondElfChoice +"score:lost" + str(lost)+ "played:scissors" + str(scissorsScore))
            totalScore += lost + scissorsScore
            print("total:"+str(totalScore))
        elif(firstElfChoice =='B' and secondElfChoice == 'Z'):
            print(firstElfChoice + "-" + secondElfChoice +"score:won" + str(won)+ "played:scissors" + str(scissorsScore))
            totalScore += won + scissorsScore
            print("total:"+str(totalScore))
        elif(firstElfChoice =='C' and secondElfChoice == 'Z'):
            print(firstElfChoice + "-" + secondElfChoice +"score:draw" + str(draw)+ "played:scissors" + str(scissorsScore))
            totalScore += draw + scissorsScore
            print("total:"+str(totalScore))
    print(totalScore)