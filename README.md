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

    Robot kindly turn 270 degrees and then move 7 steps, and then turn 90 degrees to the right
    Robot please move 9 steps 
    Please Robot turn 90 degrees to the right and move 1 blocks and then turn 90 degrees, then move 5 steps 
    Robot kindly turn 270 degrees clockwise and move 4 steps ahead and move 2 steps ahead


### Examples of invalid sentences:

    Robot move 2 blocks
    Robot moves 2 blocks.
    Robot moves 2 blocks quickly.
    Move 2 blocks right now.
    Robot 2 blocks moves.
    robot, please move 2 blocks and turn 180 degrees
    Moves Robot 2 blocks and turn 89 degrees.
    Move 2 blocks ahead, then turn 90 degrees.
    Robot, please move 2 blocks quickly and then turn.

## Grammar

Below is the grammar used in the robot programming language:

    <sentences>: <sentence>                 
         | <sentences> EOL <sentences>
         | <sentences> EOL
         ;

        <sentence>: <SUBJECT> <POLITE_WORD> <instructions>	
                | <POLITE_WORD> <SUBJECT> <instructions>
        ;

        <instructions>: <instruction >
         | <instruction> <union> <instructions>
        ;

        <union>: COMMA AND THEN 
         | COMMA AND
         | COMMA THEN
         | COMMA
         | AND THEN
         | THEN
         | AND


        <instruction>: <MOVE_ACTION> <lenght_number> <MOVE_UNIT> <MOVE_ADVERB>   
            | <MOVE_ACTION>  <lenght_number> <MOVE_UNIT>                      
            | <TURN_ACTION> <lenght_degrees> <TURN_UNIT> <TURN_ADVERB>          
            | <TURN_ACTION> <lenght_degrees> <TURN_UNIT>                    
        ;

        lenght_number: NUMBER 
        ;
        
        lenght_degrees: DEGREES;

        Robot |
        Rob |
        Turtle {return SUBJECT;}

        please |
        kindly |
        Please |
        Kindly {return POLITE_WORD;}

        ,            { return COMMA; }
        and          { return AND; }
        then         { return THEN; }


        NUMBER:[0-9]    
        DEGREES: (90|180|270|360)   

        MOVE_ACTION
        move |
        advance |
        travel |
        go |
        proceed				

        TURN_ACTION:
        turn |
        rotate |
        spin |
        pivot |
        twist |
        shift 	{

        MOVE_UNIT:
        blocks |
        block |
        steps |
        step |
        units |
        unit |
        paces |
        pace |
        strides |
        stride 

        TURN_UNIT:
        degrees 

        MOVE_ADVERB:
        ahead |
        forward |
        onward |
        straight 

        TURN_ADVERB: 
        "to the right" |
        right |
        clockwise |
        "to the east" |
        "toward the right" 

        EOL: " "

## Graphviz
<img src="graphviz_compiler.png" alt="Imagen del diagrama" width="1200">

## Model
<img src="graph.gif" alt="Gif de gráfica de Python" width="600">

