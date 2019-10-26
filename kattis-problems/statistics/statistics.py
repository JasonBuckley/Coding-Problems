from sys import stdin

def statistics(case, arr):
  minimum = 1000001
  maximum = -1000001

  for i in arr:
    minimum = minimum if minimum < i else i
    maximum = maximum if maximum > i else i

  print("case " + str(case) + ": " + str(minimum) + " " + str(maximum) + " " + str(maximum - minimum))

cases = stdin.readlines()

for i in range(len(cases)):
  data = [int(n) for n in cases[i].split(" ")]
  data.pop(0)
  statistics(i+1,data)
