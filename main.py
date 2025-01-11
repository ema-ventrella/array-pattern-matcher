def main():
    firstArray = list(map(int, input("Your series of numbers: ").split(', '))) #devided by ', '
    newArray = []
    i = 0
    while i < len(firstArray) - 2:
        if firstArray[i] == firstArray[i + 2]:
            newArray.append([firstArray[i], firstArray[i + 1], firstArray[i + 2]])
        i += 1
    print(newArray)

main()
