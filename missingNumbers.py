""" Func that finds the missing number(s) in a given list of series. """

def missingNumbers(inputList):
    inpList = sorted(inputList)
    tempList = []
    for notnum in range(inpList[0], inpList[-1]+1):
        if notnum not in inputList:
            tempList.append(notnum)
    print("Input :", inputList)
    print("Sorted:", inpList)
    print("Missing series/numbers: ")
    return tempList

mylist = [30, 27, 18, 12, 10, 26, -3, 9, 15, -1, 0]
print(missingNumbers(mylist))

