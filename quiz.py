import tkinter as tk
import tkinter.messagebox
from tkinter import Label
from tkinter import filedialog
from PIL import Image, ImageTk
import customtkinter

class Test:

    def __init__(self):


        self.window = tk.Tk()
        self.window.title("Test Page")
        # Get the screen width and height
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()

        # Calculate the center position of the screen
        center_x = screen_width // 2
        center_y = screen_height // 2

        # Set the window size and position
        self.window.geometry(f"{screen_width}x{screen_height - 75}+{center_x - screen_width // 2}+{center_y - screen_height // 2}")

        self.window.columnconfigure(1, weight = 1)
        self.title_label = tk.Label(self.window, text = 'Test Page', bg = 'green', fg = 'white', font = ("ariel", 20, "bold"))
        self.title_label.grid(row = 0, column = 0, columnspan = 2 , sticky = 'we')

        self.question_label = tk.Label(self.window, text='Enter Your Question Here: ', fg='black', font=("ariel", 20, "bold"))
        self.question_label.grid(row=1, column=0, sticky='we')
        self.textbox = customtkinter.CTkTextbox(self.window ,height= 100)
        self.textbox.grid(row=2, column=0, columnspan = 2, padx=(20, 20), pady=(40, 40), sticky="we")
        # # Variable to store the user's choice
        self.input_type = tk.StringVar()
        # value = self.input_type.get()
        self.choice_label = tk.Label(self.window, text='Question Choice: ', fg='black', font=("ariel", 20, "bold"))
        self.choice_label.grid(row=3, column=0, sticky='we')

        self.user_input_choice = customtkinter.CTkOptionMenu(self.window, values=["Multiple Choice", "Short Answer"],
                                                             variable = self.input_type,
                                                             command= self.create_input_widget)

        self.user_input_choice.grid(row=3, column=1, padx=20, pady=(10, 10))

        #create radio buttons frame (four entries because radio button have four choices)
        self.radiobutton_frame = customtkinter.CTkFrame(self.window)
        # self.radiobutton_frame.grid(row=4, column=0, columnspan = 2,  padx=(20, 20), pady=(20, 0), sticky="nsew")

        self.radiobutton_frame.grid_columnconfigure(1, weight=1)
        self.radio_label_1 = tk.Label(self.radiobutton_frame, text='Choice 1: ', fg='black', font=("ariel", 20, "bold"))
        self.radio_label_1.grid(row = 0, column=0)
        self.radio_choice_1 = customtkinter.CTkEntry(self.radiobutton_frame , placeholder_text="Choice 1")
        self.radio_choice_1.grid(row= 0, column=1, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="ew")
        self.radio_label_2 = tk.Label(self.radiobutton_frame, text='Choice 2: ', fg='black', font=("ariel", 20, "bold"))
        self.radio_label_2.grid(row = 1, column=0)
        self.radio_choice_2 = customtkinter.CTkEntry(self.radiobutton_frame , placeholder_text="Choice 2")
        self.radio_choice_2.grid(row= 1, column=1, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="ew")
        self.radio_label_3 = tk.Label(self.radiobutton_frame, text='Choice 3: ', fg='black', font=("ariel", 20, "bold"))
        self.radio_label_3.grid(row =2, column=0)
        self.radio_choice_3 = customtkinter.CTkEntry(self.radiobutton_frame , placeholder_text="Choice 3")
        self.radio_choice_3.grid(row= 2, column=1, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="ew")
        self.radio_label_4 = tk.Label(self.radiobutton_frame, text='Choice 4: ', fg='black', font=("ariel", 20, "bold"))
        self.radio_label_4.grid(row = 3, column=0)
        self.radio_choice_4 = customtkinter.CTkEntry(self.radiobutton_frame , placeholder_text="Choice 4")
        self.radio_choice_4.grid(row= 3, column=1, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="ew")

        self.answer_label = tk.Label(self.radiobutton_frame, text='Answer: ', fg='black', font=("ariel", 20, "bold"))
        self.answer_label.grid(row = 4, column=0)
        self.answer = customtkinter.CTkTextbox(self.radiobutton_frame, height=100)
        self.answer.grid(row=4, column=1, columnspan=2, padx=(20, 20), pady=(40, 40), sticky="we")

        #create entry frame (four entries because radio button have four choices)
        self.answer_frame = customtkinter.CTkFrame(self.window)
        # self.answer_frame.grid(row=4, column=0, columnspan = 2,  padx=(20, 20), pady=(20, 0), sticky="nsew")
        self.answer_frame.grid_columnconfigure(1, weight=1)
        self.entry_answer_label = tk.Label(self.answer_frame, text='Answer: ', fg='black', font=("ariel", 20, "bold"))
        self.entry_answer_label.grid(row = 0, column=0)
        self.entry_answer = customtkinter.CTkTextbox(self.answer_frame, height=100)
        self.entry_answer.grid(row=0, column=1, columnspan=2, padx=(20, 20), pady=(40, 40), sticky="we")

        self.window.mainloop()


    def create_input_widget(self, user_input):
        if user_input == "Short Answer":
            self.answer_frame.grid(row=4, column=0, columnspan=2, padx=(20, 20), pady=(20, 0), sticky="nsew")
            self.radiobutton_frame.grid_forget()
        else:
            self.answer_frame.grid_forget()
            self.radiobutton_frame.grid(row=4, column=0, columnspan=2, padx=(20, 20), pady=(20, 0), sticky="nsew")





Test()