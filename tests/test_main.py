# -*- coding: utf-8 -*-
from calculator.main import Calc 

def test_add_two_numbers():
    calculator = Calc() #Instantation
    
    result = calculator.add(2, 3)
    
    assert result == 5
    
    
def test_add_three_numbers():
    calculator = Calc() #Instantation
    
    result = calculator.add(2, 3, 4)
    
    assert result == 9
    
def test_add_many_numbers():
    numbers = range(1,100)
    calculator = Calc() #Instantation
    
    result = calculator.add(*numbers)
    
    assert result == 4950
