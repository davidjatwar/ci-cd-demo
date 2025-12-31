"""Basic math tests to demonstrate pytest"""

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

class TestMathOperations:
    def test_addition(self):
        assert add(2, 3) == 5
        assert add(-1, 1) == 0
        assert add(0, 0) == 0
    
    def test_subtraction(self):
        assert subtract(5, 3) == 2
        assert subtract(0, 0) == 0
        assert subtract(-1, -1) == 0
    
    def test_addition_with_floats(self):
        result = add(0.1, 0.2)
        assert round(result, 1) == 0.3