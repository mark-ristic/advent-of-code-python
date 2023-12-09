import re

def is_surrounded_by_symbol(lines, direction, digits_and_dots):
    return lines[direction] not in digits_and_dots and lines[direction] is not None

file = open('input3.txt')
lines = file.readlines()
digits_and_dots = ['0','1','2','3','4','5','6','7','8','9', '.']
indices = []
numbers = []
sum = 0
for i, line in enumerate(lines):
    numbers_in_line = re.findall('[0-9]+', line)
    for number in numbers_in_line:
        print(line)
        local_indices = []
        start_index = line.find(number)
        line = re.sub(number, '.' * len(number), line, 1)
        end_index = len(number) - 1 + start_index
        numbers.append(number)
        for x in range(start_index, end_index+1):
            local_indices.append([i,x])
        indices.append(local_indices)

symbol_indices = []
for i, line in enumerate(lines):
    line = line.strip()
    for j, char in enumerate(line):
        if char == '*':
            symbol_indices.append([i,j])

print(indices)
print()
print(symbol_indices)
in_range = [-1, 0, 1]
good_dots = []

for symbol in symbol_indices:
    multiply_this = []
    for en, dots in enumerate(indices):   
        for dot in dots:
            #print(dot[0], dot[1])
            diff_row = dot[0] - symbol[0]
            diff_column = dot[1] - symbol[1]
            if diff_row in in_range and diff_column in in_range:
                multiply_this.append(int(numbers[en]))
                break


    if len(multiply_this) == 2:
        sum = sum + (multiply_this[0] * multiply_this[1])
    print('-----', multiply_this)

print(sum)