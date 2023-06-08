# Robot-Language-Compiler

This is the README file for the Robot-Language-Compiler project. Below, you will find a description of the project, the constraints of the robot, and the grammar used in the programming language.

## Project Description

The Robot-Language-Compiler project focuses on developing a compiler for a programming language designed to control a robot on a two-dimensional field. The robot has two supported instructions: MOV (move) and TURN. The field on which the robot will move is a 2-D square matrix of 10 blocks implemented in Python.

The compiler ensures that the instructions are valid and polite, and it displays an error message if the robot goes beyond the boundaries of the matrix.

## Robot Constraints

    Only 2 supported instructions: MOVE and TURN.
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

    "Robot move 2 blocks"
    "Robot moves 2 blocks."
    "Robot moves 2 blocks quickly."
    "Move 2 blocks right now."
    "Robot 2 blocks moves."
    "robot, please move 2 blocks and turn 180 degrees"
    "Moves Robot 2 blocks and turn 89 degrees."
    "Move 2 blocks ahead, then turn 90 degrees."
    "Robot, please move 2 blocks quickly and then turn."

## Grammar

Below is the grammar used in the robot programming language:

```<sentences>      ::= <sentence>```
                   ```| <sentences> EOL <sentence>```

```<sentence>       ::= <subject> <polite_word> <instructions>```

```<instructions>   ::= <instruction>```
                   ```| <instruction> <union> <instructions>```

```<union>          ::= COMMA AND THEN```
                   ```| COMMA AND```
                   ```| COMMA THEN```
                   ```| COMMA```
                   ```| AND THEN```
                   ```| THEN```
                   ```| AND```

```<instruction>    ::= <move_action> <length> <move_unit> <move_adverb>```
                   ```| <turn_action> <length> <turn_unit> <turn_adverb>```
                   ```| <move_action> <length> <move_unit>```
                   ```| <turn_action> <length> <turn_unit>```

```<length>         ::= NUMBER```
                   ```| DEGREES```

```<subject>        ::= Robot```
                    ```| Rob```
                    ```| Turtle```

```<polite_word>    ::= please```
                    ```| kindly```

```<move_action>    ::= move```
                   ```| advance```
                   ```| travel```
                   ```| go```
                   ```| proceed```

```<turn_action>    ::= turn```
                   ```| rotate```
                   ```| spin```
                   ```| pivot```
                   ```| twist```
                   ```| shift```

```<move_unit>      ::= blocks```
                   ```| block```
                   ```| steps```
                   ```| step```
                   ```| units```
                   ```| unit```
                   ```| paces```
                   ```| pace```
                   ```| strides```
                   ```| stride```

```<turn_unit>      ::= degrees```

```<move_adverb>    ::= ahead```
                   ```| forward```
                   ```| onward```
                   ```| straight```

```<turn_adverb>    ::= to the right```
                   ```| right```
                   ```| clockwise```
                   ```| to the east```
                   ```| toward the right```

```<NUMBER>         ::= 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9```

```<EOL>            ::= \n```

## Model
<img src="graph.gif" alt="Gif de gráfica de Python" width="600">

