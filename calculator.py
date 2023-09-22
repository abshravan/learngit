import tkinter as tk

# Define functions for calculator operations
def add():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        result.set(num1 + num2)
    except ValueError:
        result.set("Invalid input")

def subtract():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        result.set(num1 - num2)
    except ValueError:
        result.set("Invalid input")

def multiply():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        result.set(num1 * num2)
    except ValueError:
        result.set("Invalid input")

def divide():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        if num2 == 0:
            result.set("Division by zero")
        else:
            result.set(num1 / num2)
    except ValueError:
        result.set("Invalid input")

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Create input fields and labels
label_num1 = tk.Label(root, text="Enter first number:")
label_num1.pack()
entry_num1 = tk.Entry(root)
entry_num1.pack()

label_num2 = tk.Label(root, text="Enter second number:")
label_num2.pack()
entry_num2 = tk.Entry(root)
entry_num2.pack()

# Create buttons for calculator operations
btn_add = tk.Button(root, text="Add", command=add)
btn_add.pack()

btn_subtract = tk.Button(root, text="Subtract", command=subtract)
btn_subtract.pack()

btn_multiply = tk.Button(root, text="Multiply", command=multiply)
btn_multiply.pack()

btn_divide = tk.Button(root, text="Divide", command=divide)
btn_divide.pack()

# Create a label to display the result
result = tk.StringVar()
result_label = tk.Label(root, textvariable=result)
result_label.pack()

# Run the GUI application
root.mainloop()
