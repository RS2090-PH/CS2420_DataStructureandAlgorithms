"""
File: maze.py
Project 7.9

Determine the solution to a maze problem.
Uses a gid to represent the maze.  This grid is input from
a text file.  Uses a stack-based backtracking algorithm.
"""

from grid import Grid
from arraystack import ArrayStack

def main():
    maze = getMazeFromFile()
    print(maze)
    (startRow, startCol) = findStartPos(maze)
    print("Starting Position: ", startRow, startCol)
    success = getOut(startRow, startCol, maze)
    if success:
        print("Maze solved:")
        print(maze)
    else:
        print("No path out of this maze")

def getMazeFromFile():
    """Reads the maze from a text file and returns a grid that
    represents it."""
    maze_file = open("maze.txt", "r")
    maze_size = maze_file.readline()
    maze_size = maze_size.split()
    maze_size = int(maze_size[0]), int(maze_size[1])
    grid_maze = Grid(maze_size[0], maze_size[1])

    for row in range(0, maze_size[0]):
        line = maze_file.readline()
        if len(line) <= 1:
            break
        else:
            for column in range(0, maze_size[1]):
                grid_maze[row][column] = line[column]

    maze_file.close()
    return grid_maze


def findStartPos(maze):
    """Returns the position of the start symbol in the grid."""

    for row in range(0, maze.getHeight()):
        for column in range(0, maze.getWidth()):
            if maze[row][column] == "P":
                starting_point = (row, column)
                break

    return starting_point


def getOut(row, column, maze):
    """(row,column) is the position of the start symbol in the maze.
    Returns True if the maze can be solved or False otherwise."""
    # States are tuples of coordinates of cells in the grid.
    # Cell has not been visited, so mark it and push adjacent unvisited
    #     positions onto the stack
    position_stack = ArrayStack()
    current_position = (row, column)
    position_stack.push(current_position)

    while len(position_stack) != 0:
        if maze[current_position[0]][current_position[1]] == "T":
            print(maze[current_position[0]][current_position[1]])
            return True
        else:
            north = (current_position[0] - 1, current_position[1])
            east = (current_position[0], current_position[1] + 1)
            south = (current_position[0] + 1, current_position[1])
            west = (current_position[0], current_position[1] - 1)

            try:
                if maze[north[0]][north[1]] == "T":
                    position_stack.push(north)
                    current_position = north
                    continue
                elif maze[north[0]][north[1]] == " ":
                    maze[north[0]][north[1]] = "-"
                    position_stack.push(north)
                    current_position = north
                    continue
            except:
                pass
            try:
                if maze[east[0]][east[1]] == "T":
                    position_stack.push(east)
                    current_position = east
                    continue
                elif maze[east[0]][east[1]] == " ":
                    maze[east[0]][east[1]] = "-"
                    position_stack.push(east)
                    current_position = east
                    continue
            except:
                pass
            try:
                if maze[south[0]][south[1]] == "T":
                    position_stack.push(south)
                    current_position = south
                    continue
                elif maze[south[0]][south[1]] == " ":
                    maze[south[0]][south[1]] = "-"
                    position_stack.push(south)
                    current_position = south
                    continue
            except:
                pass
            try:
                if maze[west[0]][west[1]] == "T":
                    position_stack.push(west)
                    current_position = west
                    continue
                if maze[west[0]][west[1]] == " ":
                    maze[west[0]][west[1]] = "-"
                    position_stack.push(west)
                    current_position = west
                    continue
            except:
                pass

            position_stack.pop()
            current_position = position_stack.peek()
            continue

    return False

if __name__ == "__main__": main()
