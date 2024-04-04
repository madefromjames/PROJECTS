# Importing necessary modules from tkinter library
from tkinter import *

# Creating a tkinter window
win = Tk()

# Setting the initial dimensions of the window
win.geometry("312x324")

# Ensuring the window size remains fixed (not resizable)
win.resizable(0, 0)

# Setting the title of the window
win.title('Calculator')

# Function to clear the input field
def btn_clear():
    global expression
    expression = ""  # Clearing the expression
    input_text.set("")  # Clearing the input field

# Function to delete the last character from the input field
def btn_delete():
    global expression
    expression = input_text.get()  # Getting the current expression
    new_expression = expression[:-1]  # Removing the last character
    input_text.set(new_expression)  # Updating the input field

# Function to calculate percentage of the current expression
def btn_percent():
    global expression
    expression = input_text.get()  # Getting the current expression
    expression_numeric = float(expression)  # Converting expression to float
    divide = str(expression_numeric / 100)  # Calculating percentage
    result = str(eval(divide))  # Evaluating the result
    input_text.set(result)  # Updating the input field
    expression = f"{result}"  # Updating the expression

# Function to handle button clicks
def btn_click(item):
    global expression
    expression = expression + str(item)  # Appending clicked button value to expression
    input_text.set(expression)  # Updating the input field

# Function to evaluate the expression and display the result
def btn_equal():
    global expression
    result = str(eval(expression))  # Evaluating the expression
    input_text.set(result)  # Updating the input field with result
    expression = f"{result}"  # Updating the expression

# Initializing the expression variable
expression = ""

# Creating a StringVar to store and manipulate the input field text
input_text = StringVar()

# Creating a frame for the input field
input_frame = Frame(win, width=312, bd=0, height=50, highlightbackground="black", highlightthickness=2, highlightcolor="black")
input_frame.pack(side=TOP)

# Creating an Entry widget for input
input = Entry(input_frame, width=50, textvariable=input_text, bg="#000", fg="#fff", font=('arial', 21, 'bold'), bd=0, justify=RIGHT)
input.insert(0, '0')  # Inserting default value '0' into input field
input.grid(row=0, column=0)
input.pack(ipady=10)  # Adjusting internal padding in y-direction

# Creating a frame for the buttons
btn = Frame(win, width=312, height=272.5, bg='grey')
btn.pack()

# Creating calculator buttons and arranging them in a grid

# first row
clear = Button(btn, text='AC', fg='orange', width=10, height=3, bd=0, bg="#000", cursor="hand2", command=lambda: btn_clear()).grid(row=0, column=0, padx=1, pady=1)
delete = Button(btn, text='⇦', fg='orange', width=10, height=3, bd=0, bg="#000", cursor="hand2", command=lambda: btn_delete()).grid(row=0, column=1, padx=1, pady=1)
clear = Button(btn, text='%', fg='orange', width=10, height=3, bd=0, bg="#000", cursor="hand2", command=lambda: btn_percent()).grid(row=0, column=2, padx=1, pady=1)
divide = Button(btn, text='÷', fg='orange', width=10, height=3, bd=0, bg="#000", cursor="hand2", command=lambda: btn_click('/')).grid(row=0, column=3, padx=1, pady=1)

# second row
seven = Button(btn, text='7', fg='#fff', bg='#000', width=10, height=3, bd=0, cursor='hand2', command=lambda: btn_click('7')).grid(row=1, column=0, padx=1, pady=1)
eight = Button(btn, text='8', fg='#fff', bg='#000', width=10, height=3, bd=0, cursor='hand2', command=lambda: btn_click('8')).grid(row=1, column=1, padx=1, pady=1)
nine = Button(btn, text='9', fg='#fff', bg='#000', width=10, height=3, bd=0, cursor='hand2', command=lambda: btn_click('9')).grid(row=1, column=2, padx=1, pady=1)
multiply = Button(btn, text='x', fg='orange', bg='#000', width=10, height=3, bd=0, cursor='hand2', command=lambda: btn_click('*')).grid(row=1, column=3, padx=1, pady=1)

# third row
four = Button(btn, text='4', fg='#fff', bg='#000', width=10, height=3, bd=0, cursor='hand2', command=lambda: btn_click('4')).grid(row=2, column=0, padx=1, pady=1)
five = Button(btn, text='5', fg='#fff', bg='#000', width=10, height=3, bd=0, cursor='hand2', command=lambda: btn_click('5')).grid(row=2, column=1, padx=1, pady=1)
six = Button(btn, text='6', fg='#fff', bg='#000', width=10, height=3, bd=0, cursor='hand2', command=lambda: btn_click('6')).grid(row=2, column=2, padx=1, pady=1)
minus = Button(btn, text='-', fg='orange', bg='#000', width=10, height=3, bd=0, cursor='hand2', command=lambda: btn_click('-')).grid(row=2, column=3, padx=1, pady=1)

# fourth row
one = Button(btn, text='1', fg='#fff', bg='#000', width=10, height=3, bd=0, cursor='hand2', command=lambda: btn_click('1')).grid(row=3, column=0, padx=1, pady=1)
two = Button(btn, text='2', fg='#fff', bg='#000', width=10, height=3, bd=0, cursor='hand2', command=lambda: btn_click('2')).grid(row=3, column=1, padx=1, pady=1)
three = Button(btn, text='3', fg='#fff', bg='#000', width=10, height=3, bd=0, cursor='hand2', command=lambda: btn_click('3')).grid(row=3, column=2, padx=1, pady=1)
plus = Button(btn, text='+', fg='orange', bg='#000', width=10, height=3, bd=0, cursor='hand2', command=lambda: btn_click('+')).grid(row=3, column=3, padx=1, pady=1)

# fifth row
zero = Button(btn, text='0', fg='#fff', bg='#000', width=21, height=3, bd=0, cursor='hand2', command=lambda: btn_click('0')).grid(row=4, column=0, columnspan=2, padx=1, pady=1)
dot = Button(btn, text='.', fg='orange', bg='#000', width=10, height=3, bd=0, cursor='hand2', command=lambda: btn_click('.')).grid(row=4, column=2, padx=1, pady=1)
equal = Button(btn, text='=', fg='#fff', bg='orange', width=10, height=3, bd=0, cursor='hand2', command=lambda: btn_equal()).grid(row=4, column=3, padx=1, pady=1)

win.mainloop()
