import tkinter as tk
from tkinter import filedialog

from c_chat import c_chat_z as c_chat_z

# -*- Window -*-
window = tk.Tk()
window.title('ptt analysis')  # Title
window.geometry('300x160')  # Window size

# Create the first entry widget for input
label1 = tk.Label(window, text="關鍵字")
label1.grid(row=0, column=0)  # Position label in row 0, column 0
entry1 = tk.Entry(window)
entry1.grid(row=0, column=1)  # Position entry next to the label

# Label and Entry for Value 2
label2 = tk.Label(window, text="截止日")
label2.grid(row=1, column=0)  # Position label in row 1, column 0
entry2 = tk.Entry(window)
entry2.grid(row=1, column=1)  # Position entry next to the label

# Checkbox for Value 3
check_var = tk.IntVar()  # Variable to store the state of the checkbox
checkbox = tk.Checkbutton(window, text="只要出現關鍵字就搜尋", variable=check_var)
checkbox.grid(row=2, column=0, columnspan=2)  # Position the checkbox

# Function to handle button click
def handle_button_click():
    # Get the values from the entry widgets
    value1 = entry1.get().lower()
    value2 = entry2.get().lower()
    # Determine the value of value3 based on the checkbox
    if check_var.get() == 1:
        value3 = "include all" 
    else:
        value3 = "title only"
    
    c_chat_z(value1, value2, value3)

# Button to trigger the action
bt1 = tk.Button(window, text='Analyze', command=handle_button_click)
bt1.grid(row=3, column=0, columnspan=2)

window.mainloop()