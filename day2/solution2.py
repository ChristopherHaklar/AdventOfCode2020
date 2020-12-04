import re

def solution2(fileName):
  validPasswordCount = 0
  input = []
  pattern = r'(^\d+)\D(\d+)\D([a-z])\W+([a-z]+)'
  file = open(fileName, "r")
  for line in file:
      input.append(re.search(pattern, line).group(1, 2, 3, 4))
  file.close()

  for tupleInput in input:
    min, max, testLetter, passwordString = tupleInput
    testLetterCount = 0
    for i in passwordString:
      if i == testLetter:
        testLetterCount += 1
    if testLetterCount <= int(max) and testLetterCount >= int(min):
        if len(passwordString) >= int(max):
          if not((passwordString[int(min)] == testLetter) and (passwordString[int(max)] == testLetter)):
              validPasswordCount += 1
              print(passwordString)
        else:
          if (passwordString[int(min)] == testLetter):
              validPasswordCount +=1
              print(passwordString)

  return validPasswordCount

print(solution2("input.txt"))
