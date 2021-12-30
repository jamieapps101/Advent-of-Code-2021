#! /usr/bin/env python3

class Tile:
    def __init__(self,value):
        self.value = value
        self.marked = False

    def mark_if_value_is(self, value) -> bool:
        if self.value == value:
            self.marked = True
        return self.marked

    def is_marked(self) -> bool:
        return self.marked

    def get_value(self) -> int:
        return self.value

class Board:
    def __init__(self,values):
        self.tiles = []
        # values is a list of 5 lists of 5 numbers
        for row in values:
            row_of_tiles = []
            for number in row:
                tile = Tile(number)
                row_of_tiles.append(tile)
            self.tiles.append(row_of_tiles)

    def mark_if_value_present(self,value):
        value_found = False
        for row_index in range(len(self.tiles)):
            for col_index in range(len(self.tiles[0])):
                result = self.tiles[row_index][col_index].mark_if_value_is(value)
                if result == True:
                    value_found = True
        return value_found

    def check_board_complete(self) -> bool:
        # row checker
        for row_index in range(len(self.tiles)):
            # result = all([self.tiles[row_index][col_index].is_marked() for col_index in range(len(self.tiles[0]))])
            # if result:
            #     return True
            marked_tiles = 0
            for col_index in range(len(self.tiles[0])):
                result = self.tiles[row_index][col_index].is_marked()
                if result:
                    marked_tiles += 1
            if marked_tiles==5:
                return True # return true if 5 tiles in this row are marked

        # col checker
        for col_index in range(len(self.tiles[0])):
            marked_tiles = 0
            for row_index in range(len(self.tiles)):
                result = self.tiles[row_index][col_index].is_marked()
                if result:
                    marked_tiles += 1
            if marked_tiles==5:
                return True # return true if 5 tiles in this column are marked
        return False # return false if no cols and rows are found

    def find_score(self, called_number) -> int:
        unmarked_tile_sum = 0
        for row in self.tiles:
            for tile in row:
                if not tile.is_marked():
                    unmarked_tile_sum += tile.get_value()
        return unmarked_tile_sum*called_number

def read_data(data_path: str):
    # first need to read random numbers
    # then need to read all the boards
    random_numbers = []
    boards = []
    # list of instances of the class Board
    with open(data_path) as fp:
        data_buffer = []
        for line_index,line in enumerate(fp):
            if line_index == 0:
                # this is the random numbers
                random_numbers = [int(n) for n in line.split(",")]
            else:
                # probably a board
                if line!="\n":
                    data_buffer.append([int(n) for n in line.split()])
                    if len(data_buffer) == 5:
                        new_board = Board(data_buffer)
                        boards.append(new_board)
                        data_buffer = []

    print(f"Read in {len(random_numbers)} numbers and {len(boards)} boards")

    return random_numbers,boards

def play_all_games(random_numbers,boards):
    for r in random_numbers:
        for board_index in range(len(boards)):
            # if boards[board_index].mark_if_value_present(r):
            #     if boards[board_index].check_board_complete():
            #         return board_index
            # if 0==1 and 6==6 (6==6 will never be evaluated as 1==0 is false and the "and" is shortcutting)
            if boards[board_index].mark_if_value_present(r) and boards[board_index].check_board_complete():
                return r,board_index


def main():
    print("solve me")
    random_numbers,boards = read_data("./day_4/data/input.txt")
    number,winning_board_index = play_all_games(random_numbers,boards)
    winning_score = boards[winning_board_index].find_score(number)
    print(f"winning_score: {winning_score}")



if __name__=="__main__":
    main()