import sys


class Ship:
    def __init__(self, size):
        self.size = size
        self.hits = 0
        self.positions = []

    def place(self, positions):
        self.positions = positions

    def hit(self):
        self.hits += 1
        return self.is_sunk()

    def is_sunk(self):
        return self.hits >= self.size


class Battleship(Ship):
    def __init__(self):
        super().__init__(4)


class Cruiser(Ship):
    def __init__(self):
        super().__init__(3)


class Destroyer(Ship):
    def __init__(self):
        super().__init__(2)


class Submarine(Ship):
    def __init__(self):
        super().__init__(1)


class Board:
    def __init__(self, size=10, grid=None):
        self.size = size
        if grid is not None:
            self.grid = grid
        else:
            self.grid = [[' ' for _ in range(size)] for _ in range(size)]
        self.ships = []

    def is_valid_position(self, positions):
        for x, y in positions:
            if x < 0 or y < 0 or x >= self.size or y >= self.size:
                return False
            if self.grid[x][y] != ' ':
                return False
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    if 0 <= x + dx < self.size and 0 <= y + dy < self.size:
                        if self.grid[x + dx][y + dy] != ' ':
                            return False
        return True

    def place_ship(self, ship, start_row, start_col, horizontal=True):
        positions = []
        if horizontal and start_col + ship.size > self.size:
            return False
        if not horizontal and start_row + ship.size > self.size:
            return False

        for i in range(ship.size):
            if horizontal:
                positions.append((start_row, start_col + i))
            else:
                positions.append((start_row + i, start_col))

        if self.is_valid_position(positions):
            for x, y in positions:
                self.grid[x][y] = 'S'
            ship.place(positions)
            self.ships.append(ship)
            return True
        return False

    def receive_shot(self, row, col):
        if not (0 <= row < self.size and 0 <= col < self.size):
            return False
        if self.grid[row][col] in ['X', 'O']:
            return False

        if self.grid[row][col] == 'S':
            self.grid[row][col] = 'X'
            for ship in self.ships:
                if (row, col) in ship.positions:
                    ship.hit()
                    return True
        else:
            self.grid[row][col] = 'O'
        return False

    # def display(self):
    #     return '\n'.join([''.join(row) for row in self.grid])
    #
    # def display_hidden(self):
    #     return '\n'.join([''.join([' ' if cell == 'S' else cell for cell in row]) for row in self.grid])

    def display(self):
        return [row[:] for row in self.grid]

    def display_hidden(self):
        return [[' ' if cell == 'S' else cell for cell in row] for row in self.grid]

    def all_ships_sunk(self):
        return all(ship.is_sunk() for ship in self.ships)


exec(sys.stdin.read())
