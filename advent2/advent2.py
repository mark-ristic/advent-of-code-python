# Game 1: 
#12 red, 2 green, 5 blue; 
#9 red, 6 green, 4 blue; 
#10 red, 2 green, 5 blue; 8 blue, 9 red
def get_game_id(line):
    line = line.replace('Game ', '')
    splitty = line.split(':')
    return splitty[0]

def get_games(line):
    splitty = line.split(':')
    return  splitty[1].split(';')

file = open('input2.txt')
lines = file.readlines()

sum = 0
#r = 12
#g = 13
#b = 14
#print(lines[0])
#print(get_game_id(lines[0]))
#print(get_games(lines[0]))

#part 1
'''for line in lines:
    games = get_games(line)
    should_add = True
    for game in games:
        for set in game.split(';'):
            red = 0
            blue = 0
            green = 0
            split_set = []
            if ',' in set:
                split_set = set.split(',')
            else:
                split_set = [color]
            for color in set.split(','):
                replaced = ''
                #print(color)
                if 'red' in color:
                    replaced = color.replace('red', '')
                    replaced = replaced.strip()
                    red = red + int(replaced)
                if 'blue' in color:
                    replaced = color.replace('blue', '')
                    replaced = replaced.strip()
                    blue = blue + int(replaced)
                if 'green' in color:
                    replaced = color.replace('green', '')
                    replaced = replaced.strip()
                    green = green + int(replaced)
            
            if red > r or blue > b or green > g:
                should_add = False
            
    if should_add:
        sum = sum + int(get_game_id(line))'''

for line in lines:
    games = get_games(line)
    should_add = True
    red = 0
    blue = 0
    green = 0
    for game in games:    
        print(red, green, blue)
        split_set = []
        if ',' in game:
            split_set = game.split(',')
        else:
            split_set = [game]
        for color in game.split(','):
            replaced = ''
            print(color)
            if 'red' in color:
                replaced = color.replace('red', '')
                replaced = replaced.strip()
                if int(replaced) > red:
                    red = int(replaced)
                
            if 'blue' in color:
                replaced = color.replace('blue', '')
                replaced = replaced.strip()
                if int(replaced) > blue:
                    blue = int(replaced)
        
            if 'green' in color:
                replaced = color.replace('green', '')
                replaced = replaced.strip()
                if int(replaced) > green:
                    green = int(replaced)
        print('end of turn -----')
        print()
            
    print('*********rgb', red, green, blue)
    sum = sum + (red * green * blue)

'''
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
'''


print(sum)