def reverse_bin_to_dec(num): 
  bin_str = str((bin(num)))
  return int("0b" + bin_str[:1:-1],2)

number = int(input(),10)

print(reverse_bin_to_dec(number))