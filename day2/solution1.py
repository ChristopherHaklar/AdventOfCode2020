import re

def solution1(fileName):
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
      validPasswordCount += 1
      print(passwordString)

  return validPasswordCount

print(solution1("input.txt"))
