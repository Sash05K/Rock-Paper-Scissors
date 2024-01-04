from random import choice

combinations = ['Rock', 'Paper', 'Scissors']

pc_points = 0
player_points = 0

while pc_points != 3 and player_points != 3:
    pc = choice(combinations)
    player = input('Rock, Paper, Scissors? ').capitalize()

    if pc == player:
        print(f"{pc} | {player}")
        print('Lets try again!')
        print(f"Pc points: {pc_points} | Player points: {player_points}")
    elif (pc == 'Rock' and player == 'Paper')\
        or (pc == 'Paper' and player == 'Scissors')\
            or (pc == 'Scissors' and player == 'Rock'):
        player_points += 1
        print(f"{pc} | {player}")
        print('Player win')
        print(f"Pc points: {pc_points} | Player points: {player_points}")
    else:
        pc_points += 1
        print(f"{pc} | {player}")
        print('Pc win')
        print(f"Pc points: {pc_points} | Player points: {player_points}")


print('Game Over!')
print('Player win' if player_points == 3 else 'Pc win')
