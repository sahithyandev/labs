# maze is denoted using a matrix
# cells are denoted by numbers
# maze is traversed through by a "walker"
# if a walker can go north the cell will include 0b1000
# and other directions have a dedicated bit position

from typing import Tuple, Generic,TypeVar, Dict

T = TypeVar("T")

class Stack(Generic[T]):
    def __init__(self) -> None:
        self.buffer: list[T] = []
    def push(self,item: T):
        self.buffer.append(item)
        pass
    def pop(self) -> T | None:
        if len(self.buffer) == 0:
            return

        return self.buffer.pop()
    def peek(self) -> T | None:
        if len(self.buffer) == 0:
            return

        return self.buffer[- 1]

    def get_all(self):
        return self.buffer
    def includes(self, item: T) -> bool:
        return item in self.buffer

class Maze:
    DIRECTION_NORTH =   0b01000
    DIRECTION_EAST =    0b00100
    DIRECTION_SOUTH =   0b00010
    DIRECTION_WEST =    0b00001
    ALREADY_VISITED_BLOCK = 0b10000

    def __init__(self, maze_data: list[list[int]], starting_position: Tuple["int", "int"], ending_position: Tuple["int", "int"]) -> None:
        self.maze = maze_data
        self.walker_position = starting_position
        self.target_position = ending_position
        self.checkpoints = Stack[Tuple["int", "int"]]()

    def update_cell_value(self, cell_position: Tuple["int", "int"], value: int):
        self.maze[cell_position[0]][cell_position[1]] = value

    def get_cell_value(self, position: Tuple["int", "int"]):
        return self.maze[position[0]][position[1]]

    def possible_next_cells(self) -> list[Tuple["int", "int"]]:
        pos = self.walker_position
        current_cell_value = self.maze[pos[0]][pos[1]]
        can_go_north = current_cell_value & Maze.DIRECTION_NORTH == Maze.DIRECTION_NORTH
        can_go_south = current_cell_value & Maze.DIRECTION_SOUTH == Maze.DIRECTION_SOUTH
        can_go_east = current_cell_value & Maze.DIRECTION_EAST == Maze.DIRECTION_EAST
        can_go_west = current_cell_value & Maze.DIRECTION_WEST == Maze.DIRECTION_WEST

        possibilities = []
        if can_go_north:
            expected_cell = (pos[0] -1, pos[1])
            if pos[0] != 0 and self.get_cell_value(expected_cell) & Maze.ALREADY_VISITED_BLOCK == 0:
                possibilities.append("north")
                possibilities.append(expected_cell)
        if can_go_east:
            expected_cell = (pos[0], pos[1] + 1)
            if pos[1] != len(self.maze[0]) - 1 and self.get_cell_value(expected_cell) & Maze.ALREADY_VISITED_BLOCK == 0:
                possibilities.append("east")
                possibilities.append(expected_cell)
        if can_go_south:
            expected_cell = (pos[0] +1, pos[1])
            if pos[0] != len(self.maze) - 1 and self.get_cell_value(expected_cell) & Maze.ALREADY_VISITED_BLOCK == 0:
                possibilities.append("south")
                possibilities.append(expected_cell)
        if can_go_west:
            expected_cell = (pos[0], pos[1]-1)
            if pos[1]!= 0 and self.get_cell_value(expected_cell) & Maze.ALREADY_VISITED_BLOCK == 0:
                possibilities.append("west")
                possibilities.append(expected_cell)

        return possibilities

    def start_walking(self):
        print(f"Start at ( {self.walker_position[0]} , {self.walker_position[1]} )")

        msg = []
        while self.walker_position != self.target_position:
            next_cells = self.possible_next_cells()
            self.update_cell_value(self.walker_position,  self.get_cell_value(self.walker_position) | 0b10000)

            if len(next_cells) == 0:
                msg.append(f"Stuck at ( {self.walker_position[0]} , {self.walker_position[1]} )")

                last_checkpoint = self.checkpoints.pop()
                if last_checkpoint == None:
                    return
                self.walker_position = last_checkpoint

                # self.update_cell_value(self.walker_position,  self.get_cell_value(self.walker_position) | 0b01111)
                print(" ".join(msg))
                msg.clear()
                print(f"Back to ( {self.walker_position[0]} , {self.walker_position[1]} )")
            else:
                self.checkpoints.push(self.walker_position)
                self.walker_position = next_cells[1]
                msg.append(str(next_cells[0]).capitalize())

        msg.append(f"Leaving at ( {self.walker_position[0]} , {self.walker_position[1]} )")
        print(" ".join(msg))
        msg.clear()


maze = Maze([
    [6, 5, 7, 1, 6,5,3,4,7,5,1,6,5,3],
    [10,4,13,1,10,4,13,7,11,4,5,13,1,10],
    [14,7,1,6,9,6,1,10,12,5,5,3,6,11],
    [10,10,6,15,5,9,4,13,1,6,5,9,10,10],
    [10,10,10,10,6,5,5,3,6,9,6,5,9,10],
    [10,10,8,10,10,6,1,10,10,6,11,6,3,8],
    [8,14,3,10,10,10,6,13,9,10,10,10,10,2],
    [2,10,10,10,10,10,14,1,2,8,14,9,10,10],
    [10,8,14,9,10,12,9,6,9,2,10,6,13,11],
    [14,5,13,1,12,5,3,12,5,13,11,10,2,10],
    [8,2,6,5,5,3,14,3,6,5,9,10,10,10],
    [6,11,10,6,3,12,9,10,12,5,3,10,12,13],
    [10,12,9,10,12,7,1,8,6,5,9,12,1,2],
    [12,5,5,13,1,12,5,5,13,5,5,5,5,9],
], (2,0), (11,13))

maze.start_walking()
