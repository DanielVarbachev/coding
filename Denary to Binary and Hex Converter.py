TypeOfInput = input("What base will your input be? ")
Binary = ["binary","Binary","b","B","2"]
Hex = ["Hex","hex","Hexadecimal","hexadecimal","h","H"]
thingy = 0
thing = 0
BTotal = 0
HTotal = 0


if TypeOfInput in Binary:
    numberstring = input("Enter your number: ")
    number = list(numberstring)
    length = len(number)
    lastcolumn = 2 ** (length - 1)
    for i in range(length):
        digit = number[thingy]
        if digit == "1":
            BTotal += lastcolumn
        lastcolumn = lastcolumn / 2
        thingy += 1

    IntBTotal = int(BTotal)
    print("Final answer = " , IntBTotal)

if TypeOfInput in Hex:
    numberstring = input("Enter your number: ")
    number = list(numberstring)
    length = len(number)
    thing = length - 1
    for i in range(length):
        digit = number[thingy]
        if digit == "1":
            HTotal += 1 * 16 ** thing
        if digit == "2":
            HTotal += 2 * 16 ** thing
        if digit == "3":
            HTotal += 3 * 16 ** thing
        if digit == "4":
            HTotal += 4 * 16 ** thing
        if digit == "5":
            HTotal += 5 * 16 ** thing
        if digit == "6":
            HTotal += 6 * 16 ** thing
        if digit == "7":
            HTotal += 7 * 16 ** thing
        if digit == "8":
            HTotal += 8 * 16 ** thing
        if digit == "9":
            HTotal += 9 * 16 ** thing
        if digit.lower() == "a":
            HTotal += 10 * 16 ** thing
        if digit.lower() == "b":
            HTotal += 11 * 16 ** thing
        if digit.lower() == "c":
            HTotal += 12 * 16 ** thing
        if digit.lower() == "d":
            HTotal += 13 * 16 ** thing
        if digit.lower() == "e":
            HTotal += 14 * 16 ** thing
        if digit.lower() == "f":
            HTotal += 15 * 16 ** thing
        thing += -1
        thingy += 1
    print("Final answer = " , int(HTotal))
    


    

