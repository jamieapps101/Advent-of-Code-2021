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


def test_board():
    board_data = [
        [13,65,84,25,51],
        [ 4, 9,14,93,51],
        [52,50, 6,34,55],
        [70,64,78,65,95],
        [12,22,41,60,71]
    ]
    board = Board(board_data)
    assert(not board.check_board_complete())

    random_data = [ 4, 9,14,93,51]
    for r in random_data:
        board.mark_if_value_present(r)
    assert(board.check_board_complete())

    board = Board(board_data)
    random_data = [ 65, 9,50,64,22]
    for c in random_data:
        board.mark_if_value_present(c)
    assert(board.check_board_complete())

    print("All working")

def read_data(data_path: str):
    # first need to read random numbers
    # then need to read all the boards
    random_numbers = []
    boards = []
    # list of instances of the class Board
    with open(data_path) as fp:
        for line_index,line in enumerate(fp):
            if line_index == 0:
                # this is the random numbers
                random_numbers = [int(n) for n in line.split(",")]
            else:
                # probably a board
                pass

    return random_numbers,boards


def main():
    print("solve me")
    test_board()



if __name__=="__main__":
    main()