import random
from colorama import init, Fore
from colorama import Back

init(autoreset=True)


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

    def __str__(self):
        return f'{self.__class__.__name__} ({self.size}), потоплен: {self.is_sunk()}'

    def __repr__(self):
        return self.__str__()


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
            print(Fore.RED + '-- Выстрел за пределы доски-- ')
            return False
        if self.grid[row][col] == 'S':
            self.grid[row][col] = 'X'
            for ship in self.ships:
                if (row, col) in ship.positions:
                    print(Fore.GREEN + '- Попал! -')
                    if ship.hit():
                        print(Fore.BLUE + '-- Корабль потоплен! --')
                    return True
        else:
            self.grid[row][col] = 'O'
        print(Fore.RED + '- Промах... -')
        return False

    def display(self):
        strokes = 'abcdefghijklmnopqrstuvwxyz'
        return f'\n  {"━ " * (self.size - 1)}━\n'.join(
            [f'{strokes[i]}:' + '┃'.join(row) for i, row in enumerate(self.grid)])

    def display_hidden(self):
        return f'\n  {"━ " * (self.size - 1)}━\n'.join(
            ['┃'.join([' ' if cell == 'S' else cell for cell in row]) for row in self.grid])

    def all_ships_sunk(self):
        if all(ship.is_sunk() for ship in self.ships):
            print(Back.BLACK + Fore.GREEN + '<-- Победа! -->')
            return True
        return False

    def place_all_ships(self):
        ship_classes = [Battleship, Cruiser, Destroyer, Submarine]
        for ShipClass in ship_classes:
            ship = ShipClass()
            while True:
                row = random.randint(0, self.size - 1)
                col = random.randint(0, self.size - 1)
                horizontal = random.choice([True, False])
                if self.place_ship(ship, row, col, horizontal):
                    break


class Game:
    def __init__(self, size=10):
        self.board = Board(size)

    def play(self):
        self.board.place_all_ships()

        while not self.board.all_ships_sunk():
            # for ship in self.board.ships:
            #     print(ship)
            # print(self.board.display_hidden())
            print('  ' + ' '.join([f'{str(i)}' for i in range(1, self.board.size + 1)]))
            print(self.board.display())
            try:
                row = int(input(Fore.YELLOW + 'Введи строку ' + f'(1 - {self.board.size}): ')) - 1
                col = int(input(Fore.LIGHTYELLOW_EX + 'Введи столбец ' + f'(1 - {self.board.size}): ')) - 1
            except ValueError:
                print('Введи число')
                continue
            self.board.receive_shot(row, col)


if __name__ == '__main__':
    game = Game()
    game.play()