def cavityMap(grid):
    # Write your code here
    for num in range(len(grid)):
        grid[num] = list(grid[num])
  
    for i in range(1, len(grid) - 1):
        for j in range(1, len(grid[0]) - 1):
            if grid[i][j] > grid[i - 1][j] and grid[i][j] > grid[i][j - 1] and grid[i][j] > grid[i][j + 1] and grid[i][j] > grid[i + 1][j]:
                grid[i][j] = 'X'
  
    return ("".join(row) for row in grid)