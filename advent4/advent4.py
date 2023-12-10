file = open('input4.txt')
lines = file.readlines()

sum = 0
scratch = {}

for en, line in enumerate(lines):
    winners = 0
    line = line.replace('  ', ' ')
    num = en + 1
    replace_this = 'Card ' + str(num) +  ': '
    line = line.replace(replace_this, '')
    split = line.split('|')
    winning = split[0].strip().split(' ')
    mine = split[1].strip().split(' ')
    
    for number in mine:
        if number in winning:
            winners = winners + 1
  
    scratch[en] = winners #how many winning numbers does each card have

print(scratch)
winning_repeated = {}



for key in scratch.keys():
    winning_repeated[key] = [scratch[key], 1]
    print(winning_repeated[key])

for index, (key, value) in enumerate(scratch.items()):

    end = key + value + 1 if key + value + 1 < len(lines) - 1 else len(lines) - 1
    print(key+1, end-1)
    for i in range(key + 1, end):
        for x in range(winning_repeated[key][1]):
            if (i in scratch.keys()):
                winning_repeated[i][1] = winning_repeated[i][1] + 1

for key in scratch.keys():
    print(key,':', winning_repeated[key])

sum = 0
for key in winning_repeated.keys():
    sum = sum + winning_repeated[key][1]

print(sum + winning_repeated[184][1])