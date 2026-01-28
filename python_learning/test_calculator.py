"""
create venv : source /home/raj/Desktop/fastAPI/fastapi-env/bin/activate
install : pip install pytest
run : pytest filename.py

this pytest will give you test results either pass or fail. 
pytest is used to automate/reduce work of developer as we don't need to write multiple try/except blocks

assert is used instead of try: except assertion_error: .......
"""

import calculator

def test_add():
    assert calculator.add(2, 3) == 5
    assert calculator.add(2, 2) == 4

def test_sub():
    assert calculator.sub(2, 2) == 0
    assert calculator.sub(1, 5) == -4

def test_square():
    assert calculator.square(5) == 25
    assert calculator.square(2) == 4
    assert calculator.square(-2) == 4
    assert calculator.square(0) == 0

def test_mul():
    assert calculator.mul(2, 2) == 4
    assert calculator.mul(2, 4) == 8
    assert calculator.mul(2, 8) == 16
    assert calculator.mul(6, 4) == 24

def test_div():
    assert calculator.div(2, 2) == 1
    assert calculator.div(1, 5) == 0.2
