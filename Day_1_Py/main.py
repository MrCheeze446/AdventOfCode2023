
def cleanDigits(digitArray: []):
    cleanedDigits = []
    for digit in digitArray:
        if digit.isnumeric():
            cleanedDigits.append(digit)

    return cleanedDigits

def getIndexes(inputArray, desiredElement):
    return [index for index, element in enumerate(inputArray) if element == desiredElement]


def checkIfSeen(givenLetter):
    if givenLetter in timesSeen:
        index = timesSeen.get(givenLetter)
        digitIndex = getIndexes(inputString, givenLetter)[index]
        timesSeen[givenLetter] += 1
    else:
        timesSeen.update({givenLetter: 1})
        digitIndex = inputString.find(givenLetter)

    return digitIndex


if __name__ == '__main__':
    with open("input", "r") as fileInput:
        inputStrings = fileInput.read()

    inputList = inputStrings.splitlines()

    lettersToInt = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }

    timesSeen = {}
    twoDigitsList = []

    for inputString in inputList:
        length = len(inputString)
        digits = ['a'] * length
        for (key, value) in lettersToInt.items():
            if key in inputString:
                digitIndex = inputString.find(key)
                digits[digitIndex] = value
        for letter in inputString:
            if letter.isnumeric():
                digitIndex = checkIfSeen(letter)
                digits[digitIndex] = letter

        digits = cleanDigits(digits)
        if len(digits) == 1:
            twoDigits = digits[0] + digits[0]
        else:
            twoDigits = digits[0] + digits[len(digits) - 1]

        twoDigitsList.append(int(twoDigits))
        timesSeen.clear()
        digits.clear()

    answer = 0
    for number in twoDigitsList:
        answer += number

    print(answer)

