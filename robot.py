import turtle
import os

INPUT_FILE_PATH = "test.txt"
OUTPUT_FILE_PATH = "output.asm"

# Create a turtle screen
screen = turtle.Screen()

# Set up the screen size and coordinates
screen.setup(width=600, height=600)
screen.setworldcoordinates(0, 0, 10, 10)

#Control variables
direction = 0   # 0 = North, 1 = East, 2 = South, 3 = West

# Create a turtle object
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
    # Compile lex and yacc and get output file
    lex_and_yacc()
    # Call the draw_grid function to draw the grid
    draw_grid()
    robot.speed(2)  
    instructions()
    print(robot.xcor(), robot.ycor())
    # Exit on click
    turtle.exitonclick()

if __name__ == "__main__":
    main()
