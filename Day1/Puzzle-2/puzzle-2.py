def main() -> int:

    f = open('puzzle-2-codes.txt', 'r')
    data = f.readlines()

    digitString = ""
    returnValue = 0

    class numberPair:
        def __init__(self, a, b, c):
            self.number = a
            self.index = b
            self.occurances = c
        def __repr__(self) -> str:
            return "Number: % s Index: % s \n Occurance at index(s): % s" % (self.number, self.index, self.occurances)


    for row in data:

        numbers = [ 
        numberPair("1", row.find("one"), [i for i in range(len(row)) if row.startswith("one", i)]),
        numberPair("2", row.find("two"), [i for i in range(len(row)) if row.startswith("two", i)]),
        numberPair("3", row.find("three"), [i for i in range(len(row)) if row.startswith("three", i)]),
        numberPair("4", row.find("four"), [i for i in range(len(row)) if row.startswith("four", i)]),
        numberPair("5", row.find("five"), [i for i in range(len(row)) if row.startswith("five", i)]),
        numberPair("6", row.find("six"), [i for i in range(len(row)) if row.startswith("six", i)]),
        numberPair("7", row.find("seven"), [i for i in range(len(row)) if row.startswith("seven", i)]),
        numberPair("8", row.find("eight"), [i for i in range(len(row)) if row.startswith("eight", i)]),
        numberPair("9", row.find("nine"), [i for i in range(len(row)) if row.startswith("nine", i)]),
        numberPair("1", row.find("1"), [i for i in range(len(row)) if row.startswith("1", i)]),
        numberPair("2", row.find("2"), [i for i in range(len(row)) if row.startswith("2", i)]),
        numberPair("3", row.find("3"), [i for i in range(len(row)) if row.startswith("3", i)]),
        numberPair("4", row.find("4"), [i for i in range(len(row)) if row.startswith("4", i)]),
        numberPair("5", row.find("5"), [i for i in range(len(row)) if row.startswith("5", i)]),
        numberPair("6", row.find("6"), [i for i in range(len(row)) if row.startswith("6", i)]),
        numberPair("7", row.find("7"), [i for i in range(len(row)) if row.startswith("7", i)]),
        numberPair("8", row.find("8"), [i for i in range(len(row)) if row.startswith("8", i)]),
        numberPair("9", row.find("9"), [i for i in range(len(row)) if row.startswith("9", i)]) ]
        
        for number in numbers:
            if isinstance(number.occurances, list):
                if len(number.occurances) > 1:
                    for i in range(len(number.occurances)):
                        numbers.append(numberPair(number.number, number.occurances[i], number.occurances[i]))

        numbers.sort(key=lambda x : x.index)

        beenAdded = 0

        for pair in numbers:
            if pair.index != -1:
                if beenAdded == 0:

                    digitString += pair.number
                    digitString += numbers[len(numbers)-1].number
                    returnValue += int(digitString)

                    beenAdded = 1

            digitString = ""
            
    return returnValue

        

print(main())