"""
En este archivo se están haciendo distintos unit tests de la funcion instructions() del archivo robot.py

Esta es la única función que realmente podría generar errores y nos puede preocupar probar varios casos
para ver que esté funcionando correctamente.

Lo anterior porque la función lex_and_yacc() simplemente compila el lex y yacc y estos hacen el trabajo
de traducir el lenguaje a tokens. Si hay errores en las oraciones que pasemos como parámetros en el archivo
test.txt, el lex y yacc se encargarán y darán un error por que las instrucciones no tienen un formato
admitido por el grammar.
"""


import pytest
from robot import *
from unittest.mock import Mock

def test_instructions_move1() -> None:
    file = "tests/test1.asm"

    move_forward_mock = Mock()
    move_forward_mock.call_count = 0

    # Replace the original function with the mock
    instructions(file, move_function = move_forward_mock)
    assert move_forward_mock.call_count == 7

def test_instructions_move2() -> None:
    file = "tests/test2.asm"

    move_forward_mock = Mock()
    move_forward_mock.call_count = 0

    # Replace the original function with the mock
    instructions(file, move_function = move_forward_mock)
    assert move_forward_mock.call_count == 50

def test_instructions_turn1() -> None:
    file = "tests/test3.asm"
    turn_right_mock = Mock()
    turn_right_mock.call_count = 0

    instructions(file, turn_function = turn_right_mock)
    assert turn_right_mock.call_count == 7

def test_instructions_turn2() -> None:
    file = "tests/test4.asm"
    turn_right_mock = Mock()
    turn_right_mock.call_count = 0

    instructions(file, turn_function = turn_right_mock)
    assert turn_right_mock.call_count == 50

def test_instructions_both() -> None:
    file = "tests/test5.asm"
    move_forward_mock = Mock()
    move_forward_mock.call_count = 0
    turn_right_mock = Mock()
    turn_right_mock.call_count = 0

    instructions(file, move_function = move_forward_mock, turn_function = turn_right_mock)
    assert turn_right_mock.call_count + move_forward_mock.call_count == 57