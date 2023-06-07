# Robot-Language-Compiler

This is the README file for the Robot-Language-Compiler project. Below, you will find a description of the project, the constraints of the robot, and the grammar used in the programming language.

## Project Description

The Robot-Language-Compiler project focuses on developing a compiler for a programming language designed to control a robot on a two-dimensional field. The robot has two supported instructions: MOV (move) and TURN. The field on which the robot will move is a 2-D square matrix of 10 blocks implemented in Python.

The compiler ensures that the instructions are valid and polite, and it displays an error message if the robot goes beyond the boundaries of the matrix.

## Robot Constraints

    Only 2 supported instructions: MOV and TURN.
    The field on which the robot moves is a 2-D square matrix of 10 blocks implemented in Python.
    If the instruction leads the robot out of the boundaries of the matrix, the CPU should return an illegal instruction error.

## Polite Programming Language

The programming language used to control the robot must be polite and follow certain grammar rules. Here are some examples of valid and invalid sentences:
### Examples of valid sentences:

    "Robot, please move 2 blocks ahead."
    "Robot, please move 3 blocks ahead and then turn 90 degrees. Then, move 2 blocks."
    "Robot, kindly turn 90 degrees and then move 2 steps, and then turn 270 degrees to the right."
    "Robot, please move 3 blocks ahead, then turn 180 degrees to the right, and finally move 2 steps."
    "Please kindly turn 270 degrees to the right, then move 5 blocks ahead and turn 90 degrees."

### Examples of invalid sentences:

    "Robot moves 2 blocks."
    "Robot moves 2 blocks quickly."
    "Move 2 blocks right now."
    "Robot 2 blocks moves."
    "Moves Robot 2 blocks and turn 89 degrees."
    "Move 2 blocks ahead, then turn 90 degrees."
    "Robot, please move 2 blocks quickly and then turn."

## Grammar

Below is the grammar used in the robot programming language:

```<SENTENCES>     ::= <SENTENCE> <SENTENCES> | <SENTENCE>```

```<SENTENCE>      ::= <SUBJECT> <POLITE WORD> <INSTRUCTIONS> | <POLITE WORD> <SUBJECT> <INSTRUCTIONS>```

```<INSTRUCTIONS>  ::= <INSTRUCTION> | <INSTRUCTION> <UNION> <INSTRUCTIONS>```

```<INSTRUCTION>   ::= <MOVE_ACTION> <NUMBER> <MOVE_UNIT> <MOVE_ADVERB> | <TURN_ACTION> <DEGREES> <TURN_UNIT> <TURN_ADVERB> | <MOVE_ACTION> <NUMBER> <MOVE_UNIT> | <TURN_ACTION> <DEGREES> <TURN_UNIT>```

```<SUBJECT>       ::= Robot```

```<POLITE WORD>   ::= please```

```<COMMA>         ::= ,```

```<AND>           ::= and```

```<THEN>          ::= then```

```<UNION>         ::= COMMA AND THEN | COMMA AND | COMMA THEN | COMMA | AND THEN | THEN | AND```

```<NUMBER>        ::= 1|2|3|4|5|6|7|8|9```

```<DEGREES>       ::= 90|180|270|360```

```<MOVE_ACTION>   ::= move | advance | travel | go | proceed```

```<TURN_ACTION>   ::= turn | rotate | spin | pivot | twist | shift```

```<MOVE_UNIT>     ::= blocks | steps```

```<TURN_UNIT>     ::= degrees```

```<MOVE_ADVERB>   ::= ahead```

```<TURN_ADVERB>   ::= to the right | clockwise```

## Usage

import turtle
import os

INPUT_FILE_PATH = "test.txt"
OUTPUT_FILE_PATH = "output.asm"

Create a turtle screen
screen = turtle.Screen()

Set up the screen size and coordinates
screen.setup(width=600, height=600)
screen.setworldcoordinates(0, 0, 10, 10)

Control variables
direction = 0   # 0 = North, 1 = East, 2 = South, 3 = West

Create a turtle object
robot = turtle.Turtle()
robot.speed(0)
robot.pensize(1)
robot.shape("turtle")
robot.color("green")

def draw_grid():
    for x in range(11):
        robot.penup()
        robot.goto(x, 0)
        robot.pendown()
        robot.goto(x, 10)
        
        robot.penup()
        robot.goto(0, x)
        robot.pendown()
        robot.goto(10, x)
        #erase grid turtle
        robot.penup()
        robot.goto(0.5, 0.5)

def move_foward(steps):
    print(robot.xcor(), robot.ycor())
    robot.forward(steps)
    if off_the_grid(0):
        print("Off the grid")
    
def turn_right(degrees):
    global direction   
    direction =  (direction + degrees//90)%4
    robot.right(degrees)

def off_the_grid(steps):
    if direction == 0:
        if robot.xcor() + steps < 10:
            return False
    elif direction == 1:
        if robot.ycor() + steps > 0:
            return False
    elif direction == 2:
        if robot.xcor() + steps > 0:
            return False
    elif direction == 3:
        if robot.ycor() + steps < 10:
            return False 
    return True

def lex_and_yacc():
    os.system("yacc -d robot.y")
    os.system("lex robot.l")
    os.system("cc lex.yy.c y.tab.c -o robot.exe")
    os.system("./robot.exe " + INPUT_FILE_PATH + " > " + OUTPUT_FILE_PATH)

def instructions():
    actions = {"MOV": move_foward, "TURN": turn_right}
    read_file = open(OUTPUT_FILE_PATH, "r")
    for line in read_file:
        if line[0] == "M":
            actions[line[0:3]](int(line[4:-1]))
        elif line[0] == "T":
            actions[line[0:4]](int(line[5:-1]))
        print(line)
    read_file.close()

def main():
    Compile lex and yacc and get output file
    lex_and_yacc()
    Call the draw_grid function to draw the grid
    draw_grid()
    robot.speed(2)  
    instructions()
    print(robot.xcor(), robot.ycor())
    Exit on click
    turtle.exitonclick()

if __name__ == "__main__":
    main()

# Example code to move the turtle
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.done()

