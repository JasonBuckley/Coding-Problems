import math

def secret_message(l,m,message):
  encrypt = ""

  while(len(message) < m*m):
    message+="*"

  for i in range(m):
    for k in range(m-1,-1,-1):
      if(message[k*m+i] != '*'):
        encrypt+=(message[k*m+i])

  print(encrypt)

num = int(input())

for i in range(num):
  message = input();
  l = len(message)
  m = math.ceil(l**(1/2))

  secret_message(l,m,message)


