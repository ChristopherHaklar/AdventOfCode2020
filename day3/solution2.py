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

a = solution1("input.txt", 1, 1)
b = solution1("input.txt", 1, 3)
c = solution1("input.txt", 1, 5)
d = solution1("input.txt", 1, 7)
e = solution1("input.txt", 2, 1)
print("Product of Slopes: ")
print((a*b*c*d*e))