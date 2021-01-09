import re

file = open( "regex_sum_2.txt.txt")
numbers = []
for line in file:
    numbers = numbers + re.findall("[0-9]+", line)
sum =0
for num in numbers:
    sum = sum + int(num)
print( sum )
