import turtle
import os

INPUT_FILE_PATH = "input.txt"
OUTPUT_FILE_PATH = "output.txt"

# Create a turtle screen
screen = turtle.Screen()

# Set up the screen size and coordinates
screen.setup(width=600, height=600)
screen.setworldcoordinates(0, 0, 10, 10)

#Control variables
direction = 0   # 0 = North, 1 = East, 2 = South, 3 = West

# Create a turtle object
robot = turtle.Turtle()

# Set the turtle's speed and pen size
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
    if not hit_wall(steps):
        robot.forward(steps)

def turn_right(degrees):
    global direction 
    direction =  direction %4 + 1
    robot.right(degrees)

# Function that stops the robot if it hits a wall
def hit_wall(steps):
    if direction == 0:
        if robot.ycor() + steps == 10:
            return True
    elif direction == 1:
        if robot.xcor() + steps == 10:
            return True
    elif direction == 2:
        if robot.ycor() + steps == 0:
            return True
    elif direction == 3:
        if robot.xcor() + steps == 0:
            return True 
    return False



def main():

    os.system("yacc -d robot.y")
    os.system("lex robot.l")
    os.system("cc lex.yy.c y.tab.c -o robot.exe")
    os.system("./build/compiler " + INPUT_FILE_PATH + " > " + OUTPUT_FILE_PATH)
    
    # Call the draw_grid function to draw the grid
    draw_grid()

    robot.speed(4)  

    print(robot.xcor())
    print(robot.ycor())

    print("hola")

    
    move_foward(6)
    turn_right(270)


    move_foward(6)

    # Exit on click
    turtle.exitonclick()



if __name__ == "__main__":
    main()

### Falta hacer bien hitwall para que verifique si las coordenadas más lo que se va a mover
### es mayor a 10 o menor a 0