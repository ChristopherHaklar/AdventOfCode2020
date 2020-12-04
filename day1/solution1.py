def solution1(fileName):
  input = []
  file = open(fileName, "r")
  for x in file:
    input.append(int(x))
  file.close()
  for x in input:
    for y in input:
      if(x + y == 2020):
        return(x*y)

print(solution1("input.txt"))
