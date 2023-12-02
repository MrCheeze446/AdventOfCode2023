import re

if __name__ == '__main__':
    with open("input", "r") as fileInput:
        inputStrings = fileInput.read()

    gameSums = 0

    inputStrings = inputStrings.splitlines()

    for line in inputStrings:
        ids = line.split(':')[0]
        gameID = int(re.findall(r'\d+', line)[0])
        rounds = line.split(';')
        biggestRed = 0
        biggestGreen = 0
        biggestBlue = 0
        for currentRound in rounds:
            colors = [0] * 3

            foundRed = re.search('\d+ red', currentRound)
            foundGreen = re.search('\d+ green', currentRound)
            foundBlue = re.search('\d+ blue', currentRound)

            if foundRed:
                match = re.findall('\d+ red', currentRound)[0]
                red = int(re.findall('\d+', match)[0])
                colors[0] = red
                if red > biggestRed:
                    biggestRed = re
            if foundGreen:
                match = re.findall('\d+ green', currentRound)[0]
                green = int(re.findall('\d+', match)[0])
                colors[1] = green
                if green > biggestGreen:
                    biggestGreen = green
            if foundBlue:
                match = re.findall('\d+ blue', currentRound)[0]
                blue = int(re.findall('\d+', match)[0])
                colors[2] = blue
                if blue > biggestBlue:
                    biggestBlue = blue

        gameSums += biggestRed * biggestBlue * biggestGreen


    print(gameSums)