from courses import App
import tkinter as tk
from Database import Database, Instructor
import tkinter.messagebox as messagebox
from PIL import Image, ImageTk
from tkinter import font as tkFont
import customtkinter

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")
img = Image.open('bg.jpg')
class SelfLearningPlatform:
    # def __init__(self):
    #     # self.myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    #     # self.slp_database = self.myclient["Self_Learning_Platform"]
    #     # self.user_info = self.slp_database["user_info"]

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

    def login_to_menu(self, window, username):
        window.destroy()
        Instructor_Landing_Page(username)

    def menu_to_create(self, window):
        window.destroy()
        App()

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

    def login_validation(self, window, password, username, role):
        ins = Instructor(username=username, password= password, role= role)
        result = ins.login_confirmation()
        try:
            if result != []:
                messagebox.showinfo('Message', "Login is successful")
                self.login_to_menu(window, username)
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
                              command=lambda: self.slp.login_validation(self.window,
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
    def __init__(self, username):
        self.slp = SelfLearningPlatform()
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

        self.add_button = tk.Button(self.main_frame, text = 'Create Courses', image=self.resized_add_image, compound= 'top', bg = 'grey', font=font_obj.get_font(36), command = lambda: self.slp.menu_to_create(self.window))
        self.add_button.grid(row = 1, column = 1,padx=(40, 40), pady=(20, 20), sticky = 'e')
        self.record_button = tk.Button(self.main_frame,  text = 'View Courses', image=self.resized_record_image, compound= 'top', bg = 'grey', font=font_obj.get_font(36))
        self.record_button.grid(row=1, column=2,padx=(40, 40), pady=(20, 20), sticky = 'w')

        # # creating labels for the buttons
        # self.add_label = customtkinter.CTkLabel(self.main_frame, text="Create Course")
        # self.add_label.grid(row=2, column=1, padx=(40, 40), pady=(20, 20), sticky = 'e')
        # self.view_label = customtkinter.CTkLabel(self.main_frame, text="View Course")
        # self.view_label.grid(row=2, column=2, padx=(40, 40), pady=(20, 20), sticky = 'w')

        self.window.mainloop()


class Font:
    def get_font(self, size):
        helv = tkFont.Font(family='Helvetica', size=size, weight='bold')
        return helv

if __name__ == '__main__':
    slp = SelfLearningPlatform()
    print(slp.get_curr_screen_geometry())
    LoginPage(slp)




