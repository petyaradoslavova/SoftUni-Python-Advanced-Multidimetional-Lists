def move(direction: str, ):
    matrix[santa_position[0]][santa_position[1]] = '-'
    r = santa_position[0] + directions[direction][0]
    c = santa_position[1] + directions[direction][1]

    if not (0 <= r < matrix_size and 0 <= c < matrix_size):
        return santa_position
    else:
        return [r, c]


number_of_presents = int(input())
matrix_size = int(input())
matrix = []
santa_position = []
nice_kids_count = 0

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),

}

for row in range(matrix_size):
    matrix.append(input().split())

    if 'S' in matrix[row]:
        santa_position = [row, matrix[row].index('S')]
        matrix[row][santa_position[1]] = '-'

    nice_kids_count += matrix[row].count('V')

while True:
    if number_of_presents == 0:
        break
    command = input()
    if command == 'Christmas morning':
        break

    santa_position = move(command)

    if matrix[santa_position[0]][santa_position[1]] == 'V':
        number_of_presents -= 1

    elif matrix[santa_position[0]][santa_position[1]] == 'C':
        for direction in directions:
            r = santa_position[0] + directions[direction][0]
            c = santa_position[1] + directions[direction][1]

            if number_of_presents == 0:
                break
            if matrix[r][c] == 'V' or matrix[r][c] == 'X':
                number_of_presents -= 1
            matrix[r][c] = '-'
    matrix[santa_position[0]][santa_position[1]] = 'S'

count_v = sum(row.count('V') for row in matrix)
if number_of_presents == 0 and count_v > 0:
    print('Santa ran out of presents!')

[print(*row) for row in matrix]

if count_v == 0:
    print(f"Good job, Santa! {nice_kids_count} happy nice kid/s.")
else:
    print(f"No presents for {count_v} nice kid/s.")