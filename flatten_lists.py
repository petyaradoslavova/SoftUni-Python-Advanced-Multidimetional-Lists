matrix = []
for n in input().split('|')[::-1]:
    row_data = [str(num) for num in n.split()]
    matrix.extend(row_data)

print(*matrix)
