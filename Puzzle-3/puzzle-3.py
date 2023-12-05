from pathlib import Path

def main() -> int:
        
    path = Path(__file__).with_name('puzzle-3-data.txt')    
    f = path.open()
    data = f.readlines()

    max = {
        'green': 13,
        'red': 12,
        'blue': 14
    }

    min = {
        'green': 0,
        'red': 0,
        'blue': 0
    }

    idsOfTotalPassing = 0
    totalPowers = []


    for row in data:
        game, pulls =  row.split(': ')
        game = int(game[5:])

        possible = True

        for handfuls in pulls.split('; '):
            colorData = handfuls.split(', ')
            for something in colorData:
                number, color = something.split()
                if int(number) > max[color]:
                    possible = False
                if int(number) > min[color]:
                    min[color] = int(number)
        if possible:
            idsOfTotalPassing += game
        
        gamePower = min['blue'] * min['green'] * min['red']
        totalPowers.append(gamePower)
        min['blue'] = 0
        min['green'] = 0
        min['red'] = 0
    

    returPower = 0
    for line in totalPowers:
        returPower += line
        
    print(returPower)

    return 0

main()
