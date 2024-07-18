import tkinter as tk
from Database import *
from tkinter import Label
from tkinter import filedialog
from PIL import Image, ImageTk
import customtkinter



customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"



class course_content(customtkinter.CTk):

    def __init__(self, course_pages_content, course_len, slp, course_index, ins, username):
        self.window = customtkinter.CTk()
        super().__init__()
        self.course_index = course_index
        self.course_len = course_len
        self.slp = slp
        self.ins = ins
        self.username = username
        selected_course_content = course_pages_content
        course_page_content = selected_course_content[course_index]


        # loading all the images from database
        img1 = Image.open(course_page_content[20])
        img2 = Image.open(course_page_content[21])
        img3 = Image.open(course_page_content[22])
        img4 = Image.open(course_page_content[23])
        img5 = Image.open(course_page_content[24])
        img6 = Image.open(course_page_content[25])
        img7 = Image.open(course_page_content[26])
        img8 = Image.open(course_page_content[27])
        img9 = Image.open(course_page_content[28])


        # Resize the images
        img_1_resized = img1.resize((400, 150))
        img_2_resized = img2.resize((400, 150))
        img_3_resized = img3.resize((400, 150))
        img_4_resized = img4.resize((400, 150))
        img_5_resized = img5.resize((400, 150))
        img_6_resized = img6.resize((400, 150))
        img_7_resized = img7.resize((400, 150))
        img_8_resized = img8.resize((400, 150))
        img_9_resized = img9.resize((400, 150))

        #Load the images

        self.pic1 = ImageTk.PhotoImage(img_1_resized)
        self.pic2 = ImageTk.PhotoImage(img_2_resized)
        self.pic3 = ImageTk.PhotoImage(img_3_resized)
        self.pic4 = ImageTk.PhotoImage(img_4_resized)
        self.pic5 = ImageTk.PhotoImage(img_5_resized)
        self.pic6 = ImageTk.PhotoImage(img_6_resized)
        self.pic7 = ImageTk.PhotoImage(img_7_resized)
        self.pic8 = ImageTk.PhotoImage(img_8_resized)
        self.pic9 = ImageTk.PhotoImage(img_9_resized)

        # Get the screen width and height
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()

        # Calculate the center position of the screen
        center_x = screen_width // 2
        center_y = screen_height // 2

        # Set the window size and position
        self.window.geometry(
            f"{screen_width}x{screen_height - 75}+{center_x - screen_width // 2}+{center_y - screen_height // 2}")

        # configure grid layout (4x4)
        self.window.grid_columnconfigure(1, weight=1)
        # self.grid_columnconfigure((2, 3), weight=0)
        self.window.grid_rowconfigure((0,1), weight = 0 )
        self.window.grid_rowconfigure((2,3), weight=1)

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self.window, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=5, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame,
                                                                       values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))

        # Frame to show title, author, and date
        self.title_frame = customtkinter.CTkFrame(self.window, corner_radius=0)
        self.title_frame.grid(row=0, column=1, padx=(20, 20), pady=(20, 0), sticky="nsew")
        self.title_frame.grid_columnconfigure(0, weight=0)
        self.title_frame.grid_columnconfigure(1, weight=1)
        self.title_frame.grid_rowconfigure((0, 1, 2), weight=1)
        self.title_label = customtkinter.CTkLabel(self.title_frame, text="Title:")
        self.title_label.grid(row=0, column=0, padx=20, pady=(10, 0), sticky="w")
        self.title_content = customtkinter.CTkTextbox(self.title_frame, height  = 15)
        self.title_content.grid(row=0, column=1, padx=20, pady=(10, 0), sticky='we')

        self.author_label = customtkinter.CTkLabel(self.title_frame, text="Author:")
        self.author_label.grid(row=1, column=0, padx=20, pady=(10, 0), sticky="w")
        self.author_entry = customtkinter.CTkTextbox(self.title_frame, height = 15)
        self.author_entry.grid(row=1, column=1, padx=20, pady=10, sticky="we")


        # create an abstract frame
        self.abtract_frame = customtkinter.CTkFrame(self.window, corner_radius= 0)
        self.abtract_frame.grid(row=1, column=1, padx=(20, 20), pady=(20, 0), sticky="nsew")
        self.abtract_frame.grid_columnconfigure(0, weight = 1)
        self.abtract_label = customtkinter.CTkLabel(self.abtract_frame, text="Abtract:")
        self.abtract_label.grid(row=0, column=0, padx=20, pady=(10, 0), sticky="w")
        self.abstract_content = customtkinter.CTkTextbox(self.abtract_frame ,height= 100)
        self.abstract_content.grid(row=1, column=0, padx=(20, 20), pady=(20, 20), sticky="nsew")

        # create tabview
        self.tabview = customtkinter.CTkTabview(self.window)
        self.tabview.grid(row=2, column=1, padx=(20, 20), pady=(0, 0), sticky="nsew")
        self.tabview.add("Subtopic 1")
        self.tabview.add("Subtopic 2")
        self.tabview.add("Subtopic 3")

        # Usage example
        # Call the setup_tab_design function for each tab
        self.setup_tab_design("Subtopic 1")
        self.setup_tab_design("Subtopic 2")
        self.setup_tab_design("Subtopic 3")

        #populating the course contents
        self.title_content.insert(tk.END, course_page_content[2])
        self.author_entry.insert(tk.END, course_page_content[3])
        self.abstract_content.insert(tk.END, course_page_content[4])
        self.subtopic1_subtopic_content.insert(tk.END, course_page_content[5])
        self.subtopic1_data_entry_content1.insert(tk.END, course_page_content[6])
        self.subtopic1_data_entry_content2.insert(tk.END, course_page_content[7])
        self.subtopic1_data_entry_content3.insert(tk.END, course_page_content[8])
        self.subtopic1_textbox_content.insert(tk.END, course_page_content[9])
        self.subtopic2_subtopic_content.insert(tk.END, course_page_content[10])
        self.subtopic2_data_entry_content1.insert(tk.END, course_page_content[11])
        self.subtopic2_data_entry_content2.insert(tk.END, course_page_content[12])
        self.subtopic2_data_entry_content3.insert(tk.END, course_page_content[13])
        self.subtopic2_textbox_content.insert(tk.END, course_page_content[14])
        self.subtopic3_subtopic_content.insert(tk.END, course_page_content[15])
        self.subtopic3_data_entry_content1.insert(tk.END, course_page_content[16])
        self.subtopic3_data_entry_content2.insert(tk.END, course_page_content[17])
        self.subtopic3_data_entry_content3.insert(tk.END, course_page_content[18])
        self.subtopic3_textbox_content.insert(tk.END, course_page_content[19])

        # previous page button, add button , next page

        self.submit_frame = customtkinter.CTkFrame(self.window, corner_radius= 0)
        self.submit_frame.grid(row= 3, column = 1, padx=(20, 20), pady=(20, 0), sticky="nsew")
        self.submit_frame.grid_columnconfigure((0,1,2), weight=1)
        self.previous_page_button = customtkinter.CTkButton(self.submit_frame, text='Previous Page', command = lambda : self.slp.current_to_previous_page(selected_course_content, self.slp, self.course_index, self.course_len, self.window, ins, self.username))
        if self.course_index == 0:
            self.previous_page_button = customtkinter.CTkButton(self.submit_frame, text='Previous Page', state='Disabled')
        self.previous_page_button.grid(row=0, column=2, padx=20, pady=20)
        self.exit_button = customtkinter.CTkButton(self.submit_frame, text='Exit to Menu', command = lambda : self.content_to_menu())
        self.exit_button.grid(row=0, column=1, padx=20, pady=20)
        self.next_page_button = customtkinter.CTkButton(self.submit_frame, text='Next Page', command = lambda : self.slp.content_to_new_page(selected_course_content, self.slp, self.course_index, self.course_len, self.window, ins, self.username))
        if self.course_index == self.course_len - 1:
            self.next_page_button = customtkinter.CTkButton(self.submit_frame, text = 'Next Page', state = 'Disabled')
        self.next_page_button.grid(row=0, column=0, padx=20, pady=20)

        self.title_content.configure(state="disabled")
        self.author_entry.configure(state="disabled")
        self.abstract_content.configure(state="disabled")
        self.subtopic1_subtopic_content.configure(state="disabled")
        self.subtopic1_data_entry_content1.configure(state="disabled")
        self.subtopic1_data_entry_content2.configure(state="disabled")
        self.subtopic1_data_entry_content3.configure(state="disabled")
        self.subtopic1_textbox_content.configure(state="disabled")
        self.subtopic2_subtopic_content.configure(state="disabled")
        self.subtopic2_data_entry_content1.configure(state="disabled")
        self.subtopic2_data_entry_content2.configure(state="disabled")
        self.subtopic2_data_entry_content3.configure(state="disabled")
        self.subtopic2_textbox_content.configure(state="disabled")
        self.subtopic3_subtopic_content.configure(state="disabled")
        self.subtopic3_data_entry_content1.configure(state="disabled")
        self.subtopic3_data_entry_content2.configure(state="disabled")
        self.subtopic3_data_entry_content3.configure(state="disabled")
        self.subtopic3_textbox_content.configure(state="disabled")

        self.window.mainloop()

    def get_course_index(self):
        return self.course_index

    def set_course_index(self, course_index):
        self.course_index = course_index

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def setup_tab_design(self, tab_name):
        if tab_name == "Subtopic 1":
            self.setup_subtopic1_design(self.tabview.tab(tab_name), tab_name)
        elif tab_name == "Subtopic 2":
            self.setup_subtopic2_design(self.tabview.tab(tab_name), tab_name)
        elif tab_name == "Subtopic 3":
            self.setup_subtopic3_design(self.tabview.tab(tab_name), tab_name)
    def setup_subtopic1_design(self, tab, num):
        self.tabview.tab(num).grid_columnconfigure((0, 1, 2), weight=1)  # configure grid of individual tabs

        self.subtopic1_subtopic_content = customtkinter.CTkEntry(tab, placeholder_text="CTkEntry")
        self.subtopic1_subtopic_content.grid(row=0, column=0, columnspan=3, padx=20, pady=(10, 10), sticky="we")


        self.subtopic1_imgLabel1 = Label(tab, image=self.pic1)
        self.subtopic1_imgLabel1.grid(row=1, column=0, sticky="ns")

        self.subtopic1_imgLabel2 = Label(tab, image=self.pic2)
        self.subtopic1_imgLabel2.grid(row=1, column=1, sticky="ns")

        self.subtopic1_imgLabel3 = Label(tab, image=self.pic3)
        self.subtopic1_imgLabel3.grid(row=1, column=2, sticky="ns")

        self.subtopic1_data_entry_content1 = customtkinter.CTkEntry(tab, placeholder_text="CTkEntry", )
        self.subtopic1_data_entry_content1.grid(row=2, column=0, padx=20, pady=(10, 10), sticky="ns")


        self.subtopic1_data_entry_content2 = customtkinter.CTkEntry(tab, placeholder_text="CTkEntry")
        self.subtopic1_data_entry_content2.grid(row=2, column=1, padx=20, pady=(10, 10), sticky="ns")


        self.subtopic1_data_entry_content3 = customtkinter.CTkEntry(tab, placeholder_text="CTkEntry")
        self.subtopic1_data_entry_content3.grid(row=2, column=2, padx=20, pady=(10, 10), sticky="ns")


        self.subtopic1_textbox_content = customtkinter.CTkTextbox(tab)
        self.subtopic1_textbox_content.grid(row=4, column=0, columnspan=3, padx=(20, 20), pady=(20, 20), sticky="nsew")


    def setup_subtopic2_design(self, tab, num):
        self.tabview.tab(num).grid_columnconfigure((0, 1, 2), weight=1)  # configure grid of individual tabs

        self.subtopic2_subtopic_content = customtkinter.CTkEntry(tab, placeholder_text="CTkEntry")
        self.subtopic2_subtopic_content.grid(row=0, column=0, columnspan=3, padx=20, pady=(10, 10), sticky="we")


        self.subtopic2_imgLabel1 = Label(tab, image=self.pic4)
        self.subtopic2_imgLabel1.grid(row=1, column=0, sticky="ns")

        self.subtopic2_imgLabel2 = Label(tab, image=self.pic5)
        self.subtopic2_imgLabel2.grid(row=1, column=1, sticky="ns")

        self.subtopic2_imgLabel3 = Label(tab, image=self.pic6)
        self.subtopic2_imgLabel3.grid(row=1, column=2, sticky="ns")

        self.subtopic2_data_entry_content1 = customtkinter.CTkEntry(tab, placeholder_text="CTkEntry", )
        self.subtopic2_data_entry_content1.grid(row=2, column=0, padx=20, pady=(10, 10), sticky="ns")


        self.subtopic2_data_entry_content2 = customtkinter.CTkEntry(tab, placeholder_text="CTkEntry")
        self.subtopic2_data_entry_content2.grid(row=2, column=1, padx=20, pady=(10, 10), sticky="ns")


        self.subtopic2_data_entry_content3 = customtkinter.CTkEntry(tab, placeholder_text="CTkEntry")
        self.subtopic2_data_entry_content3.grid(row=2, column=2, padx=20, pady=(10, 10), sticky="ns")


        self.subtopic2_textbox_content = customtkinter.CTkTextbox(tab)
        self.subtopic2_textbox_content.grid(row=4, column=0, columnspan=3, padx=(20, 20), pady=(20, 20), sticky="nsew")


    def setup_subtopic3_design(self, tab, num):
        self.tabview.tab(num).grid_columnconfigure((0, 1, 2), weight=1)  # configure grid of individual tabs

        self.subtopic3_subtopic_content = customtkinter.CTkEntry(tab, placeholder_text="CTkEntry")
        self.subtopic3_subtopic_content.grid(row=0, column=0, columnspan=3, padx=20, pady=(10, 10), sticky="we")


        self.subtopic3_imgLabel1 = Label(tab, image=self.pic7)
        self.subtopic3_imgLabel1.grid(row=1, column=0, sticky="ns")

        self.subtopic3_imgLabel2 = Label(tab, image=self.pic8)
        self.subtopic3_imgLabel2.grid(row=1, column=1, sticky="ns")

        self.subtopic3_imgLabel3 = Label(tab, image=self.pic9)
        self.subtopic3_imgLabel3.grid(row=1, column=2, sticky="ns")

        self.subtopic3_data_entry_content1 = customtkinter.CTkEntry(tab, placeholder_text="CTkEntry", )
        self.subtopic3_data_entry_content1.grid(row=2, column=0, padx=20, pady=(10, 10), sticky="ns")


        self.subtopic3_data_entry_content2 = customtkinter.CTkEntry(tab, placeholder_text="CTkEntry")
        self.subtopic3_data_entry_content2.grid(row=2, column=1, padx=20, pady=(10, 10), sticky="ns")

        self.subtopic3_data_entry_content3 = customtkinter.CTkEntry(tab, placeholder_text="CTkEntry")
        self.subtopic3_data_entry_content3.grid(row=2, column=2, padx=20, pady=(10, 10), sticky="ns")

        self.subtopic3_textbox_content = customtkinter.CTkTextbox(tab)
        self.subtopic3_textbox_content.grid(row=4, column=0, columnspan=3, padx=(20, 20), pady=(20, 20), sticky="nsew")


    def content_to_menu(self):
        from main import Instructor_Landing_Page
        self.window.destroy()
        print(self.username)
        Instructor_Landing_Page(self.slp, self.username, self.ins)
