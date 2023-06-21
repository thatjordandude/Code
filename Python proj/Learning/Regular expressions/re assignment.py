import re

ope = open("regex_sum_1794758.txt", encoding='utf-8')
file = ope.read()
numbers = re.findall('[0-9]+', file)
sum_numbers = sum(map(int, numbers))

print(sum_numbers)




ope.close()