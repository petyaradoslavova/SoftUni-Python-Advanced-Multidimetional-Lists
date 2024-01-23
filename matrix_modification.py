def is_valid_index(r,c):
    if 0 <= int(r) <= len(matrix)-1 and 0 <=int(c) <= len(matrix)-1:
        return True
    print("Invalid coordinates")


matrix = [[int(num) for num in input().split()] for _ in range(int(input()))]

while True:
    line = input()
    if line == 'END':
        break
        
    command, *coordinates,value = line.split()

    if command == 'Add':
        row,col = coordinates
        if is_valid_index(row,col):
            matrix[int(row)][int(col)] += int(value)

    elif command == 'Subtract':
        row,col= coordinates
        if is_valid_index(row, col):
            matrix[int(row)][int(col)] -= int(value)

[print(*row, sep=' ') for row in matrix]


