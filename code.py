import numpy as np
import matplotlib.pyplot as plt

def initialize_grid(rows, cols):
    return np.random.choice([0, 1], size=(rows, cols))

def count_neighbors(grid, x, y, boundary="wrapping"):
    rows, cols = grid.shape
    neighbors = 0

    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if i == 0 and j == 0:
                continue
            nx, ny = x + i, y + j

            if boundary == "wrapping":
                # Wrap around boundaries
                neighbors += grid[nx % rows, ny % cols]
            elif boundary == "fixed":
                # Fixed boundaries: Ignore out-of-bound indices
                if 0 <= nx < rows and 0 <= ny < cols:
                    neighbors += grid[nx, ny]

    return neighbors

def update_grid(grid, boundary="wrapping"):
    rows, cols = grid.shape
    new_grid = np.zeros((rows, cols), dtype=int)
    for x in range(rows):
        for y in range(cols):
            neighbors = count_neighbors(grid, x, y, boundary)
            if grid[x, y] == 1 and neighbors in [2, 3]:
                new_grid[x, y] = 1
            elif grid[x, y] == 0 and neighbors == 3:
                new_grid[x, y] = 1
    return new_grid

def run_game(rows, cols, steps, boundary="wrapping"):
    grid = initialize_grid(rows, cols)
    plt.ion()
    for _ in range(steps):
        plt.imshow(grid, cmap="binary")
        plt.pause(0.1)
        grid = update_grid(grid, boundary)
    plt.ioff()
    plt.show()
