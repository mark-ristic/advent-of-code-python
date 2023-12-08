# advent 1
sum = 0

file = open('input1.txt')

digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

lines = file.readlines()

for line in lines:
    converted = ''
    index_map = {}
        #converted = converted + '1'
    found = [i for i in range(len(line)) if line.startswith('one', i)]
    for f in found:
        index_map[f] = '1'
    found = [i for i in range(len(line)) if line.startswith('two', i)]
    for f in found:
        index_map[f] = '2'
    found = [i for i in range(len(line)) if line.startswith('three', i)]
    for f in found:
        index_map[f] = '3'
    found = [i for i in range(len(line)) if line.startswith('four', i)]
    for f in found:
        index_map[f] = '4'
    found = [i for i in range(len(line)) if line.startswith('five', i)]
    for f in found:
        index_map[f] = '5'
    found = [i for i in range(len(line)) if line.startswith('six', i)]
    for f in found:
        index_map[f] = '6'
    found = [i for i in range(len(line)) if line.startswith('seven', i)]
    for f in found:
        index_map[f] = '7'
    found = [i for i in range(len(line)) if line.startswith('eight', i)]
    for f in found:
        index_map[f] = '8'
    found = [i for i in range(len(line)) if line.startswith('nine', i)]
    for f in found:
        index_map[f] = '9'
    found = [i for i in range(len(line)) if line.startswith('1', i)]
    for f in found:
        index_map[f] = '1'
    found = [i for i in range(len(line)) if line.startswith('2', i)]
    for f in found:
        index_map[f] = '2'
    found = [i for i in range(len(line)) if line.startswith('3', i)]
    for f in found:
        index_map[f] = '3'
    found = [i for i in range(len(line)) if line.startswith('4', i)]
    for f in found:
        index_map[f] = '4'
    found = [i for i in range(len(line)) if line.startswith('5', i)]
    for f in found:
        index_map[f] = '5'
    found = [i for i in range(len(line)) if line.startswith('6', i)]
    for f in found:
        index_map[f] = '6'
    found = [i for i in range(len(line)) if line.startswith('7', i)]
    for f in found:
        index_map[f] = '7'
    found = [i for i in range(len(line)) if line.startswith('8', i)]
    for f in found:
        index_map[f] = '8'
    found = [i for i in range(len(line)) if line.startswith('9', i)]
    for f in found:
        index_map[f] = '9'

    keyz = list(index_map.keys())
    keyz = sorted(keyz)
    
    converted = ''
    for key in keyz:
        converted = converted + index_map[key]
    #print(keys)

    line = converted
    first_digit = ''
    first_digit_set = False
    last_digit = ''
    digit = ''
    for char in converted:
        if char in digits:
            if not first_digit_set:
                first_digit = char
                first_digit_set = True
            if first_digit_set:
                last_digit = char
    digit = first_digit + last_digit
    print(digit)
    sum = sum + int(digit)

print(sum)