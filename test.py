import unittest
from Calculator import Calculator


class TestCalculator(unittest.TestCase):

    # Create an instance of the calculator that can be used in all tests
    @classmethod
    def setUpClass(self):
        print('start')
        self.c = Calculator()

    @classmethod
    def tearDownClass(self):
        print('end')

    # Write test methods inputs and operations
    def test_add(self):
        self.c.add_to_expression("1")
        self.c.add_to_expression("2")
        self.c.append_operator("+")
        self.c.add_to_expression("2")
        self.c.evaluate()

        self.assertEqual(self.c.current_expression, "14", msg=None)

        self.c.clear()

    def test_multiply(self):
        self.c.add_to_expression("1")
        self.c.add_to_expression("0")
        self.c.append_operator("*")
        self.c.add_to_expression("5")
        self.c.evaluate()

        self.assertEqual(self.c.current_expression, "50", msg=None) 

        self.c.clear()

    def test_divide(self):
        self.c.add_to_expression("1")
        self.c.add_to_expression("0")
        self.c.append_operator("/")
        self.c.add_to_expression("5")
        self.c.evaluate()

        self.assertEqual(self.c.current_expression, "2", msg=None) 

        self.c.clear()

    def test_square(self):
        self.c.add_to_expression("2")
        self.c.square()

        self.assertEqual(self.c.current_expression, "4", msg=None)

        self.c.backspace()

    def test_squareroot(self):
        self.c.add_to_expression("4")
        self.c.sqrt()

        self.assertEqual(self.c.current_expression, "2.0", msg=None)

        self.c.backspace()
        self.c.backspace()
        self.c.backspace()

    def test_subtract(self):
        self.c.add_to_expression("5")
        self.c.add_to_expression("0")
        self.c.append_operator("-")
        self.c.add_to_expression("10")
        self.c.evaluate()

        self.assertEqual(self.c.current_expression, "40", msg=None)

        self.c.clear()

    def test_decimal(self):
        self.c.add_to_expression("1")
        self.c.add_to_expression(".")
        self.c.add_to_expression("5")
        self.c.append_operator("*")
        self.c.add_to_expression("2")
        self.c.evaluate()

        self.assertEqual(self.c.current_expression, "3", msg=None)

        self.c.clear()

    def test_multiple_operations(self):
        self.c.add_to_expression("1")
        self.c.append_operator("+")
        self.c.add_to_expression("2")
        self.c.add_to_expression("1")
        self.c.append_operator("-")
        self.c.add_to_expression("10")
        self.c.append_operator("/")
        self.c.add_to_expression("2")
        self.c.append_operator("*")
        self.c.add_to_expression("1")
        self.c.evaluate()

        self.assertEqual(self.c.current_expression, "17", msg=None)

        self.c.clear()

    def test_Operation_Error(self):
        self.c.add_to_expression("5")
        self.c.append_operator("+")
        self.c.append_operator("/")
        self.c.add_to_expression("1")
        self.c.evaluate()

        self.assertEqual(self.c.current_expression, "Math Error", msg=None)

        self.c.clear()
    
    def test_divisionByzero_Error(self):
        self.c.add_to_expression("5")
        self.c.append_operator("/")
        self.c.add_to_expression("0")
        self.c.evaluate()

        self.assertEqual(self.c.current_expression, "Math Error", msg=None)

        self.c.clear()

    def test_backspace(self):
        self.c.add_to_expression("5")
        self.c.add_to_expression("4")
        self.c.add_to_expression("3")
        self.c.add_to_expression("2")
        self.c.add_to_expression("1")

        self.c.backspace()
        self.c.backspace()
        self.c.backspace()
        self.c.backspace()
        self.c.backspace()

        self.assertEqual(self.c.current_expression, "", msg=None)

    def test_backspace_again(self):
        self.c.add_to_expression("5")
        self.c.append_operator("+")
        self.c.add_to_expression("4")
        self.c.append_operator("-")
        self.c.add_to_expression("3")
        self.c.append_operator("*")
        self.c.add_to_expression("2")

        self.c.backspace()
        self.c.backspace()
        self.c.backspace()
        self.c.backspace()
        self.c.backspace()
        self.c.backspace()
        self.c.backspace()

        self.assertEqual(self.c.current_expression, "", msg=None)

    def test_operators(self):
        self.c.append_operator("-")
        self.c.append_operator("+")
        self.c.append_operator("*")
        self.c.append_operator("/")

        self.assertEqual(self.c.total_expression, "- + * /", msg=None)

        self.c.clear()

    def test_negative_output(self):
        self.c.add_to_expression("4")
        self.c.append_operator("*")
        self.c.add_to_expression("4")
        self.c.append_operator("*")
        self.c.add_to_expression("4")
        self.c.append_operator("*")
        self.c.append_operator("-")
        self.c.add_to_expression("3")
        self.c.evaluate()

        self.assertEqual(self.c.current_expression, "-192", msg=None)

        self.c.backspace()
        self.c.backspace()

    def  test_SqrtAndSquare(self):
        self.c.add_to_expression("1")
        self.c.add_to_expression("4")
        self.c.add_to_expression("4")
        self.c.sqrt()
        self.c.append_operator("-")
        self.c.add_to_expression("2")
        self.c.square()
        self.c.evaluate()

        self.assertEqual(self.c.current_expression, "8", msg=None)

        self.c.backspace()
        self.c.backspace()

    def test_negativeNumbers(self):
        self.c.append_operator("-")
        self.c.add_to_expression("5")
        self.c.append_operator("-")
        self.c.add_to_expression("5")
        self.c.append_operator("-")
        self.c.add_to_expression("5")
        self.c.append_operator("-")
        self.c.add_to_expression("5")
        self.c.evaluate()

        self.assertEqual(self.c.current_expression, "-20", msg=None)

        self.c.clear()


if __name__ == '__main__':
    unittest.main()