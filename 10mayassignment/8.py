def print_pascals_triangle(n):
    for i in range(n):
        row = [1]
        if i > 0:
            for j in range(1, i):
                val = pascals_triangle[i - 1][j - 1] + pascals_triangle[i - 1][j]
                row.append(val)
            row.append(1)
        pascals_triangle.append(row)
        row_str = [str(num) for num in row]
        print(' '.join(row_str).center(n * 3))
pascals_triangle = []
print_pascals_triangle(7)
