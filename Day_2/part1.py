import re

if __name__ == '__main__':
    with open("input", "r") as fileInput:
        inputStrings = fileInput.read()

    totalRed = 12
    totalGreen = 13
    totalBlue = 14
    gameSums = 0

    inputStrings = inputStrings.splitlines()

    for line in inputStrings:
        ids = line.split(':')[0]
        gameID = int(re.findall(r'\d+', line)[0])
        rounds = line.split(';')
        invalid = False
        for currentRound in rounds:
            colors = [0] * 3

            foundRed = re.search('\d+ red', currentRound)
            foundGreen = re.search('\d+ green', currentRound)
            foundBlue = re.search('\d+ blue', currentRound)

            if foundRed:
                match = re.findall('\d+ red', currentRound)[0]
                red = int(re.findall('\d+', match)[0])
                colors[0] = red
            if foundGreen:
                match = re.findall('\d+ green', currentRound)[0]
                green = int(re.findall('\d+', match)[0])
                colors[1] = green
            if foundBlue:
                match = re.findall('\d+ blue', currentRound)[0]
                blue = int(re.findall('\d+', match)[0])
                colors[2] = blue

            if colors[0] > totalRed or colors[1] > totalGreen or colors[2] > totalBlue:
                invalid = True
                break

        if not invalid:
            print(gameID)
            gameSums += gameID

    print(gameSums)