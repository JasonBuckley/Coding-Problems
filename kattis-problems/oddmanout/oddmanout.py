from sys import stdin,stdout

def single_number(arr):
  single = 0

  for i in arr:
    single ^= i

  return single

cases = int(stdin.readline())
result = ""

for i in range(cases):
  length = stdin.readline()
  arr = [int(i) for i in stdin.readline().split()]
  result+= "Case #" + str(i+1) + ": " + str(single_number(arr)) + "\n"

stdout.write(result)