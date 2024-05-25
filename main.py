from courses import App
import customtkinter
import tkinter as tk
import pymongo
from tkinter import ttk
import tkinter.messagebox as messagebox
from PIL import Image, ImageTk

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")
img = Image.open('bg.jpg')
class SelfLearningPlatform:
    def __init__(self):
        self.myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        self.slp_database = self.myclient["Self_Learning_Platform"]
        self.user_info = self.slp_database["user_info"]

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

    def login_to_menu(self, window):
        window.destroy()
        App()

    def menu_to_none(self, window):
        App().destroy()

    def registration_validation(self, username, password, email, gender, role):
        user_list = list(self.user_info.find())
        try:
            if len(user_list)>0:
                for user in user_list:
                    if user['username'] == username:
                        raise Exception("The username has already been registered")
                        #break
            if any(ch.isdigit() for ch in username):
                raise Exception("Only strings are allowed for the username")
            self.user_info.insert_one(self.create_user_info(username, password, email, gender, role))
            messagebox.showinfo('Message', "Account has been added successfully")
        except Exception as e:
            messagebox.showerror('Error', str(e))

    def login_validation(self, window, password, username, role):
        user_list = list(self.user_info.find())
        try:
            if len(user_list) > 0:
                for user in user_list:
                    if user['username'] == username and user['password'] == password and user['role'] == role:
                        messagebox.showinfo('Message', "Login is successful")
                        # question_bank = []
                        # for question in question_data:
                        #     choices = []
                        #     question_text = html.unescape(question["question"])
                        #     correct_answer = html.unescape(question["correct_answer"])
                        #     incorrect_answers = question["incorrect_answers"]
                        #     for ans in incorrect_answers:
                        #         choices.append(html.unescape(ans))
                        #     choices.append(correct_answer)
                        #     shuffle(choices)
                        #     new_question = Question(question_text, correct_answer, choices)
                        #     question_bank.append(new_question)
                        # quiz = QuizBrain(question_bank)
                        # quiz_ui = QuizInterface(quiz)
                        # quiz_ui
                        self.login_to_menu(window)

                        return
                raise Exception("The input is invalid")  # Raise exception if no matching user is found
            else:
                raise Exception("There are no registered accounts")
        except Exception as e:
            messagebox.showerror('Error', str(e))




class RegistrationPage:
    def __init__(self, slp):
        self.slp = slp
        self.width = "1920"
        self.height = "1080"
        self.window = tk.Tk()
        self.window.title('Registration Page')
        self.window.geometry(f"{self.width}x{self.height}")
        self.window.resizable(False, False)
        bg = Image.open("bg.jpg")
        bg = bg.resize((1920, 1080))
        self.background_image = ImageTk.PhotoImage(bg, master=self.window)
        image_label = tk.Label(self.window, image=self.background_image)
        image_label.place(x=0, y=0)

        registration_frame = tk.Frame(self.window, width=1200, height=700, bg="white")
        registration_frame.place(relx=0.5, rely=0.5, anchor="center")
        width_length = 1200 / 2
        height_length = 700 / 2

        self.string = tk.StringVar()
        password_lbl = tk.Label(master=registration_frame, text="Password", fg='black', bg='white')
        password_lbl.place(x=width_length - 200, y=height_length - 100, width=100, height=30)
        password_txt = tk.Entry(master=registration_frame, show='x', textvariable=self.string)
        password_txt.place(x=width_length - 100, y=height_length - 100, width=200, height=30)
        username_lbl = tk.Label(master=registration_frame, text="Username", fg='black', bg='white')
        username_lbl.place(x=width_length - 200, y=height_length - 150, width=100, height=30)
        username_txt = tk.Entry(master=registration_frame)
        username_txt.place(x=width_length - 100, y=height_length - 150, width=200, height=30)
        email_lbl = tk.Label(master=registration_frame, text="Email", fg='black', bg='white')
        email_lbl.place(x=width_length - 200, y=height_length - 200, width=100, height=30)
        email_txt = tk.Entry(master=registration_frame)
        email_txt.place(x=width_length - 100, y=height_length - 200, width=200, height=30)
        gender_lbl = tk.Label(master=registration_frame, text="Gender", fg='black', bg='white')
        gender_lbl.place(x=width_length - 200, y=height_length - 250, width=100, height=30)
        gender_combo = ttk.Combobox(master=registration_frame, values=["Male", "Female"])
        gender_combo.place(x=width_length - 100, y=height_length - 250, width=200, height=30)
        role_lbl = tk.Label(master=registration_frame, text="Role", fg='black', bg='white')
        role_lbl.place(x=width_length - 200, y=height_length - 300, width=100, height=30)
        role_combo = ttk.Combobox(master=registration_frame, values=["Learner", "Instructor"])
        role_combo.place(x=width_length - 100, y=height_length - 300, width=200, height=30)

        register_btn = tk.Button(master=registration_frame, text='Register',
                                 command=lambda: self.slp.registration_validation(
                                                                                  username_txt.get(),
                                                                                  password_txt.get(),
                                                                                  email_txt.get(),
                                                                                  gender_combo.get(),
                                                                                  role_combo.get()))
        register_btn.place(x=width_length - 100, y=height_length - 50, width=200, height=30)

        back_btn = tk.Button(master=registration_frame, text='Back',
                             command=lambda: self.slp.registration_to_login(self.window))
        back_btn.place(x=width_length + 100, y=height_length + 200, width=100, height=30)

        self.window.mainloop()

class LoginPage:
    def __init__(self, slp):
        self.slp = slp
        self.width = "1920"
        self.height = "1080"
        self.window = tk.Tk()
        self.window.title('Login Page')
        self.window.geometry(f"{self.width}x{self.height}")
        self.window.resizable(False, False)
        bg = Image.open("bg.jpg")
        bg = bg.resize((1920, 1080))
        self.background_image = ImageTk.PhotoImage(bg, master=self.window)
        image_label = tk.Label(self.window, image=self.background_image)
        image_label.place(x=0, y=0)

        login_frame = tk.Frame(self.window, width=1200, height=700, bg="white")
        login_frame.place(relx=0.5, rely=0.5, anchor="center")
        width_length = 1200 / 2
        height_length = 700 / 2

        self.string = tk.StringVar()
        password_lbl = tk.Label(master=login_frame, text="Password", fg='black', bg='white')
        password_lbl.place(x=400, y=250, width=100, height=30)
        password_txt = tk.Entry(master=login_frame, show='x', textvariable=self.string)
        password_txt.place(x=500, y=250, width=200, height=30)
        username_lbl = tk.Label(master=login_frame, text="Username", fg='black', bg='white')
        username_lbl.place(x=400, y=200, width=100, height=30)
        username_txt = tk.Entry(master=login_frame)
        username_txt.place(x=500, y= 200, width=200, height=30)
        role_lbl = tk.Label(master=login_frame, text="Role: ", fg='black', bg='white')
        role_lbl.place(x=400, y=300, width=100, height=30)
        role_combo = ttk.Combobox(master=login_frame, values=["Learner", "Instructor"])
        role_combo.place(x=500, y=300, width=200, height=30)

        login_btn = tk.Button(master=login_frame, text='Login',
                              command=lambda: self.slp.login_validation(self.window,
                                                                        password_txt.get(),
                                                                        username_txt.get(),
                                                                        role_combo.get()))
        login_btn.place(x= 550, y= 350, width=100, height=30)

        register_btn = tk.Button(master=login_frame, text='Register',
                                 command=lambda: self.slp.login_to_registration(self.window))
        register_btn.place(x= 550, y=400,  width=100, height=30)

        self.window.mainloop()

if __name__ == '__main__':
    slp = SelfLearningPlatform()
    print(slp.get_curr_screen_geometry())
    LoginPage(slp)

