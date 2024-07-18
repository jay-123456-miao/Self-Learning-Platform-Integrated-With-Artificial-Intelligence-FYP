import tkinter as tk
import tkinter.messagebox
from tkinter import Label, messagebox
from tkinter import filedialog
from PIL import Image, ImageTk
from Database import *
import customtkinter

class Test(customtkinter.CTk):
    def __init__(self, slp, course_info, username, ins):
        self.course_info = course_info
        self.slp = slp
        self.username = username
        self.ins = ins
        self.window = customtkinter.CTk()
        self.quiz_number = self.slp.get_quiz_number() + 1
        self.slp.set_quiz_number(self.quiz_number)
        super().__init__()
        # Get the screen width and height
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        # Calculate the center position of the screen
        center_x = screen_width // 2
        center_y = screen_height // 2
        # Set the window size and position
        self.window.geometry(
            f"{screen_width}x{screen_height - 75}+{center_x - screen_width // 2}+{center_y - screen_height // 2}")
        self.window.title("Test Page")
        self.window.columnconfigure(1, weight = 1)
        self.title_label = tk.Label(self.window, text = 'Test Page', bg = 'green', fg = 'white', font = ("ariel", 20, "bold"))
        self.title_label.grid(row = 0, column = 0, columnspan = 2 , sticky = 'we')
        self.question_label = tk.Label(self.window, text='Enter Your Question Here: ', fg='black', font=("ariel", 20, "bold"))
        self.question_label.grid(row=1, column=0, sticky='we')
        self.question_textbox = customtkinter.CTkTextbox(self.window ,height= 100)
        self.question_textbox.grid(row=2, column=0, columnspan = 2, padx=(20, 20), pady=(40, 40), sticky="we")
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
        # self.radiobutton_frame.grid(row=4, column=0, columnspan = 2, padx=(20, 20), pady=(20, 0), sticky="nsew")
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
        # self.answer_frame.grid(row=4, column=0, columnspan = 2, padx=(20, 20), pady=(20, 0), sticky="nsew")
        self.answer_frame.grid_columnconfigure(1, weight=1)
        self.entry_answer_label = tk.Label(self.answer_frame, text='Answer: ', fg='black', font=("ariel", 20, "bold"))
        self.entry_answer_label.grid(row = 0, column=0)
        self.entry_answer = customtkinter.CTkTextbox(self.answer_frame, height=100)
        self.entry_answer.grid(row=0, column=1, columnspan=2, padx=(20, 20), pady=(40, 40), sticky="we")

        #create the add new page button
        self.bottom_frame = customtkinter.CTkFrame(self.window)
        self.add_quiz_button = customtkinter.CTkButton(self.bottom_frame, text='Add New Page', command = lambda : self.add_new_page("Add"))
        self.add_quiz_button.grid(row=0, column=0, padx=(1000, 100), pady=20, sticky = 'e')
        self.finish_quiz_button = customtkinter.CTkButton(self.bottom_frame, text='Finish', command = lambda : self.quiz_to_menu("Submit"))
        self.finish_quiz_button.grid(row=0, column=1, padx=20, pady=20, sticky = 'e')
        self.window.mainloop()


    def add_new_page(self, type):
        self.capture_input(user_input= self.user_input_choice.get(), course_info= self.course_info, type = type)
        self.window.destroy()
        Test()
    def create_input_widget(self, user_input):
        if user_input == "Short Answer":
            self.answer_frame.grid(row=4, column=0, columnspan=2, padx=(20, 20), pady=(20, 0), sticky="nsew")
            self.radiobutton_frame.grid_forget()
            self.bottom_frame.grid(row=5, column=1, padx=(20, 20), pady=(20, 0), sticky="nsew")
        else:
            self.answer_frame.grid_forget()
            self.radiobutton_frame.grid(row=4, column=0, columnspan=2, padx=(20, 20), pady=(20, 0), sticky="nsew")
            self.bottom_frame.grid(row=5, column=1, padx=(20, 20), pady=(20, 0), sticky="nsew")

    def capture_input(self, user_input, course_info, type):
        if user_input == "Short Answer":
            quiz_question = self.question_textbox.get("1.0", "end-1c")
            short_answer_ans = self.entry_answer.get("1.0", "end-1c")
            quiz = Quiz(quiz_number= self.quiz_number,  quiz_question = quiz_question,  input_type=user_input, short_answer_ans=short_answer_ans, course_info= course_info)
            quiz.create_quiz_info()
        else:
            quiz_question = self.question_textbox.get("1.0", "end-1c")
            radio_choice_1 = self.radio_choice_1.get()
            radio_choice_2 = self.radio_choice_2.get()
            radio_choice_3 = self.radio_choice_3.get()
            radio_choice_4 = self.radio_choice_4.get()
            radio_answer = self.answer.get("1.0", "end-1c")
            quiz2 = Quiz(quiz_number= self.quiz_number, quiz_question = quiz_question, input_type=user_input, radio_choice_1=radio_choice_1, radio_choice_2=radio_choice_2, radio_choice_3=radio_choice_3, radio_choice_4 = radio_choice_4, radio_answer=radio_answer, course_info=course_info)
            quiz2.create_quiz_info()

        if type == "Add":
            self.window.destroy()
            Test(self.slp, self.course_info, self.username, self.ins)
        elif type == "Submit":
            messagebox.showinfo('Message', "Quiz Added Successfully")
            # self.quiz_to_menu(self.slp)
            self.quiz_number = 0
            self.slp.set_page_number(self.quiz_number)
            return

    def quiz_to_menu(self, type):
        from main import Instructor_Landing_Page
        self.capture_input(user_input=self.user_input_choice.get(), course_info=self.course_info, type=type)
        self.window.destroy()
        print(self.username)
        Instructor_Landing_Page(self.slp, self.username, self.ins)

# Test()