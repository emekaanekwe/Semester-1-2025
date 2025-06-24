class Environment:
    """The envronment is designed for a 5x5 grid world
    """
    def __init__(self, grid_size):
        # Grid setup
        self.grid_size = grid_size
        self.grid_world = tuple((x, y) for x in range(grid_size) for y in range(grid_size))
        self.a = None  # Location A
        self.b = None  # Location B