import tkinter as tk
from tkinter.ttk import Combobox

root = tk.Tk()

# Variable to store the user's choice
input_type = tk.StringVar(value="entry")

# Variable to store the selected radio button value
selected_value = tk.StringVar()

def create_input_widget(*args):
    if input_type.get() == "entry":
        # Create an entry widget
        entry_widget.pack()
        radio_buttons_frame.pack_forget()
        # Clear the selected radio button value
        selected_value.set("")
    else:
        # Create radio buttons
        entry_widget.pack_forget()
        radio_buttons_frame.pack()
        # Set the selected radio button value to the current value in the entry
        selected_value.set(entry_widget.get())

def get_input_value():
    if input_type.get() == "entry":
        # Get the value from the entry widget
        print("Input value:", entry_widget.get())
    else:
        # Get the value from the selected radio button
        print("Selected value:", selected_value.get())

# Create the radio buttons
radio_buttons_frame = tk.Frame(root)
radio_button_1 = tk.Radiobutton(radio_buttons_frame, text="Option 1", variable=selected_value, value="option1")
radio_button_2 = tk.Radiobutton(radio_buttons_frame, text="Option 2", variable=selected_value, value="option2")
radio_button_1.pack(side=tk.LEFT)
radio_button_2.pack(side=tk.LEFT)

# Create the entry widget
entry_widget = tk.Entry(root, textvariable=selected_value)

# Create the combobox
input_type_combobox = Combobox(root, textvariable=input_type, values=["entry", "radio"])
input_type_combobox.pack()
input_type_combobox.bind("<<ComboboxSelected>>", create_input_widget)

# Create a button to get the input value
get_value_button = tk.Button(root, text="Get Input Value", command=get_input_value)
get_value_button.pack()

create_input_widget()  # Initial creation of the input widget

root.mainloop()