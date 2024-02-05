def move(direction: str, ):
    matrix[ship_position[0]][ship_position[1]] = '-'
    r = ship_position[0] + directions[direction][0]
    c = ship_position[1] + directions[direction][1]
    current_position = [r,c]

    if not (0 <= r < size and 0 <= c < size):
        boundary(current_position,size)
        return [current_position[0],current_position[1]]
    else:
        return [r, c]


def boundary(position,size):
    for i in range(2):
        if position[i] < 0:
            position[i] = size - 1
        elif position[i] >= size:
            position[i] = 0


def handle_results(quote):
    if quote >= 20:
        print('Success! You managed to reach the quota!')
    else:
        print(f"You didn't catch enough fish and didn't reach the quota! You need {20 - quote} tons of fish more.")
    if quote > 0:
        print(f"Amount of fish caught: {quote} tons.")


size = int(input())

matrix = []
ship_position = []
quote = 0
current_char = ''

directions = {
    'up':  (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}
survived = True
for row in range(size):
    matrix.append(list(input()))

    if 'S' in matrix[row]:
        ship_position = [row,matrix[row].index('S')]
        matrix[row][ship_position[1]] = '-'

while True:
    command = input()
    if command == 'collect the nets':
        break

    ship_position = move(command)

    current_char = matrix[ship_position[0]][ship_position[1]]
    if current_char.isdigit():
        quote += int(current_char)

    elif current_char == 'W':
        quote = 0
        survived = False
        print(f"You fell into a whirlpool! The ship sank and you lost the fish you caught. "
              f"Last coordinates of the ship: [{ship_position[0]},{ship_position[1]}]")
        break

    matrix[ship_position[0]][ship_position[1]] = 'S'

if survived:
    handle_results(quote)
    for row in matrix:
        print("".join(row))
