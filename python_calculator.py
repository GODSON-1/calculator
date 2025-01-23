
import tkinter as tk

def display_number(number):
    current_text = entry.get()
    entry.insert(0, current_text + str(number))  # Append the number to the current text

# Create the main window
root = tk.Tk()
root.title("Calculator")

# Create an entry box to display the number
entry = tk.Entry(root, width=40, borderwidth=10)
entry.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

# Create buttons for three different numbers
button1 = tk.Button(root, text="1",width=7,height=3,borderwidth=5,pady=20, padx=20, command=lambda: display_number(1))
button2 = tk.Button(root, text="2",width=7,height=3,borderwidth=5,pady=20, padx=20, command=lambda: display_number(2))
button3 = tk.Button(root, text="3",width=7,height=3,borderwidth=5,pady=20, padx=20, command=lambda: display_number(3))
button4 = tk.Button(root, text="4",width=7,height=3,borderwidth=5,pady=20, padx=20, command=lambda: display_number(4))
button5 = tk.Button(root, text="5",width=7,height=3,borderwidth=5,pady=20, padx=20, command=lambda: display_number(5))
button6 = tk.Button(root, text="6",width=7,height=3,borderwidth=5,pady=20, padx=20, command=lambda: display_number(6))
button7 = tk.Button(root, text="7",width=7,height=3,borderwidth=5,pady=20, padx=20, command=lambda: display_number(7))
button8 = tk.Button(root, text="8",width=7,height=3,borderwidth=5,pady=20, padx=20, command=lambda: display_number(8))
button9 = tk.Button(root, text="9",width=7,height=3,borderwidth=5,pady=20, padx=20, command=lambda: display_number(9))
button0 = tk.Button(root, text="0",width=7,height=3,borderwidth=5,pady=20, padx=20, command=lambda: display_number(0))
button_clear = tk.Button(root, text="Clear",width=30,height=3,borderwidth=5,pady=20, padx=20,command=lambda:entry.delete(0,tk.END))
button_add = tk.Button(root,text="+",width=7,height=3,borderwidth=5,pady=20, padx=20, command=lambda: display_number("+"))
button_substraction = tk.Button(root,text="-",width=7,height=3,borderwidth=5,pady=20, padx=20, command=lambda: display_number("-"))
button_division = tk.Button(root,text="/",width=7,height=3,borderwidth=5,pady=20, padx=20, command=lambda: display_number("/"))
button_multiplication = tk.Button(root,text="x",width=7,height=3,borderwidth=5,pady=20, padx=20, command=lambda: display_number("x"))
button_equal = tk.Button(root, text="=",width=7,height=3,borderwidth=5,pady=20, padx=20, command=lambda: display_number("="))
                                         


# Put the buttons on the screen
button1.grid(row=1, column=0)
button2.grid(row=1, column=1)
button3.grid(row=1, column=2)
button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)
button7.grid(row=3, column=0)
button8.grid(row=3, column=1)
button9.grid(row=3, column=2)
button0.grid(row=4, column=0)
button_add.grid(row=4, column=1)
button_substraction.grid(row=4, column=2)
button_division .grid(row=5, column=0)
button_multiplication.grid(row=5, column=1)
button_equal.grid(row=5, column=2)
button_clear.grid(row=6, column=0,columnspan=4)



# Start the main event loop
root.mainloop()
