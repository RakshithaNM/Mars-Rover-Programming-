#We start by importing Libraries and Defining Classes:
#We start by importing a library called logging for keeping track of what the program does.
import logging

# Command Pattern: Command interface and concrete commands
class Command:
    def execute(self, rover):
        pass

class MoveCommand(Command):
    def execute(self, rover):
        rover.move()

class TurnLeftCommand(Command):
    def execute(self, rover):
        rover.turn_left()

class TurnRightCommand(Command):
    def execute(self, rover):
        rover.turn_right()

# Composite Pattern: Component interface
class GridComponent:
    def check_collision(self, x, y):
        pass

#We create a grid where the Rover will move. The grid has a size, and we can place obstacles on it and we have made it to take user input.
class Grid(GridComponent):
    def __init__(self, size_x, size_y):
        self.size_x = size_x
        self.size_y = size_y
        self.obstacles = set()

    def add_obstacle(self, x, y):
        self.obstacles.add((x, y))

    def check_collision(self, x, y):
        return (x, y) in self.obstacles or not (0 <= x < self.size_x and 0 <= y < self.size_y)

# Obstacle class
class Obstacle(GridComponent):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def check_collision(self, x, y):
        return x == self.x and y == self.y

# Rover class
#We define a set of commands that the Rover can follow, like moving forward (M), turning left (L), and turning right (R).
#We define how the Rover behaves. It can move around, turn, and follow a sequence of commands.
#The Rover knows its position (X, Y) and which direction it's facing (North, South, East, West).

class Rover:
    #constructor of rover class
    def __init__(self, x, y, direction, grid):
        self.x = x
        self.y = y
        self.direction = direction
        self.grid = grid

    def move(self):
        new_x, new_y = self.x, self.y
        if self.direction == 'North':
            new_y += 1
        elif self.direction == 'South':
            new_y -= 1
        elif self.direction == 'East':
            new_x += 1
        elif self.direction == 'West':
            new_x -= 1

        if not self.grid.check_collision(new_x, new_y):
            self.x, self.y = new_x, new_y
        else:
            print("Obstacle detected. Rover cannot move.")
 
 #when you call turn_right(), the Rover rotates its direction 90 degrees clockwise.
 #when you call turn_left(), the Rover rotates its direction 90 degrees counterclockwise.
    def turn_left(self):
        if self.direction == 'North':
            self.direction = 'West'
        elif self.direction == 'West':
            self.direction = 'South'
        elif self.direction == 'South':
            self.direction = 'East'
        elif self.direction == 'East':
            self.direction = 'North'

    def turn_right(self):
        if self.direction == 'North':
            self.direction = 'East'
        elif self.direction == 'East':
            self.direction = 'South'
        elif self.direction == 'South':
            self.direction = 'West'
        elif self.direction == 'West':
            self.direction = 'North'


#if command='M':the code executes the MoveCommand().execute(self) line. This means the Rover should move one step forward in the direction it is facing.
#if command='L': This means the Rover should turn left from its current direction.
#if command='R': This means the Rover should turn right from its current direction.

    def execute_commands(self, commands):
        for command in commands:
            if command == 'M':
                MoveCommand().execute(self)
            elif command == 'L':
                TurnLeftCommand().execute(self)
            elif command == 'R':
                TurnRightCommand().execute(self)

    def get_position(self):
        return f"Rover is at ({self.x}, {self.y}) facing {self.direction}. No Obstacles detected."


# Logging configuration
logging.basicConfig(level=logging.INFO)

# User inputs:
#The program asks the user for input: 1)Grid size: The size of the grid where the Rover will move.
#Starting position:It is  Where the Rover begins (X, Y) and which way it's facing.
#Commands: A sequence of commands (e.g., MMRMLM) for the Rover to follow.
#Obstacles: The number of obstacles and their positions on the grid.

#The program creates a grid and sets up the Rover with the provided inputs.It then executes the given commands to move the Rover on the grid while avoiding obstacles.
grid_size_x = int(input("Enter the grid size (X): "))
grid_size_y = int(input("Enter the grid size (Y): "))
start_x = int(input("Enter the starting X position: "))
start_y = int(input("Enter the starting Y position: "))
start_direction = input("Enter the starting direction (North/ South/ East/ West): ").lower()
commands = input("Enter the commands, to tell rover path to move(e.g., 'MMLR'): ").lower()
obstacle_count = int(input("Enter the number of obstacles: "))

obstacles = []
for _ in range(obstacle_count):
    obstacle_x = int(input("Enter obstacle X position: "))
    obstacle_y = int(input("Enter obstacle Y position: "))
    obstacles.append((obstacle_x, obstacle_y))

grid = Grid(grid_size_x, grid_size_y)
for obstacle_x, obstacle_y in obstacles:
    grid.add_obstacle(obstacle_x, obstacle_y)

rover = Rover(start_x, start_y, start_direction, grid)

#Logging and Error Handling: The program logs information about what the Rover does and handles errors if something goes wrong.
try:
    rover.execute_commands(commands)
    final_position = rover.get_position()
    logging.info(final_position)
except Exception as e:
    logging.error(f"Error: {str(e)}")

#Displaying Final output position:Finally, this program displays the Rover's position after following the commands. 
       #This includes its (X, Y) coordinates and the direction it's facing.







