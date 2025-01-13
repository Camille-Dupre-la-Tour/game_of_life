import numpy as np
import matplotlib.pyplot as plt

def initialize_grid(rows, cols):
    return np.random.choice([0, 1], size=(rows, cols))

def count_neighbors(grid, x, y):
    rows, cols = grid.shape
    return sum(grid[(x + i) % rows, (y + j) % cols] 
               for i in [-1, 0, 1] for j in [-1, 0, 1] if not (i == 0 and j == 0))

def update_grid(grid):
    rows, cols = grid.shape
    new_grid = np.zeros((rows, cols), dtype=int)
    for x in range(rows):
        for y in range(cols):
            neighbors = count_neighbors(grid, x, y)
            if grid[x, y] == 1 and neighbors in [2, 3]:
                new_grid[x, y] = 1
            elif grid[x, y] == 0 and neighbors == 3:
                new_grid[x, y] = 1
    return new_grid

def run_game(rows, cols, steps):
    grid = initialize_grid(rows, cols)
    plt.ion()
    for _ in range(steps):
        plt.imshow(grid, cmap="binary")
        plt.pause(0.1)
        grid = update_grid(grid)
    plt.ioff()
    plt.show()
run_game(20, 20, 100)
