def solution2(fileName):
    input = []
    file = open(fileName, "r")
    for x in file:
        input.append(int(x))
    file.close()
    for x in input:
        for y in input:
            for z in input:
                if(x + y + z == 2020):
                    return(x*y*z)

print(solution2("input.txt"))
