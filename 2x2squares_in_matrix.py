rows,cols = [int(n) for n in input().split()]

matrix = [[str(el) for el in input().split()] for _ in range(rows)]

number_of_equals = 0
not_found = True

for row_index in range(rows-1):
    for col_index in range(cols-1):
        current_element= matrix[row_index][col_index]
        element_below = matrix[row_index+1][col_index]
        next_element = matrix[row_index][col_index+1]
        diagonal_element = matrix[row_index+1][col_index+1]
        if current_element == element_below == next_element == diagonal_element:
            number_of_equals += 1
            not_found = False

if not_found:
    print('0')
else:
    print(number_of_equals)