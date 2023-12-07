def main() -> int:

    f = open('puzzle-1-codes.txt', 'r')
    data = f.readlines()

    returnValue = 0
    digitString = ""

    for row in data:
        for letter in row:
            if letter.isdigit():
                digitString += letter
                break
        for letter in reversed(row):
            if letter.isdigit():
                digitString += letter
                break

        returnValue += int(digitString)
        digitString = ""

    return returnValue

print(main())



