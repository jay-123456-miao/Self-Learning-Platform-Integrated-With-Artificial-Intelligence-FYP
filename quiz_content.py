from tkinter import Label, messagebox
from Database import *
import customtkinter
import tkinter.messagebox as messagebox
from learner_menu import *
class Test_Content(customtkinter.CTk):
    def __init__(self, slp, username, ins, quiz_index, quiz_len, quiz_pages_content):
        self.window = customtkinter.CTk()
        super().__init__()

        # self.course_info = course_info
        self.slp = slp
        self.username = username
        self.ins = ins
        self.quiz_index = quiz_index
        self.quiz_len = quiz_len
        selected_quiz_content = quiz_pages_content
        print("Length of the list: ", len(selected_quiz_content))
        print(selected_quiz_content)
        print("quiz index = ", quiz_index)
        quiz_page_content = selected_quiz_content[quiz_index]
        self.quiz_type = quiz_page_content[1]

        # Get the screen width and height
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        print(screen_width)
        print(screen_height)
        # Calculate the center position of the screen
        center_x = screen_width // 2
        center_y = screen_height // 2
        # Set the window size and position
        # Set the window size and position
        self.window.geometry(
            f"{screen_width}x{screen_height - 75}+{center_x - screen_width // 2}+{center_y - screen_height // 2}")
        self.window.title("Test Page")
        self.window.columnconfigure(1, weight = 1)
        self.title_label = tk.Label(self.window, bg = 'green',  text = 'Test Page', fg = 'white', font = ("ariel", 20, "bold"))
        self.title_label.grid(row = 0, column = 0, columnspan = 2 , sticky = 'we')
        self.question_label = tk.Label(self.window, fg='black', font=("ariel", 20, "bold"))
        self.question_label.grid(row=1, column=0, sticky='we')
        self.question_textbox = customtkinter.CTkTextbox(self.window ,height= 100)
        self.question_textbox.grid(row=2, column=0, columnspan = 2, padx=(20, 20), pady=(40, 40), sticky="we")
        self.question_textbox.insert(tk.END, quiz_page_content[3])

        #Creating the radio button frames first
        self.radiobutton_frame = customtkinter.CTkFrame(self.window)
        self.radiobutton_frame.grid_columnconfigure(1, weight=1)
        self.radio_var = tk.StringVar(value = quiz_page_content[5])
        print(quiz_page_content[5])
        self.radio_label_1 = tk.Label(self.radiobutton_frame, text='Choice 1: ', fg='black', font=("ariel", 20, "bold"))
        self.radio_label_1.grid(row=0, column=0)
        self.radio_choice_1 = customtkinter.CTkRadioButton(master=self.radiobutton_frame, variable=self.radio_var, value = quiz_page_content[5], text = quiz_page_content[5])
        self.radio_choice_1.grid(row=0, column=1, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="ew")
        self.radio_label_2 = tk.Label(self.radiobutton_frame, text='Choice 2: ', fg='black', font=("ariel", 20, "bold"))
        self.radio_label_2.grid(row=1, column=0)
        self.radio_choice_2 = customtkinter.CTkRadioButton(master=self.radiobutton_frame, variable=self.radio_var, value = quiz_page_content[6], text = quiz_page_content[6])
        self.radio_choice_2.grid(row=1, column=1, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="ew")
        self.radio_label_3 = tk.Label(self.radiobutton_frame, text='Choice 3: ', fg='black', font=("ariel", 20, "bold"))
        self.radio_label_3.grid(row=2, column=0)
        self.radio_choice_3 = customtkinter.CTkRadioButton(master=self.radiobutton_frame, variable=self.radio_var, value = quiz_page_content[7], text = quiz_page_content[7])
        self.radio_choice_3.grid(row=2, column=1, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="ew")
        self.radio_label_4 = tk.Label(self.radiobutton_frame, text='Choice 4: ', fg='black', font=("ariel", 20, "bold"))
        self.radio_label_4.grid(row=3, column=0)
        self.radio_choice_4 = customtkinter.CTkRadioButton(master=self.radiobutton_frame, variable=self.radio_var, value = quiz_page_content[8], text = quiz_page_content[8])
        self.radio_choice_4.grid(row=3, column=1, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="ew")

        # create entry frame first
        self.answer_frame = customtkinter.CTkFrame(self.window)
        self.answer_frame.grid_columnconfigure(1, weight=1)
        self.entry_answer_label = tk.Label(self.answer_frame, text='Please enter you answer: ', fg='black',
                                           font=("ariel", 20, "bold"))
        self.entry_answer_label.grid(row=0, column=0)
        self.entry_answer = customtkinter.CTkTextbox(self.answer_frame, height=100)
        self.entry_answer.grid(row=0, column=1, columnspan=2, padx=(20, 20), pady=(40, 40), sticky="we")

        # self.answer_label = tk.Label(self.radiobutton_frame, text='Answer: ', fg='black', font=("ariel", 20, "bold"))
        # self.answer_label.grid(row = 4, column=0)
        # self.answer = customtkinter.CTkTextbox(self.radiobutton_frame, height=100)
        # self.answer.grid(row=4, column=1, columnspan=2, padx=(20, 20), pady=(40, 40), sticky="we")

        #create the add new page button
        self.bottom_frame = customtkinter.CTkFrame(self.window)
        self.next_question_button = customtkinter.CTkButton(self.bottom_frame, text='Next Question', command = lambda : self.verify_asnwer("Next", selected_quiz_content , quiz_page_content))
        if self.quiz_index == self.quiz_len-1:
            self.next_question_button = customtkinter.CTkButton(self.bottom_frame, text='Finish Attempt', command = lambda : self.verify_asnwer("Finish", selected_quiz_content, quiz_page_content))
        self.next_question_button.grid(row=0, column=0, padx=(1000, 100), pady=20, sticky = 'e')
        # self.finish_quiz_button = customtkinter.CTkButton(self.bottom_frame, text='Finish', command = lambda : self.quiz_to_menu("Submit"))
        # self.finish_quiz_button.grid(row=0, column=1, padx=20, pady=20, sticky = 'e')

        if self.quiz_type == "Multiple Choice":
            self.radiobutton_frame.grid(row=3, column=0, columnspan=2, padx=(20, 20), pady=(20, 0), sticky="nsew")
            self.bottom_frame.grid(row=4, column=1, padx=(20, 20), pady=(20, 0), sticky="nsew")
        elif self.quiz_type == "Short Answer":
            self.answer_frame.grid(row=3, column=0, columnspan=2, padx=(20, 20), pady=(20, 0), sticky="nsew")
            self.bottom_frame.grid(row=4, column=1, padx=(20, 20), pady=(20, 0), sticky="nsew")

        self.question_textbox.configure(state = "disabled")
        self.window.mainloop()


    def verify_asnwer(self, type, selected_quiz_content, quiz_page_content):
        if self.quiz_type == "Multiple Choice":
            selected_value = self.radio_var.get()
            # Specify the file name and path
            file_name = "quizscore.txt"
            file_path = "C:/Users/ASUS/Documents/"  # Replace with the desired path

            try:
                with open(file_path + file_name, "r+") as file:
                    # Read the content from the file
                    quiz_score = int(file.read())

                    if selected_value == quiz_page_content[9]:
                        new_quiz_score = quiz_score + 1

                        # Write the new page number back to the file
                        file.seek(0)
                        file.write(str(new_quiz_score))
                        file.truncate()

                        if type == "Next":
                            tk.messagebox.showinfo('Message', "Correct Answer ! \n"
                                                              f"Your current score is {new_quiz_score}/{self.quiz_len}")

                            self.quiz_to_new_page(selected_quiz_content)
                        elif type == "Finish":
                            tk.messagebox.showinfo('Message', "Correct Answer ! \n"
                                                              f"Your final score is {new_quiz_score}/{self.quiz_len}")

                            self.window.destroy()
                            Learner_Landing_Page(self.slp, self.username, self.ins)

                    if selected_value != quiz_page_content[9]:
                        new_quiz_score = quiz_score

                        # Write the new page number back to the file
                        file.seek(0)
                        file.write(str(new_quiz_score))
                        file.truncate()

                        if type == "Next":
                            tk.messagebox.showinfo('Message', "Incorrect Answer ! \n"
                                                              f"Your current score is {new_quiz_score}/{self.quiz_len} \n"
                                                                     f"The correct answer is {quiz_page_content[9]}")

                            self.quiz_to_new_page(selected_quiz_content)
                        elif type == "Finish":
                            tk.messagebox.showinfo('Message', "Incorrect Answer ! \n"
                                                              f"Your final score is {new_quiz_score}/{self.quiz_len} \n"
                                                                    f"The correct answer is {quiz_page_content[9]}")
                            self.window.destroy()
                            Learner_Landing_Page(self.slp, self.username, self.ins)
            except FileNotFoundError:
                # Handle the case where the file doesn't exist
                pass
            except Exception as e:
                # Handle any other exceptions that may occur
                print(f"An error occurred: {e}")

        elif self.quiz_type == "Short Answer":
            selected_value = self.entry_answer.get("1.0", "end-1c")
            # Specify the file name and path
            file_name = "quizscore.txt"
            file_path = "C:/Users/ASUS/Documents/"  # Replace with the desired path

            try:
                with open(file_path + file_name, "r+") as file:
                    # Read the content from the file
                    quiz_score = int(file.read())

                    if selected_value == quiz_page_content[4]:
                        new_quiz_score = quiz_score + 1

                        # Write the new page number back to the file
                        file.seek(0)
                        file.write(str(new_quiz_score))
                        file.truncate()

                        if type == "Next":
                            tk.messagebox.showinfo('Message', "Correct Answer ! \n"
                                                              f"Your current score is {new_quiz_score}/{self.quiz_len}")


                            self.quiz_to_new_page(selected_quiz_content)
                        elif type == "Finish":
                            tk.messagebox.showinfo('Message', "Correct Answer ! \n"
                                                              f"Your final score is {new_quiz_score}/{self.quiz_len}")

                            self.window.destroy()
                            Learner_Landing_Page(self.slp, self.username, self.ins)

                    if selected_value != quiz_page_content[4]:
                        new_quiz_score = quiz_score

                        # Write the new page number back to the file
                        file.seek(0)
                        file.write(str(new_quiz_score))
                        file.truncate()

                        if type == "Next":
                            tk.messagebox.showinfo('Message', "Incorrect Answer ! \n"
                                                              f"Your current score is {new_quiz_score}/{self.quiz_len} \n"
                                                                f"The correct answer is {quiz_page_content[4]}")


                            self.quiz_to_new_page(selected_quiz_content)
                        elif type == "Finish":
                            tk.messagebox.showinfo('Message', "Incorrect Answer ! \n"
                                                              f"Your final score is {new_quiz_score}/{self.quiz_len} \n"
                                                                f"The correct answer is {quiz_page_content[4]}")

                            self.window.destroy()
                            Learner_Landing_Page(self.slp, self.username, self.ins)


            except FileNotFoundError:
                # Handle the case where the file doesn't exist
                pass
            except Exception as e:
                # Handle any other exceptions that may occur
                print(f"An error occurred: {e}")

    def quiz_to_new_page(self, selected_quiz_content):

        # Specify the file name and path
        file_name = "quizpage.txt"
        file_path = "C:/Users/ASUS/Documents/"  # Replace with the desired path

        try:
            with open(file_path + file_name, "r+") as file:
                # Read the content from the file
                page_num = int(file.read())
                print("quiz len = ", self.quiz_len)
                print(" page_num = ", page_num)
                if page_num < self.quiz_len - 1:
                    new_page_num = page_num + 1
                    self.window.destroy()

                    # Write the new page number back to the file
                    file.seek(0)
                    file.write(str(new_page_num))
                    file.truncate()

                    new_test_content = Test_Content(self.slp, self.username, self.ins, new_page_num, self.quiz_len, selected_quiz_content)
                    new_test_content

        except FileNotFoundError:
            # Handle the case where the file doesn't exist
            pass
        except Exception as e:
            # Handle any other exceptions that may occur
            print(f"An error occurred: {e}")

    def quiz_to_menu(self, type):
        from main import Instructor_Landing_Page
        self.capture_input(user_input=self.user_input_choice.get(), course_info=self.course_info, type=type)
        self.window.destroy()
        print(self.username)
        Instructor_Landing_Page(self.slp, self.username, self.ins)