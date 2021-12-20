from tkinter import *

#globally declare the expression value
expression = ""


# Function to update expressiom
# in the text entry box
def press(num):
    # point out the global expression variable
    global expression

    # concatenation of string
    expression = expression + str(num)

    # update the expression by using set method
    equation.set(expression)


# Function to evaluate the final expression
def equalpress():
    # Try and except statement is used
    # for handling the errors like zero
    # division error etc.

    # Put that code inside the try block
    # which may generate the error
    try:

        global expression

        # eval function evaluate the expression
        # and str function convert the result
        # into string
        total = str(eval(expression))

        equation.set(total)

        # update the expersion to reflect the current total
        # by empty string
        expression = total

        # if error is generate then handle
    # by the except block
    except:

        equation.set(" error ")
        expression = ""


# Function to clear the contents
# of text entry box
def clear():
    global expression
    expression = ""
    equation.set("")


#  Driver code
if __name__ == "__main__":
    # create root window
    root = Tk()

    # root window title and dimension
    root.title("Calculator")
    root.geometry('265x150')

    # StringVar() is the variable class
    # we create an instance of this class
    equation = StringVar()

    # create the text entry box for
    # showing the expression .
    expression_field = Entry(root, textvariable=equation)

    # grid method is used for placing
    # the widgets at respective positions
    # in table like structure .
    expression_field.grid(columnspan=4, ipadx=70)

    equation.set('enter your expression')


    # create a Buttons and place at a particular
    # location inside the root window .
    # when user press the button, the command or
    # function affiliated to that button is executed
    btn_1 = Button(root, text="1", width=7, height=1, fg="blue", command=lambda: press(1))

    btn_2 = Button(root, text="2", width=7, height=1, fg="blue", command=lambda: press(2))

    btn_3 = Button(root, text="3", width=7, height=1, fg="blue", command=lambda: press(3))

    btn_4 = Button(root, text="4", width=7, height=1, fg="blue", command=lambda: press(4))

    btn_5 = Button(root, text="5", width=7, height=1, fg="blue", command=lambda: press(5))

    btn_6 = Button(root, text="6", width=7, height=1, fg="blue", command=lambda: press(6))

    btn_7 = Button(root, text="7", width=7, height=1, fg="blue", command=lambda: press(7))

    btn_8 = Button(root, text="8", width=7, height=1, fg="blue", command=lambda: press(8))

    btn_9 = Button(root, text="9", width=7, height=1, fg="blue", command=lambda: press(9))

    btn_0 = Button(root, text="0", width=7, height=1, fg="blue", command=lambda: press(0))

    btn_plus = Button(root, text="+", width=7, height=1, fg="blue", command=lambda: press("+"))

    btn_minus = Button(root, text="-", width=7, height=1, fg="blue", command=lambda: press("-"))

    btn_multiply = Button(root, text="*", width=7, height=1, fg="blue", command=lambda: press("*"))

    btn_divide = Button(root, text="/", width=7, height=1, fg="blue", command=lambda: press("/"))

    btn_equal = Button(root, text="=", width=7, height=1, fg="blue", command=equalpress)

    btn_clear = Button(root, text="clear", width=7, height=1, fg="blue", command=clear)

    btn_decimal = Button(root, text=".", width=7, height=1, fg="blue", command=lambda: press("."))

    btn_power = Button(root, text="^", width=7, height=1, fg="blue", command=lambda: press("**"))

    btn_open_bracket = Button(root, text="(", width=7, height=1, fg="blue", command=lambda: press("("))

    btn_close_bracket = Button(root, text=")", width=7, height=1, fg="blue", command=lambda: press(")"))

    btn_1.grid(column=0, row=1)
    btn_2.grid(column=1, row=1)
    btn_3.grid(column=2, row=1)
    btn_plus.grid(column=3, row=1)
    btn_4.grid(column=0, row=2)
    btn_5.grid(column=1, row=2)
    btn_6.grid(column=2, row=2)
    btn_minus.grid(column=3, row=2)
    btn_7.grid(column=0, row=3)
    btn_8.grid(column=1, row=3)
    btn_9.grid(column=2, row=3)
    btn_multiply.grid(column=3, row=3)
    btn_0.grid(column=0, row=4)
    btn_clear.grid(column=1, row=4)
    btn_equal.grid(column=2, row=4)
    btn_divide.grid(column=3, row=4)
    btn_decimal.grid(column=0, row=5)
    btn_open_bracket.grid(column=1, row=5)
    btn_close_bracket.grid(column=2, row=5)
    btn_power.grid(column=3, row=5)
    

    root.mainloop()