import time


class sudoku_engine:

    def __init__(self):
        self.map = []
        self.solution = None

    def initalisePreset(self) -> None:
        for i in range(6):
            self.map.append(self.row_parse(input()))

    def row_parse(self, row_input : str) -> [int]:
        row = row_input.split(" ")
        map_row = []
        for val in row:
            if int(val) == 0:
                map_row.append(None)
            else:
                map_row.append(int(val))
        return map_row

    def solve(self, i : int, j : int):
        if self.solution: return

        if i == 6 :
            # print(self.map, self.checkMap())
            if self.checkMap():
                self.solution = [row[:] for row in self.map]
            return

        if self.map[i][j] == None:
            # print(i, j)
            for x in range(1, 7):
                if x not in self.getRow(i) and x not in self.getCol(j):
                    self.map[i][j] = x
                    if j >= 5:
                        self.solve(i + 1, 0)
                    else:
                        self.solve(i, j + 1)
                    self.map[i][j] = None
        else:
            if j >= 5:
                self.solve(i + 1, 0)
            else:
                self.solve(i, j + 1)

    def checkMap(self) -> bool:
        for i in range(6):
            if not self.check(self.getSector(i+1)) or not self.check(self.getRow(i)) or not self.check(self.getCol(i)):
                # print(self.getSector(i+1), self.getRow(i), self.getCol(i))
                return False
        return True

    def check(self, sequence : [int]) -> bool:
        sequence = [i for i in sequence if i is not None]
        return sorted(sequence) == list(range(1,7))

    def getSector(self, sector : int) -> [int]:
        ## sectors go from top to bottom, left to right, 1 to 6
        row_offset = ((sector - 1) // 2) * 2
        col_offset = 3 if sector % 2 == 0 else 0
        sector = []
        for i in range(3):
            sector.append(self.map[0+row_offset][i+col_offset])
            sector.append(self.map[1+row_offset][i+col_offset])

        return sector

    def getRow(self, row : int) -> [int]:
        return self.map[row]

    def getCol(self, col : int) -> [int]:
        col = [self.map[i][col] for i in range(len(self.map))]
        return col

def main():
    test = sudoku_engine()
    test.initalisePreset()
    test.solve(0, 0)
    # print(test.map)
    print(test.solution)

main()