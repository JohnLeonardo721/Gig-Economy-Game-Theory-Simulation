"""
Grid Environment & Dynamic Demand Generator Module
"""
import numpy as np

class GridEnvironment:
    def __init__(self, grid_size=10, hotspot_ratio=0.8):
        self.grid_size = grid_size
        self.hotspot_ratio = hotspot_ratio
        # Initialize 10x10 grid matrix
        self.grid = np.zeros((grid_size, grid_size))
        print(f"Initialized {grid_size}x{grid_size} Grid Environment.")

if __name__ == "__main__":
    env = GridEnvironment()
