import re

if __name__ == '__main__':
    with open("input", "r") as fileInput:
        inputStrings = fileInput.read()

    red = 12
    green = 13
    blue = 14
    gameSums = 0

    inputList = inputStrings.splitlines()
    goodGames = []

    for i in range(0, len(inputList)-1):
        gameID = re.findall(r'\d+', inputList[i])[0]
        game = inputList[i]
        game = game[game.find(':'):]
        game = game.replace(' ', '')
        game = game.replace(':', '')
        gameValues = game.split(";")

        for valueSet in gameValues:
            values = valueSet.split(',')
            invalid = False
            for value in values:
                if invalid: break
                num = re.findall(r'\d+', value)
                if "green" in value and int(num[0]) >= green:
                    invalid = True
                elif "blue" in value and int(num[0]) >= blue:
                    invalid = True
                elif "red" in value and int(num[0]) >= red:
                    invalid = True
            if not invalid:
                goodGames.append(int(gameID))


    for value in goodGames:
        gameSums += value

    print(gameSums)