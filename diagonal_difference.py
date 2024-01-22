size_of_square_matrix = int(input())

matrix = [[int(el) for el in input().split()] for _ in range(size_of_square_matrix)]
primary = [matrix[r][r] for r in range(size_of_square_matrix)]
secondary = [matrix[r][size_of_square_matrix-r-1] for r in range(size_of_square_matrix)]

primary_sum = sum(primary)
secondary_sum = sum(secondary)

print(f'{abs(primary_sum-secondary_sum)}')