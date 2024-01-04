def pascal_triangle(n):
    if n <= 0:
        return []

    triangle = [[1] * (x + 1) for x in range(n)]

    for x in range(2, n):
        for y in range(1, x):
            triangle[x][y] = triangle[x - 1][y - 1] + triangle[x - 1][y]

    return triangle
