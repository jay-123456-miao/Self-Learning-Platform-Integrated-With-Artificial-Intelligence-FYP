import tkinter as tk
from tkinter import font as tkFont
from PIL import Image, ImageTk
import customtkinter
from learner_course_list import *
class Learner_Landing_Page(customtkinter.CTk):
    def __init__(self,slp, username, ins):
        self.ins = ins
        self.slp = slp
        self.username = username

        self.window = customtkinter.CTk()
        super().__init__()
        self.window.title('Learner Main Page')

        # Get the screen width and height
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()

        # Calculate the center position of the screen
        center_x = screen_width // 2
        center_y = screen_height // 2

        #creating the font obj
        font_obj = Font()

        # Set the window size and positionasdas
        self.window.geometry(f"{screen_width}x{screen_height - 75}+{center_x - screen_width // 2}+{center_y - screen_height // 2}")

        self.window.resizable(False, False)

        self.window.grid_columnconfigure(0, weight = 1)
        self.window.grid_rowconfigure(0, weight = 1)

        self.main_frame = customtkinter.CTkFrame(self.window, corner_radius=20, bg_color= 'grey')

        self.main_frame.grid(row = 0, column = 0, padx=(20, 20), pady=(20, 20), sticky = 'nsew')

        self.main_frame.grid_rowconfigure(1, weight = 1)
        self.main_frame.grid_columnconfigure( (1,2), weight = 1)

        # creating a label to show welcome users
        self.welcome_label = tk.Label(self.main_frame, text = f"Welcome back to the system {self.username}", font = font_obj.get_font(20), bg='grey')
        self.welcome_label.grid(row = 0, column = 0)

        self.record_image = Image.open('record_img.png')
        self.record_image = self.record_image.resize((200,200))
        self.resized_record_image = ImageTk.PhotoImage(self.record_image)

        # creating image buttons
        self.record_button = tk.Button(self.main_frame,  text = 'View Courses', image=self.resized_record_image, compound= 'top', bg = 'grey', font=font_obj.get_font(36), command =  lambda: self.learner_menu_to_learner_course_list())
        self.record_button.grid(row=1, column=2,padx=(40, 40), pady=(20, 20), sticky = 'w')

        self.exit_button = customtkinter.CTkButton(self.main_frame, text = "Log Out", command = lambda: self.learner_logout())
        self.exit_button.grid(row = 2, column = 3, padx = 20, pady = 20)

        self.window.mainloop()


    def learner_menu_to_learner_course_list(self):
        self.window.destroy()
        Learner_course_List_Page(self.slp, self.username, self.ins)

    def learner_logout(self):
        from main import LoginPage
        self.window.destroy()
        LoginPage(self.slp)

class Font:
    def get_font(self, size):
        helv = tkFont.Font(family='Helvetica', size=size, weight='bold')
        return helv


