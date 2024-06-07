# from courses import App
import tkinter as tk
from Database import *
import tkinter.messagebox as messagebox
from PIL import Image, ImageTk
from tkinter import font as tkFont
import customtkinter
import datetime
from Database import *
from tkinter import Label
from tkinter import filedialog
from PIL import Image, ImageTk
import customtkinter
from quiz import Test



customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")
img = Image.open('bg.jpg')
class SelfLearningPlatform:
    def __init__(self):
        # self.myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        # self.slp_database = self.myclient["Self_Learning_Platform"]
        # self.user_info = self.slp_database["user_info"]
        self.instructor_info = None
    def get_curr_screen_geometry(self):
        """
        Workaround to get the size of the current screen in a multi-screen setup.

        Returns:
            geometry (str): The standard Tk geometry string.
                [width]x[height]+[left]+[top]
        """
        root = tk.Tk()
        root.update_idletasks()
        root.attributes('-fullscreen', True)
        root.state('iconic')
        geometry = root.winfo_geometry()
        root.destroy()
        print(geometry)
        return geometry

    def create_user_info(self, username, password, email, gender, role):
        user_information = {"username": f"{username}",
                            "password": f"{password}",
                            "email": f"{email}",
                            "gender": f"{gender}",
                            "role": f"{role}", }
        return user_information

    def insert_into_user_info(self, object):
        self.user_info.insert_one(object)

    def show_page(self, page):
        page.tkraise()

    def login_to_registration(self, window):
        window.destroy()
        RegistrationPage(self)

    def registration_to_login(self, window):
        window.destroy()
        LoginPage(self)

    def login_to_menu(self,slp, window, username, ins):
        window.destroy()
        Instructor_Landing_Page(slp, username, ins)

    def menu_to_course(self,slp, window, ins):
        window.destroy()
        Course_Page(slp, ins)

    def course_to_create(self, slp, window, course_name, course_date, ins):
        print(self.instructor_info)
        window.destroy()
        course = Course(course_name, course_date, self.instructor_info)
        course.create_course_info()
        course_info = course.search_by_course_name()
        print(course_info)
        App(slp, course_info, ins)

    def registration_validation(self, username, password, email, gender, role):
        ins = Instructor(username, password, email, gender, role)
        result = ins.search_by_username()
        print(result)
        try:
            if result != []:
                raise Exception("The username has already been registered")
            if any(ch.isdigit() for ch in username):
                raise Exception("Only strings are allowed for the username")
            ins.create_instructor_account()
            messagebox.showinfo('Message', "Account has been added successfully")
        except Exception as e:
            messagebox.showerror('Error', str(e))

    def login_validation(self, slp, window, password, username, role):
        ins = Instructor(username=username, password= password, role= role)
        result = ins.login_confirmation()
        try:
            if result[0] != []:
                messagebox.showinfo('Message', "Login is successful")
                print(result[0])
                self.instructor_info = result[0]
                self.login_to_menu(slp, window, username, ins)

            else:
                raise Exception("The input is invalid")  # Raise exception if no matching user is found
        except Exception as e:
            messagebox.showerror('Error', str(e))






class RegistrationPage:
    def __init__(self, slp):
        self.slp = slp
        # self.width = "1920"
        # self.height = "1080"
        self.window = tk.Tk()
        self.window.title('Registration Page')
        # Get the screen width and height
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()

        # Calculate the center position of the screen
        center_x = screen_width // 2
        center_y = screen_height // 2

        # Set the window size and position
        self.window.geometry(
            f"{screen_width}x{screen_height - 75}+{center_x - screen_width // 2}+{center_y - screen_height // 2}")
        self.window.resizable(False, False)
        bg = Image.open("bg.jpg")
        bg = bg.resize((screen_width, screen_height))
        self.background_image = ImageTk.PhotoImage(bg, master=self.window)
        image_label = tk.Label(self.window, image=self.background_image)
        image_label.place(x=0, y=0)

        registration_frame = tk.Frame(self.window, bg="white")
        registration_frame.place(relx=0.5, rely=0.5, anchor="center")
        registration_frame.grid_columnconfigure((0,1), weight = 1)
        registration_frame.grid_rowconfigure((0,1,2,3), weight = 1)
        # width_length = 1200 / 2
        # height_length = 700 / 2


        username_lbl = customtkinter.CTkLabel(master=registration_frame, text="Username")
        username_lbl.grid(row = 0, column = 0, padx = (400, 20), pady = (100, 20))
        username_txt = customtkinter.CTkEntry(master=registration_frame)
        username_txt.grid(row = 0, column = 1, padx = (20, 400), pady = (100, 20))
        password_lbl = customtkinter.CTkLabel(master=registration_frame, text="Password")
        password_lbl.grid(row = 1, column = 0, padx = (400, 20), pady = 20)
        password_txt = customtkinter.CTkEntry(master=registration_frame)
        password_txt.grid(row = 1, column = 1, padx = (20, 400), pady = 20)
        email_lbl = customtkinter.CTkLabel(master=registration_frame, text="Email")
        email_lbl.grid(row = 2, column = 0, padx = (400, 20), pady = 20)
        email_txt = customtkinter.CTkEntry(master=registration_frame)
        email_txt.grid(row = 2, column = 1, padx = (20, 400), pady = 20)
        gender_lbl = customtkinter.CTkLabel(master=registration_frame, text = "Gender")
        gender_lbl.grid(row = 3, column = 0, padx = (400, 20), pady = 20)
        gender_combo = customtkinter.CTkComboBox(master=registration_frame, values=["Male", "Female"])
        gender_combo.grid(row = 3, column = 1, padx = (20, 400), pady = 20)
        role_lbl = customtkinter.CTkLabel(master=registration_frame, text="Role")
        role_lbl.grid(row = 4, column = 0, padx = (400, 20), pady = (20, 100))
        role_combo = customtkinter.CTkComboBox(master=registration_frame, values=["Learner", "Instructor"])
        role_combo.grid(row = 4, column = 1, padx = (20, 400), pady = (20,100))

        register_btn = customtkinter.CTkButton(master=registration_frame, text='Register',
                                 command=lambda: self.slp.registration_validation(
                                                                                  username_txt.get(),
                                                                                  password_txt.get(),
                                                                                  email_txt.get(),
                                                                                  gender_combo.get(),
                                                                                  role_combo.get()))
        register_btn.grid(row = 5, column = 0, columnspan = 2, pady = 20)

        login_btn = customtkinter.CTkButton(master=registration_frame, text='Login',
                             command=lambda: self.slp.registration_to_login(self.window))
        login_btn.grid(row = 6, column = 0 , columnspan = 2, pady = 20)

        self.window.mainloop()

class LoginPage:
    def __init__(self, slp):
        self.slp = slp
        # self.width = "1920"
        # self.height = "1080"
        self.window = tk.Tk()
        # Get the screen width and height
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()

        # Calculate the center position of the screen
        center_x = screen_width // 2
        center_y = screen_height // 2

        # Set the window size and position
        self.window.geometry(f"{screen_width}x{screen_height - 75}+{center_x - screen_width // 2}+{center_y - screen_height // 2}")
        self.window.title('Login Page')
        # self.window.geometry(f"{self.width}x{self.height}")
        self.window.resizable(False, False)
        bg = Image.open("bg.jpg")
        bg = bg.resize((screen_width, screen_height))
        self.background_image = ImageTk.PhotoImage(bg, master=self.window)
        image_label = tk.Label(self.window, image=self.background_image)
        image_label.place(x=0, y=0)

        login_frame = customtkinter.CTkFrame(self.window, width=1200, height=700)
        login_frame.place(relx=0.5, rely=0.5, anchor="center")


        # self.string = tk.StringVar()
        password_lbl = customtkinter.CTkLabel(master=login_frame, text="Password", width=100, height=30)
        password_lbl.place(x=400, y=250)
        password_txt = customtkinter.CTkEntry(master=login_frame, width=200, height=30)
        password_txt.place(x=500, y=250)
        username_lbl = customtkinter.CTkLabel(master=login_frame, text="Username", width=100, height=30)
        username_lbl.place(x=400, y=200)
        username_txt = customtkinter.CTkEntry(master=login_frame, width=200, height=30)
        username_txt.place(x=500, y= 200)
        role_lbl = customtkinter.CTkLabel(master=login_frame, text="Role: ", width=100, height=30)
        role_lbl.place(x=400, y=300)
        role_combo = customtkinter.CTkComboBox(master=login_frame, values=["Learner", "Instructor"], width=200, height=30)
        role_combo.place(x=500, y=300)

        login_btn = customtkinter.CTkButton(master=login_frame, text='Login',
                              command=lambda: self.slp.login_validation(self.slp,
                                                                        self.window,
                                                                        password_txt.get(),
                                                                        username_txt.get(),
                                                                        role_combo.get()),
                                                                        width=100, height=30)
        login_btn.place(x= 550, y= 350)

        register_btn = customtkinter.CTkButton(master=login_frame, text='Register',
                                 command=lambda: self.slp.login_to_registration(self.window),  width=100, height=30)
        register_btn.place(x= 550, y=400)

        self.window.mainloop()


class Instructor_Landing_Page:
    def __init__(self,slp, username, ins):
        self.ins = ins
        self.slp = slp
        self.username = username

        self.window = tk.Tk()
        self.window.title('Instructor Main Page')

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

        # retreiving images for the image buttons
        self.add_image = Image.open('add_img.jpg')
        self.add_image = self.add_image.resize((200,200))
        self.resized_add_image = ImageTk.PhotoImage(self.add_image)

        self.record_image = Image.open('record_img.png')
        self.record_image = self.record_image.resize((200,200))
        self.resized_record_image = ImageTk.PhotoImage(self.record_image)

        # creating image buttons

        self.add_button = tk.Button(self.main_frame, text = 'Create Courses', image=self.resized_add_image, compound= 'top', bg = 'grey', font=font_obj.get_font(36), command = lambda: self.slp.menu_to_course(slp, self.window, ins))
        self.add_button.grid(row = 1, column = 1,padx=(40, 40), pady=(20, 20), sticky = 'e')
        self.record_button = tk.Button(self.main_frame,  text = 'View Courses', image=self.resized_record_image, compound= 'top', bg = 'grey', font=font_obj.get_font(36))
        self.record_button.grid(row=1, column=2,padx=(40, 40), pady=(20, 20), sticky = 'w')

        self.window.mainloop()

class Course_Page:
    def __init__(self,slp, ins):
        self.slp = slp
        self.ins = ins
        self.username = ins.get_username()
        self.window = tk.Tk()
        self.window.title('Create Course Page')

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

        self.course_name_lbl = customtkinter.CTkLabel(master=self.window, text="Course Name: ")
        self.course_name_lbl.grid(row = 0, column = 0, padx = 20, pady = 20)

        self.course_name_txt = customtkinter.CTkEntry(master=self.window)
        self.course_name_txt.grid(row = 1, column = 0 , padx = 20, pady = 20, sticky = 'ew')

        self.course_date_lbl = customtkinter.CTkLabel(master=self.window, text="Course Date: ")
        self.course_date_lbl.grid(row=2, column=0, padx=20, pady=20)

        self.course_date_txt = customtkinter.CTkEntry(master=self.window, placeholder_text= "YYYY-MM-DD")
        self.course_date_txt.grid(row=3, column=0, padx=20, pady=20, sticky = 'ew')

        def create_course():
            # Get the values from the text boxes
            course_name = self.course_name_txt.get()
            course_date_str = self.course_date_txt.get()

            # Convert the date string to a datetime object
            try:
                course_date = datetime.datetime.strptime(course_date_str, "%Y-%m-%d").date()
                self.slp.course_to_create(slp, self.window, course_name, course_date, self.ins)
            except ValueError:
                # Handle the case where the date format is invalid
                messagebox.showerror("Error", "Invalid date format. Please use the format YYYY-MM-DD.")
                return

        # creating image buttons

        self.confirm_button = customtkinter.CTkButton(self.window, text = 'Confirm', command = lambda: create_course())
        self.confirm_button.grid(row = 4, column = 1,padx=(40, 40), pady=(20, 20), sticky = 'e')

        self.window.mainloop()

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):
    def __init__(self,slp, course, ins):
        self.slp = slp
        self.course_info = course
        self.window = customtkinter.CTk()
        super().__init__()
        self.ins = ins
        self.username = ins.get_username()
        img = Image.open('bg.jpg')

        img_1 = img.resize((400, 150))
        self.page_number = 1
        self.pic1 = ImageTk.PhotoImage(img_1)
        self.pic2 = ImageTk.PhotoImage(img_1)
        self.pic3 = ImageTk.PhotoImage(img_1)

        # Get the screen width and height
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()

        # Calculate the center position of the screen
        center_x = screen_width // 2
        center_y = screen_height // 2

        # Set the window size and position
        self.window.geometry(f"{screen_width}x{screen_height - 75}+{center_x - screen_width // 2}+{center_y - screen_height // 2}")

        # configure grid layout (4x4)
        self.window.grid_columnconfigure(1, weight=1)
        # self.grid_columnconfigure((2, 3), weight=0)
        self.window.grid_rowconfigure((0,1), weight = 0 )
        self.window.grid_rowconfigure((2,3), weight=1)

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self.window, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=5, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="CustomTkinter", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame,
                                                                       values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))

        # create title, Author, Date:
        self.title_frame = customtkinter.CTkFrame(self.window, corner_radius= 0 )
        self.title_frame.grid(row=0, column=1, padx=(20, 20), pady=(20, 0), sticky="nsew")
        self.title_frame.grid_columnconfigure(0,weight =0)
        self.title_frame.grid_columnconfigure(1,weight= 1)
        self.title_frame.grid_rowconfigure((0,1,2), weight=1)
        self.title_label = customtkinter.CTkLabel(self.title_frame, text="Title:")
        self.title_label.grid(row = 0, column = 0, padx=20, pady=(10, 0), sticky="w")
        self.title_entry = customtkinter.CTkEntry(self.title_frame, placeholder_text="CTkEntry")
        self.title_entry.grid(row = 0, column = 1, padx=20, pady=(10, 0), sticky = 'we')
        self.author_label = customtkinter.CTkLabel(self.title_frame, text="Author:")
        self.author_label.grid(row = 1, column = 0, padx=20, pady=(10, 0), sticky="w")
        self.author_entry = customtkinter.CTkEntry(self.title_frame, placeholder_text="CTkEntry")
        self.author_entry.grid(row = 1, column = 1, padx=20, pady=(10, 0), sticky="we")
        # self.date_label = customtkinter.CTkLabel(self.title_frame, text="Date:")
        # self.date_label.grid(row = 2, column = 0, padx=20, pady=(10, 0), sticky="w")
        # self.date_entry = customtkinter.CTkEntry(self.title_frame, placeholder_text="CTkEntry")
        # self.date_entry.grid(row = 2, column = 1, padx=20, pady=(10, 10), sticky="we")

        # create an abstract frame
        self.abtract_frame = customtkinter.CTkFrame(self.window, corner_radius= 0)
        self.abtract_frame.grid(row=1, column=1, padx=(20, 20), pady=(20, 0), sticky="nsew")
        self.abtract_frame.grid_columnconfigure(0, weight = 1)
        self.abtract_label = customtkinter.CTkLabel(self.abtract_frame, text="Abtract:")
        self.abtract_label.grid(row=0, column=0, padx=20, pady=(10, 0), sticky="w")
        self.abstract_textbox = customtkinter.CTkTextbox(self.abtract_frame ,height= 100)
        self.abstract_textbox.grid(row=1, column=0, padx=(20, 20), pady=(20, 20), sticky="nsew")

        # create tabview
        self.tabview = customtkinter.CTkTabview(self.window)
        self.tabview.grid(row=2, column=1, padx=(20, 20), pady=(0, 0), sticky="nsew")
        self.tabview.add("Subtopic 1")
        self.tabview.add("Subtopic 2")
        self.tabview.add("Subtopic 3")

        # Usage example
        # Call the setup_tab_design function for each tab
        self.setup_tab_design("Subtopic 1", self.pic1)
        self.setup_tab_design("Subtopic 2", self.pic2)
        self.setup_tab_design("Subtopic 3", self.pic3)

        # submit button, add button , create quiz
        self.submit_frame = customtkinter.CTkFrame(self.window, corner_radius= 0)
        self.submit_frame.grid(row= 3, column = 1, padx=(20, 20), pady=(20, 0), sticky="nsew")
        self.submit_frame.grid_columnconfigure((0,1,2), weight=1)
        self.submit_button = customtkinter.CTkButton(self.submit_frame, text='Submit', command = lambda : self.captureData(self.course_info))
        self.submit_button.grid(row=0, column=2, padx=20, pady=20)
        self.add_button = customtkinter.CTkButton(self.submit_frame, text='Add', command = lambda :self.clear_tab_contents())
        self.add_button.grid(row=0, column=1, padx=20, pady=20)
        self.create_quiz_button = customtkinter.CTkButton(self.submit_frame, text='Create Quiz', command = lambda : self.menu_to_none(self.window))
        self.create_quiz_button.grid(row=0, column=0, padx=20, pady=20)

        # # set default values
        self.appearance_mode_optionemenu.set("Dark")

        self.window.mainloop()

    def open_input_dialog_event(self):
        dialog = customtkinter.CTkInputDialog(text="Type in a number:", title="CTkInputDialog")
        print("CTkInputDialog:", dialog.get_input())

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def sidebar_button_event(self):
        print("sidebar_button click")

    # image uploader function
    def imageUploader(self, lbl):
        fileTypes = [("Image files", "*.png;*.jpg;*.jpeg")]
        path = tk.filedialog.askopenfilename(filetypes=fileTypes)

        # if file is selected
        if len(path):
            img = Image.open(path)
            img = img.resize((400, 150))
            pic = ImageTk.PhotoImage(img)

            # re-sizing the app window in order to fit picture
            # and buttom
            lbl.config(image=pic)
            lbl.image = pic


        # if no file is selected, then we are displaying below message
        else:
            print("No file is Choosen !! Please choose a file.")

    def setup_subtopic1_design(self, tab, num, img):
        self.tabview.tab(num).grid_columnconfigure((0, 1, 2, 3), weight=1)  # configure grid of individual tabs

        self.subtopic1_subtopic_entry = customtkinter.CTkEntry(tab, placeholder_text="CTkEntry")
        self.subtopic1_subtopic_entry.grid(row=0, column=0, columnspan=3, padx=20, pady=(10, 10), sticky="we")

        self.subtopic1_imgLabel1 = Label(tab, image=img)
        self.subtopic1_imgLabel1.grid(row=1, column=0, sticky="ns")

        self.subtopic1_imgLabel2 = Label(tab, image=img)
        self.subtopic1_imgLabel2.grid(row=1, column=1, sticky="ns")

        self.subtopic1_imgLabel3 = Label(tab, image=img)
        self.subtopic1_imgLabel3.grid(row=1, column=2, sticky="ns")

        self.subtopic1_data_entry1 = customtkinter.CTkEntry(tab, placeholder_text="CTkEntry", )
        self.subtopic1_data_entry1.grid(row=2, column=0, padx=20, pady=(10, 10), sticky="ns")

        self.subtopic1_data_entry2 = customtkinter.CTkEntry(tab, placeholder_text="CTkEntry")
        self.subtopic1_data_entry2.grid(row=2, column=1, padx=20, pady=(10, 10), sticky="ns")

        self.subtopic1_data_entry3 = customtkinter.CTkEntry(tab, placeholder_text="CTkEntry")
        self.subtopic1_data_entry3.grid(row=2, column=2, padx=20, pady=(10, 10), sticky="ns")

        self.subtopic1_upload_button1 = customtkinter.CTkButton(tab, text='Upload',
                                                      command=lambda: self.imageUploader(self.subtopic1_imgLabel1))
        self.subtopic1_upload_button1.grid(row=3, column=0, padx=20, pady=10, sticky="ns")

        self.subtopic1_upload_button2 = customtkinter.CTkButton(tab, text='Upload',
                                                      command=lambda: self.imageUploader(self.subtopic1_imgLabel2))
        self.subtopic1_upload_button2.grid(row=3, column=1, padx=20, pady=10, sticky="ns")

        self.subtopic1_upload_button3 = customtkinter.CTkButton(tab, text='Upload',
                                                      command=lambda: self.imageUploader(self.subtopic1_imgLabel3))
        self.subtopic1_upload_button3.grid(row=3, column=2, padx=20, pady=10, sticky="ns")

        self.subtopic1_textbox = customtkinter.CTkTextbox(tab)
        self.subtopic1_textbox.grid(row=4, column=0, columnspan=3, padx=(20, 20), pady=(20, 20), sticky="nsew")

    def setup_subtopic2_design(self, tab, num, img):
        self.tabview.tab(num).grid_columnconfigure((0, 1, 2, 3), weight=1)  # configure grid of individual tabs

        self.subtopic2_subtopic_entry = customtkinter.CTkEntry(tab, placeholder_text="CTkEntry")
        self.subtopic2_subtopic_entry.grid(row=0, column=0, columnspan=3, padx=20, pady=(10, 10), sticky="we")

        self.subtopic2_imgLabel1 = Label(tab, image=img)
        self.subtopic2_imgLabel1.grid(row=1, column=0, sticky="ns")

        self.subtopic2_imgLabel2 = Label(tab, image=img)
        self.subtopic2_imgLabel2.grid(row=1, column=1, sticky="ns")

        self.subtopic2_imgLabel3 = Label(tab, image=img)
        self.subtopic2_imgLabel3.grid(row=1, column=2, sticky="ns")

        self.subtopic2_data_entry1 = customtkinter.CTkEntry(tab, placeholder_text="CTkEntry", )
        self.subtopic2_data_entry1.grid(row=2, column=0, padx=20, pady=(10, 10), sticky="ns")

        self.subtopic2_data_entry2 = customtkinter.CTkEntry(tab, placeholder_text="CTkEntry")
        self.subtopic2_data_entry2.grid(row=2, column=1, padx=20, pady=(10, 10), sticky="ns")

        self.subtopic2_data_entry3 = customtkinter.CTkEntry(tab, placeholder_text="CTkEntry")
        self.subtopic2_data_entry3.grid(row=2, column=2, padx=20, pady=(10, 10), sticky="ns")

        self.subtopic2_upload_button1 = customtkinter.CTkButton(tab, text='Upload',
                                                      command=lambda: self.imageUploader(self.subtopic2_imgLabel1))
        self.subtopic2_upload_button1.grid(row=3, column=0, padx=20, pady=10, sticky="ns")

        self.subtopic2_upload_button2 = customtkinter.CTkButton(tab, text='Upload',
                                                      command=lambda: self.imageUploader(self.subtopic2_imgLabel2))
        self.subtopic2_upload_button2.grid(row=3, column=1, padx=20, pady=10, sticky="ns")

        self.subtopic2_upload_button3 = customtkinter.CTkButton(tab, text='Upload',
                                                      command=lambda: self.imageUploader(self.subtopic2_imgLabel3))
        self.subtopic2_upload_button3.grid(row=3, column=2, padx=20, pady=10, sticky="ns")

        self.subtopic2_textbox = customtkinter.CTkTextbox(tab)
        self.subtopic2_textbox.grid(row=4, column=0, columnspan=3, padx=(20, 20), pady=(20, 20), sticky="nsew")

    def setup_subtopic3_design(self, tab, num, img):
        self.tabview.tab(num).grid_columnconfigure((0, 1, 2, 3), weight=1)  # configure grid of individual tabs

        self.subtopic3_subtopic_entry = customtkinter.CTkEntry(tab, placeholder_text="CTkEntry")
        self.subtopic3_subtopic_entry.grid(row=0, column=0, columnspan=3, padx=20, pady=(10, 10), sticky="we")

        self.subtopic3_imgLabel1 = Label(tab, image=img)
        self.subtopic3_imgLabel1.grid(row=1, column=0, sticky="ns")

        self.subtopic3_imgLabel2 = Label(tab, image=img)
        self.subtopic3_imgLabel2.grid(row=1, column=1, sticky="ns")

        self.subtopic3_imgLabel3 = Label(tab, image=img)
        self.subtopic3_imgLabel3.grid(row=1, column=2, sticky="ns")

        self.subtopic3_data_entry1 = customtkinter.CTkEntry(tab, placeholder_text="CTkEntry", )
        self.subtopic3_data_entry1.grid(row=2, column=0, padx=20, pady=(10, 10), sticky="ns")

        self.subtopic3_data_entry2 = customtkinter.CTkEntry(tab, placeholder_text="CTkEntry")
        self.subtopic3_data_entry2.grid(row=2, column=1, padx=20, pady=(10, 10), sticky="ns")

        self.subtopic3_data_entry3 = customtkinter.CTkEntry(tab, placeholder_text="CTkEntry")
        self.subtopic3_data_entry3.grid(row=2, column=2, padx=20, pady=(10, 10), sticky="ns")

        self.subtopic3_upload_button1 = customtkinter.CTkButton(tab, text='Upload',
                                                      command=lambda: self.imageUploader(self.subtopic3_imgLabel1))
        self.subtopic3_upload_button1.grid(row=3, column=0, padx=20, pady=10, sticky="ns")

        self.subtopic3_upload_button2 = customtkinter.CTkButton(tab, text='Upload',
                                                      command=lambda: self.imageUploader(self.subtopic3_imgLabel2))
        self.subtopic3_upload_button2.grid(row=3, column=1, padx=20, pady=10, sticky="ns")

        self.subtopic3_upload_button3 = customtkinter.CTkButton(tab, text='Upload',
                                                      command=lambda: self.imageUploader(self.subtopic3_imgLabel3))
        self.subtopic3_upload_button3.grid(row=3, column=2, padx=20, pady=10, sticky="ns")

        self.subtopic3_textbox = customtkinter.CTkTextbox(tab)
        self.subtopic3_textbox.grid(row=4, column=0, columnspan=3, padx=(20, 20), pady=(20, 20), sticky="nsew")

    def setup_tab_design(self, tab_name, img):
        if tab_name == "Subtopic 1":
            self.setup_subtopic1_design(self.tabview.tab(tab_name), tab_name, img)
        elif tab_name == "Subtopic 2":
            self.setup_subtopic2_design(self.tabview.tab(tab_name), tab_name, img)
        elif tab_name == "Subtopic 3":
            self.setup_subtopic3_design(self.tabview.tab(tab_name), tab_name, img)

    def captureData(self, course_info):
        title_entry = self.title_entry.get()
        author_entry = self.author_entry.get()
        # date_entry = self.date_entry.get()
        abstract_entry = self.abstract_textbox.get("1.0", "end-1c")
        print(title_entry)
        print(author_entry)
        # print(date_entry)
        print(abstract_entry)
        # Retrieve data from each input field in all tabs
        data = []
        for tab_num in ["Subtopic 1", "Subtopic 2", "Subtopic 3"]:
            tab = self.tabview.tab(tab_num)
            subtopic_entry = tab.grid_slaves(row=0, column=0)[0]
            data_entry1 = tab.grid_slaves(row=2, column=0)[0]
            data_entry2 = tab.grid_slaves(row=2, column=1)[0]
            data_entry3 = tab.grid_slaves(row=2, column=2)[0]
            textbox = tab.grid_slaves(row=4, column=0)[0]

            subtopic = subtopic_entry.get()
            entry1 = data_entry1.get()
            entry2 = data_entry2.get()
            entry3 = data_entry3.get()
            text = textbox.get("1.0", "end-1c")

            data.append((subtopic, entry1, entry2, entry3, text))
        tabview1_tuple = data[0]
        tabview2_tuple = data[1]
        tabview3_tuple = data[2]


        tabview1_subtopic_entry = tabview1_tuple[0]
        tabview1_data_entry1 = tabview1_tuple[1]
        tabview1_data_entry2 = tabview1_tuple[2]
        tabview1_data_entry3 = tabview1_tuple[3]
        tabview1_textbox = tabview1_tuple[4]
        tabview2_subtopic_entry = tabview2_tuple[0]
        tabview2_data_entry1 = tabview2_tuple[1]
        tabview2_data_entry2 = tabview2_tuple[2]
        tabview2_data_entry3 = tabview2_tuple[3]
        tabview2_textbox = tabview2_tuple[4]
        tabview3_subtopic_entry = tabview3_tuple[0]
        tabview3_data_entry1 = tabview3_tuple[1]
        tabview3_data_entry2 = tabview3_tuple[2]
        tabview3_data_entry3 = tabview3_tuple[3]
        tabview3_textbox = tabview3_tuple[4]
        course_page = Course_page(self.page_number, title_entry, author_entry, abstract_entry, tabview1_subtopic_entry, tabview1_data_entry1,  tabview1_data_entry2, tabview1_data_entry3, tabview1_textbox,
                                  tabview2_subtopic_entry, tabview2_data_entry1, tabview2_data_entry2, tabview2_data_entry3, tabview2_textbox, tabview3_subtopic_entry, tabview3_data_entry1,
                                  tabview3_data_entry2, tabview3_data_entry3, tabview3_textbox, self.course_info)
        course_page.create_course_page_info()
        messagebox.showinfo('Message', "Course Added Successfully")
        self.create_to_menu(self.window)






    def clear_tab_contents(self):


        for tab_num in ["Subtopic 1", "Subtopic 2", "Subtopic 3"]:
            tab = self.tabview.tab(tab_num)
            subtopic_entry = tab.grid_slaves(row=0, column=0)[0]
            data_entry1 = tab.grid_slaves(row=2, column=0)[0]
            data_entry2 = tab.grid_slaves(row=2, column=1)[0]
            data_entry3 = tab.grid_slaves(row=2, column=2)[0]
            textbox = tab.grid_slaves(row=4, column=0)[0]

            subtopic_entry.delete(0, "end")
            data_entry1.delete(0, "end")
            data_entry2.delete(0, "end")
            data_entry3.delete(0, "end")
            textbox.delete("1.0", "end-1c")


    def menu_to_none(self, window):
        window.destroy()
        Test()

    def add_new_topic(self, window):
        window.destroy()
        App()

    def create_to_menu(self, window):
        window.destroy()
        Instructor_Landing_Page(self.slp, self.username, self.ins)

class Font:
    def get_font(self, size):
        helv = tkFont.Font(family='Helvetica', size=size, weight='bold')
        return helv

if __name__ == '__main__':
    slp = SelfLearningPlatform()
    print(slp.get_curr_screen_geometry())
    LoginPage(slp)




