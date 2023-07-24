import tkinter as tk
from stackframe import CalculatorStack


class CalculatorGUI:
    """
    Graphical user interface for the calculator stackframe.
    Supports basic arithmetic, parentheses, floats, negative numbers, and scientific operations.
    """

    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Calculator GUI')
        self.root.resizable(True, True)
        self.root.geometry('820x300')
        self.calc_stack = CalculatorStack()
        self.entry = tk.Entry(self.root, width=50)
        self.entry.grid(row=0, column=0, columnspan=6, padx=5, pady=10)
        self.make_buttons()

    def make_buttons(self):
        """
        Makes all buttons for the calculator.
        This code is poorly written, but Tkinter is a pain to work with.
        Once I research why tkinter refuses to create unique attributes for each button via a loop, this will be refactored.
        """

        # NUMBERS
        self.button1 = tk.Button(
            self.root, text='1', width=10, command=lambda: self.button_press('1'))
        self.button1.grid(row=1, column=0, padx=5, pady=10)
        self.button2 = tk.Button(
            self.root, text='2', width=10, command=lambda: self.button_press('2'))
        self.button2.grid(row=1, column=1, padx=5, pady=10)
        self.button3 = tk.Button(
            self.root, text='3', width=10, command=lambda: self.button_press('3'))
        self.button3.grid(row=1, column=2, padx=5, pady=10)
        self.button4 = tk.Button(
            self.root, text='4', width=10, command=lambda: self.button_press('4'))
        self.button4.grid(row=2, column=0, padx=5, pady=10)
        self.button5 = tk.Button(
            self.root, text='5', width=10, command=lambda: self.button_press('5'))
        self.button5.grid(row=2, column=1, padx=5, pady=10)
        self.button6 = tk.Button(
            self.root, text='6', width=10, command=lambda: self.button_press('6'))
        self.button6.grid(row=2, column=2, padx=5, pady=10)
        self.button7 = tk.Button(
            self.root, text='7', width=10, command=lambda: self.button_press('7'))
        self.button7.grid(row=3, column=0, padx=5, pady=10)
        self.button8 = tk.Button(
            self.root, text='8', width=10, command=lambda: self.button_press('8'))
        self.button8.grid(row=3, column=1, padx=5, pady=10)
        self.button9 = tk.Button(
            self.root, text='9', width=10, command=lambda: self.button_press('9'))
        self.button9.grid(row=3, column=2, padx=5, pady=10)
        self.buttonNeg = tk.Button(
            self.root, text='neg', width=10, command=lambda: self.button_press('-'))
        self.buttonNeg.grid(row=4, column=0, padx=5, pady=10)
        self.button0 = tk.Button(
            self.root, text='0', width=10, command=lambda: self.button_press('0'))
        self.button0.grid(row=4, column=1, padx=5, pady=10)
        self.buttonDot = tk.Button(
            self.root, text='.', width=10, command=lambda: self.button_press('.'))
        self.buttonDot.grid(row=4, column=2, padx=5, pady=10)

        # SIMPLE OPERATORS
        self.buttonAdd = tk.Button(
            self.root, text='+', width=10, command=lambda: self.button_press(' + '))
        self.buttonAdd.grid(row=1, column=3, padx=5, pady=10)
        self.buttonSub = tk.Button(
            self.root, text='-', width=10, command=lambda: self.button_press(' - '))
        self.buttonSub.grid(row=2, column=3, padx=5, pady=10)
        self.buttonMul = tk.Button(
            self.root, text='*', width=10, command=lambda: self.button_press(' * '))
        self.buttonMul.grid(row=3, column=3, padx=5, pady=10)
        self.buttonDiv = tk.Button(
            self.root, text='/', width=10, command=lambda: self.button_press(' / '))
        self.buttonDiv.grid(row=4, column=3, padx=5, pady=10)

        # SCIENTIFIC OPERATORS
        self.buttonSin = tk.Button(
            self.root, text='ln', width=10, command=lambda: self.button_press(' ln '))
        self.buttonSin.grid(row=1, column=4, padx=5, pady=10)
        self.buttonCos = tk.Button(
            self.root, text='sin', width=10, command=lambda: self.button_press(' sin '))
        self.buttonCos.grid(row=2, column=4, padx=5, pady=10)
        self.buttonTan = tk.Button(
            self.root, text='cos', width=10, command=lambda: self.button_press(' cos '))
        self.buttonTan.grid(row=3, column=4, padx=5, pady=10)
        self.buttonCot = tk.Button(
            self.root, text='tan', width=10, command=lambda: self.button_press(' tan '))
        self.buttonCot.grid(row=4, column=4, padx=5, pady=10)

        # CONTROL CHARACTERS
        self.buttonLParen = tk.Button(
            self.root, text='(', width=10, command=lambda: self.button_press(' ( '))
        self.buttonLParen.grid(row=1, column=5, padx=5, pady=10)
        self.buttonRParen = tk.Button(
            self.root, text=')', width=10, command=lambda: self.button_press(' ) '))
        self.buttonRParen.grid(row=2, column=5, padx=5, pady=10)
        self.buttonClear = tk.Button(
            self.root, text='C', width=10, command=lambda: self.clear_press())
        self.buttonClear.grid(row=3, column=5, padx=5, pady=10)
        self.buttonEquals = tk.Button(
            self.root, text='=', width=10, command=lambda: self.equals_press())
        self.buttonEquals.grid(row=4, column=5, padx=5, pady=10)

    def button_press(self, button_val: str, spacing_flag: bool = False):
        """
        Handles the press of a standard button (0-9, ., neg, C, =)

        args:
            - button_val: the string for the button pressed
        """
        button_val = " " + button_val + " " if spacing_flag else button_val
        self.entry.insert(tk.END, button_val)

    def clear_press(self):
        """
        Handles a clear press.
        """
        self.entry.delete(0, tk.END)

    def equals_press(self):
        """
        Handles an equals press.
        """
        expression = self.entry.get()
        self.entry.delete(0, tk.END)
        self.entry.insert(0, self.calc_stack.evaluate(expression))


def main():
    gui = CalculatorGUI()
    gui.root.mainloop()


if __name__ == '__main__':
    main()
