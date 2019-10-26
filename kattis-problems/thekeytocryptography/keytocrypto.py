from sys import stdin,stdout

def decrypt_message(ciphertext,key):
  answer = ""

  for i in range(len(ciphertext)):
    decryptedLetter = chr((ord(ciphertext[i]) - ord(key[i]))%26 + ord('A'))
    key+= decryptedLetter
    answer+= decryptedLetter

  return answer

print(decrypt_message(stdin.readline().strip(),stdin.readline().strip()))
