import math

def saving_for_retirement(raw_input):
  info = (raw_input.split(" "))
  a_years = int(info[3]) + math.ceil(((float(info[1])-float(info[0]))*float(info[2]))/float(info[4]))

  if((float(info[1])-float(info[0]))*float(info[2]) == (int(a_years) - int(info[3]))*int(info[4])):
    a_years+=1

  return a_years

print(saving_for_retirement(input()))