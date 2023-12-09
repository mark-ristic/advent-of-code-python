import re

def is_surrounded_by_symbol(lines, direction, digits_and_dots):
    return lines[direction] not in digits_and_dots and lines[direction] is not None

file = open('input3.txt')
lines = file.readlines()
digits_and_dots = ['0','1','2','3','4','5','6','7','8','9', '.']
indices = []
numbers = []
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
        if char not in digits_and_dots and char is not None:
            symbol_indices.append([i,j])

print(indices)
print()
print(symbol_indices)
in_range = [-1, 0, 1]
good_dots = []

for en, dots in enumerate(indices):
    print('******************************************')
    bad_dot = True
    break_dots = False
    for dot in dots:
        if break_dots is True:
            break
        #print(dot[0], dot[1])
        
        for symbol in symbol_indices:
            diff_row = dot[0] - symbol[0]
            diff_column = dot[1] - symbol[1]
            print(dot, 'dot')
            print(symbol, 'symbol')
            print(diff_row, diff_column, 'diff')
            if diff_row in in_range and diff_column in in_range:
                bad_dot = False
                good_dots.append(numbers[en])
                break_dots = True
                break
                print('good')
            else:
                print('bad')
            print('>>>>>>>>')

    print('-----')

sum = 0
print(numbers)
for number in good_dots:
    sum = sum + int(number)

print(sum)