
def peragram(word):
  occurrences = {}
  offset = 0

  for letter in word:
    if(occurrences.get(letter) != None):
      occurrences[letter]+=1
    else:
      occurrences[letter]=1

  #there must be 2 of each letter besides 1 in a palindrome
  for i in occurrences.values():
    if(i%2 == 1):
      offset+=1

  return offset - 1 if offset - 1 > 0 else 0

word = input()

print(peragram(word))