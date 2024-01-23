n = int(input())

commands = input().split()
matrix = []

miner_position = []
collected_coals = 0
total_coals = 0

directions = {
    'up':  (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

for row in range(n):
    matrix.append(input().split())

    if 's' in matrix[row]:
        miner_position = [row,matrix[row].index('s')]
        matrix[row][miner_position[1]] = '*'

    total_coals += matrix[row].count('c')

for command in commands:
    r,c = miner_position[0] + directions[command][0] ,miner_position[1] + directions[command][1]

    if not(0<=r<n and 0 <=c<n):
        continue

    miner_position = [r,c]

    if matrix[r][c] == 'c':
        collected_coals+= 1

        if collected_coals == total_coals:
            print(f"You collected all coal! ({r}, {c})")
            break

    elif matrix[r][c] == 'e':
        print(f"Game over! ({r}, {c})")
        break

    matrix[r][c] = '*'

else:
    print(f"{total_coals-collected_coals} pieces of coal left. ({miner_position[0]}, {miner_position[1]})")