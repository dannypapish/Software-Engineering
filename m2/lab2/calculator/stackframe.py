from helpers import is_a_number, is_unary_operator, is_binary_operator
from scientific_operations import scientific_calculate
from simple_operations import simple_calculate


class CalculatorStack:
    """
    A stack structure to help perform evaluation of a postfix expression.

    attributes:
        - original_expression: the original expression that was evaluated
        - stack: a list of items
        - postfix_expression: the postfix expression that was evaluated
        - result: the result of the evaluation
    """

    def __init__(self):
        self.original_expression = None
        self.stack = []
        self.postfix_expression = None
        self.result = None

    def push(self, item):
        """
        Push an item onto the stack.

        args:
            - item: the item to push onto the stack
        """
        self.stack.append(item)

    def pop(self):
        """
        Pop an item off the stack.

        returns:
            - the item that was popped off the stack
        """
        return self.stack.pop()

    def peek(self):
        """
        Peek at the top item on the stack.

        returns:
            - the top item on the stack
        """
        return self.stack[-1]

    def is_empty(self):
        """
        Check if the stack is empty.

        returns:
            - True if the stack is empty, False otherwise
        """
        return len(self.stack) == 0

    def size(self):
        """
        Return the size of the stack.

        returns:
            - the size of the stack
        """
        return len(self.stack)

    def get_precedence(self, operator):
        """
        Get the precedence of an operator.

        args:
            - operator: the operator to get the precedence of

        returns:
            - the precedence of the operator
        """
        top_priority = ['*', '/', 'sin', 'cos', 'tan', 'ln']
        second_priority = ['+', '-']
        if operator in top_priority:
            return 3
        elif operator in second_priority:
            return 2
        else:
            return 1

    def set_postfix(self):
        """
        Converts the self.original_expression to postfix and stores it in self.postfix_expression.

        modifies:
            - self.postfix_expression
        """
        expression = self.original_expression
        self.postfix_expression = []
        operator_stack = CalculatorStack()
        for token in expression:
            if is_a_number(token):
                self.postfix_expression.append(token)
            elif token == '(':
                operator_stack.push(token)
            elif token == ')':
                top_token = operator_stack.pop()
                while top_token != '(':
                    self.postfix_expression.append(top_token)
                    top_token = operator_stack.pop()
            else:
                while (not operator_stack.is_empty()) and \
                        (self.get_precedence(token) <= self.get_precedence(operator_stack.peek())):
                    self.postfix_expression.append(operator_stack.pop())
                operator_stack.push(token)
        while not operator_stack.is_empty():
            self.postfix_expression.append(operator_stack.pop())

    def calculate_by_operation_type(self, operation, num1, num2=None):
        """
        Determines the calculator type to use and calls the appropriate function.

        args:
            - operation: the operation to pass to the appropriate calculator
            - num1: the first number
            - num2: the second number

        returns:
            - the result of the calculation
        """
        if is_binary_operator(operation):
            return simple_calculate(operation, num1, num2)
        elif is_unary_operator(operation):
            return scientific_calculate(operation, num1)
        else:
            raise Exception(
                'Invalid operation from calculate_by_operation_type')

    def evaluate_postfix(self):
        """
        Evaluates the postfix expression stored in self.postfix_expression and stores the result in self.result.

        modifies:
            - self.result
        """

        for token in self.postfix_expression:
            if is_a_number(token):
                self.push(token)
            else:
                if is_binary_operator(token):
                    num2 = self.pop()
                    num1 = self.pop()
                    self.push(self.calculate_by_operation_type(
                        token, num1, num2))
                elif is_unary_operator(token):
                    num1 = self.pop()
                    self.push(self.calculate_by_operation_type(token, num1))
        self.result = self.pop()

    def clean_expression(self, expression: str):
        """
        Checks for misleading spaces, separates the expression into a list, and converts numbers to floats.

        args:
            - expression: the expression to clean

        returns:
            - a list representing the cleaned expression
        """

        if expression[0] == ' ':
            expression = expression[1:]
        if expression[-1] == ' ':
            expression = expression[:-1]
        expression = expression.split()
        for i in range(len(expression)):
            if is_a_number(expression[i]):
                expression[i] = float(expression[i])
        return expression

    def set_expression(self, expression: str):
        """
        Set the self.original_expression attribute.

        args:
            - expression: the cleaned expression to evaluate

        modifies:
            - self.original_expression
        """
        cleaned_expression = self.clean_expression(expression)
        self.original_expression = cleaned_expression

    def get_result(self):
        """
        Get the result of the evaluation.

        returns:
            - the result of the evaluation
        """
        return self.result

    def evaluate(self, expression):
        """
        Take in an expression, evaluate it, and return the result.

        args:
            - expression: the expression to evaluate

        returns:
            - the result of the evaluation
        """
        self.set_expression(expression)
        self.set_postfix()
        self.evaluate_postfix()
        return self.result


def main():
    """
    Main function to test the CalculatorStack class.

    output:
        - prints the result of the evaluation
    """

    stack = CalculatorStack()
    while True:
        expression = input('Enter an expression to evaluate: ')
        if expression == 'q':
            break
        print(stack.evaluate(expression))


if __name__ == '__main__':
    main()
