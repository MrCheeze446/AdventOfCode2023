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
    twoDigitsList = []

    for inputString in inputList:
        length = len(inputString)-1
        digits = ['a'] * length
        for (key, value) in lettersToInt.items():
            if key in inputString:
                digitIndex = inputString.find(key)
                digits[digitIndex] = value
        for letter in inputString:
            if letter.isnumeric():
                digitIndex = inputString.find(letter)
                digits[digitIndex] = letter

        if len(digits) == 1:
            twoDigits = digits[0] + digits[0]
        else:
            twoDigits = digits[0] + digits[len(digits) - 1]

        twoDigitsList.append(int(twoDigits))
        digits.clear()

    answer = 0
    for number in twoDigitsList:
        answer += number

    print(answer)
