size = int(input())

matrix = []
alice_position = []

tea_bags = 0

directions = {
    'up':  (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

for row in range(size):
    matrix.append(input().split())

    if 'A' in matrix[row]:
        alice_position = [row,matrix[row].index('A')]
        matrix[row][alice_position[1]] = '*'

while True:
    command = input()
    pos_row,pos_col = alice_position[0] + directions[command][0] , alice_position[1] + directions[command][1]

    if not(0 <= pos_row < size and 0 <= pos_col < size):
        print("Alice didn't make it to the tea party.")
        break

    elif matrix[pos_row][pos_col] == 'R':
        matrix[pos_row][pos_col] = '*'
        print("Alice didn't make it to the tea party.")
        break

    alice_position = [pos_row,pos_col]

    if matrix[pos_row][pos_col] == '*':
        continue

    elif matrix[pos_row][pos_col] == '.':
        matrix[pos_row][pos_col] = '*'

    else:
        tea_bags += int(matrix[pos_row][pos_col])
        matrix[pos_row][pos_col] = '*'
        if tea_bags >= 10:
            print("She did it! She went to the party.")
            break

[print(*row) for row in matrix]

# input data:
# 5
# . A . . 1
# R . 2 . .
# 4 7 . 1 .
# . . . 2 .
# . 3 . . .
# down
# right
# left
# down
# up
# left

# 7
# . A . 1 1 . .
# 9 . . . 6 . 5
# . 6 . R . . .
# . 3 . . 1 . .
# . . . 2 . . 2
# . 3 . . 1 . .
# . 8 3 . . . 2
# left
# down
# down
# right








