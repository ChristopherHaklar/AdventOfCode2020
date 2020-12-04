def solution1(fileName, x, y):
    with open(fileName) as textFile:
        array = [list(line.strip()) for line in textFile]

    treeCount=0
    col=0
    for row in range(0,len(array),x):
        if array[row][col%len(array[row])] == '#':
            treeCount += 1
        col += y
    return treeCount

print("Number of Trees: ")
print(solution1("input.txt", 1, 3))