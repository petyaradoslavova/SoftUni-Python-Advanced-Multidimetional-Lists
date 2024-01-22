rows,cols = [int(n) for n in input().split()]

matrix = [[int(el) for el in input().split()] for _ in range(rows)]

max_sum = float('-inf')

sub_matrix = []
sum_elements = 0

for row_index in range(rows-2):
    for col_index in range(cols-2):
        current_element= matrix[row_index][col_index]
        element_below = matrix[row_index+1][col_index]
        el_below_below = matrix[row_index+2][col_index]
        next_element = matrix[row_index][col_index+1]
        next_next_element  = matrix[row_index][col_index+2]
        diagonal_element = matrix[row_index+1][col_index+1]
        next_to_diagonal_el = matrix[row_index+1][col_index+2]
        below_diagonal_el = matrix[row_index+2][col_index+1]
        next_to_bewol_the_diagonal = matrix[row_index+2][col_index+2]
        sum_elements = current_element + element_below + next_element + next_next_element+ diagonal_element + next_to_diagonal_el + next_to_bewol_the_diagonal+below_diagonal_el + el_below_below

        if max_sum < sum_elements:
            max_sum = sum_elements
            sub_matrix = [[current_element,next_element,next_next_element],[element_below,diagonal_element,next_to_diagonal_el],[el_below_below,below_diagonal_el,next_to_bewol_the_diagonal]]

print(f'Sum = {max_sum}')
print(*sub_matrix[0])
print(*sub_matrix[1])
print(*sub_matrix[2])
