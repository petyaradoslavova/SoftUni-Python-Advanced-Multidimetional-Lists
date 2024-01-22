rows_cols = int(input())

matrix = [[int(n) for n in input().split()] for _ in range(rows_cols)]

coordinates = ((int(x) for x in coordinate.split(","))for coordinate in input().split())

directions = (
    (-1,0),#up
    (1,0),#down
    (0,1),#right
    (0,-1),#left
    (-1,1),#top-right
    (-1,-1),#top-left
    (1,-1),#bottom_left
    (1,1),#bottom-right
    (0,0),#current

)
for row,col in coordinates:
    if matrix[row][col] <=0:
        continue
    for x,y in directions:
        r,c = row+x,col+y

        if 0 <= r < rows_cols and 0 <=c<rows_cols:
            matrix[r][c] -= matrix[row][col] if matrix[r][c] > 0 else 0

alive_cells = [num for row in range(rows_cols) for num in matrix[row] if num > 0]
print(f'Alive cells: {len(alive_cells)}')
print(f"Sum: {sum(alive_cells)}")
[print(*row) for row in matrix]


# example testing data 
# 4
# 8 3 2 5
# 6 4 7 9
# 9 9 3 6
# 6 8 1 2
# 1,2 2,1 2,0
