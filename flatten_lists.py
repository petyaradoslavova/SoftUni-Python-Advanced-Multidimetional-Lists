matrix = []
for n in input().split('|')[::-1]:
    row_data = [str(num) for num in n.split()]
    matrix.extend(row_data)

print(*matrix)

# example input data
# 3
# 1 2 3
# 4 5 6
# 7 8 9
# Add 0 0 5
# Subtract 1 1 2
# END
