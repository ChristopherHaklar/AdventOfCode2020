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
    if len(passwordString) >= int(max):
      if bool((passwordString[int(min)-1] == testLetter)) != bool((passwordString[int(max)-1] == testLetter)):
          validPasswordCount += 1
    else:
      if (passwordString[int(min)-1] == testLetter):
          validPasswordCount +=1

  return validPasswordCount

print(solution2("input.txt"))
