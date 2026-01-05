#This script will print a pyramid with asterisks

rows = 5
star = 1
for i in range(rows):
  print((rows-i)*' ' + star*'*')
  star+=2
