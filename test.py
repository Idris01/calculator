from mini_calculator.calculator import Calculator
from unittest import TestCase


class CalculatorTest(TestCase):
  
  def setUp(self) -> None:
    self.calculator = Calculator()

  def test_answer_initializes_to_zero(self):
    self.assertEqual(self.calculator.answer, 0)
  
  def test_add_function(self):
    self.calculator.add(5)  # add 5 to answer
    self.calculator.add()   # double the value in answer
    self.assertEqual(self.calculator.answer,10)
  
  def test_minus_function(self):
    ans = self.calculator.minus(-3)
    self.assertEqual(ans,3.0)

  def test_multiply_function(self):
    self.calculator.add(-4)
    ans = self.calculator.multiply()
    self.assertEqual(ans, 16.0)
  
  def test_divide_function(self):
    self.calculator.add(9)
    ans = self.calculator.divide(3)
    self.assertEqual(ans, 3.0)
  
  def test_root_funtion(self):
    self.calculator.add(16)
    ans = self.calculator.root()
    self.assertEqual(ans,4.0)