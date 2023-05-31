# Robot-Language-Compiler

The Robot has the next constraints

* Only 2 supported instructions:
    * MOV
    * TURN <either: {90,180,270,360}>

* The field where the robot will move is a 2-D square matrix of 10 blocks (PYTHON)
* If the instruction leads the robot out of the boundaries of the matrix, the CPU should return an illegal instruction error.  (PYTHON)
* The programing language must be polite:


    * Examples of valid sentences:
        * Robot please move 2 blocks ahead
        * Robot please move 3 blocks ahead and then turn 90 degrees, then move 2 blocks
        * Robot kindly turn 90 degrees and then move 2 steps, and then turn 270 degrees to the right



    * Examples of invalid sentences:
        * Robot moves 2 blocks
        * Robot moves 2 blocks quickly
        * Move 2 blocks right now
        * Robot 2 blocks moves
        * Moves Robot 2 blocks and turn 89 degrees


GRAMMAR:

	<SENTENCES> => <SENTENCE> <SENTENCES> | <SENTENCE>			//No hay problema si es una o varias sentencias que empiecen con “Robot”
	<SENTENCE> => <SUBJECT> <POLITE WORD> <INSTRUCTIONS>
				      |<POLITE WORD> <SUBJECT> <INSTRUCTIONS>		//Esto esta bien
					
	<INSTRUCTIONS> => <INSTRUCTION>
						| <INSTRUCTION> <UNION> <INSTRUCTIONS> 


	<INSTRUCTION> =>  <MOVE_ACTION> <NUMBER> <MOVE_UNIT> <MOVE_ADVERB>
						|<TURN_ACTION> <DEGREES><TURN_UNIT> <TURN_ADVERB>
						| <MOVE_ACTION> <NUMBER> <MOVE_UNIT>
						|<TURN_ACTION> <DEGREES><TURN_UNIT>

	<SUBJECT> => Robot
	<POLITE WORD> => please

	<COMMA> => ,    //Aquí hay un problema de ambigüedad que corregir
	<AND> => and	//Es más fácil acortar la definición de lo que se va a permitir
	<THEN> => then
	<UNION> =>	 COMMA AND TEN
				| COMMA AND
				| COMMA THEN
				| COMMA
				| AND THEN
				| THEN
				| AND

	<NUMBER> => 1|2|3|4|5|6|7|8|9
	<DEGREES> =>	90|180|270|360

	<MOVE_ACTION> => move | advance | travel | go | proceed
	<TURN_ACTION> => turn | rotate | spin | pivot | twist | shift 

	<MOVE_UNIT> => blocks | steps
	<TURN_UNIT> => degrees

	<MOVE_ADVERB> => ahead
	<TURN_ADVERB> => to the right | clockwise