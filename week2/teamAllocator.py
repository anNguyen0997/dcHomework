#Team Allocator
import random

print('Welcome to Team Allocator!')

players = ['Juan','Tony','Donny','Dennis','Brett','Anthony','Duke','Danny', 'Edgar', 'Ricky']

while True:
    random.shuffle(players)

    team1 = players[:len(players)//2]
    print('Team 1 Captain: ' + random.choice(team1))
    print('Team 1: ')
    for player in team1:
        print(player)

    team2 = players[:len(players)//2]
    print('\n Team 2 Captain : ' + random.choice(team2))
    print("Team 2: ")
    for player in team2:
        print(player)

    response = input('Pick teams again? Type y or n: ')
    if response == 'n':
        break