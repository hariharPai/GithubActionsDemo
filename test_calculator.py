import unittest
import subprocess

class TestCalculator(unittest.TestCase):
    def test_addition(self):
        result = subprocess.check_output(['python', 'calculator.py', 'add', '5', '3'])
        print (result)
        print (type(result))
        self.assertEqual(float(result.strip()), 8.0)

    def test_subtraction(self):
        result = subprocess.check_output(['python', 'calculator.py', 'subtract', '5', '3'])
        self.assertEqual(float(result.strip()), 2.0)

    def test_multiplication(self):
        result = subprocess.check_output(['python', 'calculator.py', 'multiply', '5', '3'])
        self.assertEqual(float(result.strip()), 15.0)

    def test_division(self):
        result = subprocess.check_output(['python', 'calculator.py', 'divide', '6', '3'])
        self.assertEqual(float(result.strip()), 2.0)

    def test_division(self):
        result = subprocess.check_output(['python', 'calculator.py', 'divide', '9', '3'])
        self.assertEqual(float(result.strip()), 3.0)

if __name__ == '__main__':
    unittest.main()
