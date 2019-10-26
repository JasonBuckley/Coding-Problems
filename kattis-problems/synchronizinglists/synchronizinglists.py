from sys import stdin,stdout

def synchronizing_lists(arr1, arr2, dict_arr1,n):
  synced = [None for x in range(n)]
  arr1.sort()
  arr2.sort()

  for i in range(n):
    synced[dict_arr1[arr1[i]]] = (str(arr2[i])+"\n")
  
  for i in synced:
    stdout.write(i)

n = int(stdin.readline())

while(n != 0):
  if(n != 0):
    temp1 = [None for x in range(n)]
    dict_temp1 = {}
    for i in range(n):
      temp1[i] = int(stdin.readline().strip("\n"))
      dict_temp1[temp1[i]] = i

    temp2 = [None for x in range(n)]
    for i in range(n):
      temp2[i] = int(stdin.readline().strip("\n"))
    
    synchronizing_lists(temp1,temp2,dict_temp1,n)
  
  n = int(stdin.readline())
  if(n != 0):
    stdout.write("\n")
  
