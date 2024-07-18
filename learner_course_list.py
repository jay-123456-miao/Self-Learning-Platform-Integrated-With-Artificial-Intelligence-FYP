import customtkinter
from Database import *

class Learner_course_List_Page(customtkinter.CTk):
    def __init__(self, slp, username, ins):
        self.slp = slp
        self.window = customtkinter.CTk()
        self.db = Database()
        self.ins = ins
        self.username = username
        user_info = self.ins.search_by_username2(self.username)
        user_details = user_info[0]
        user_id = user_details[0]
        print(user_id)
        self.course_list = self.db.retrieve_all_course()
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

        self.window.grid_columnconfigure(0, weight = 1)
        self.window.grid_rowconfigure(0, weight=1)


        # Create listbox that shows all the available course content
        self.course_listbox = tk.Listbox(self.window)
        self.course_listbox.grid(row = 0 , column  = 0, padx = 50, pady = 50, sticky = "nsew")

        for course in self.course_list:
            self.course_listbox.insert(tk.END, course[0])

        # # create a combo box for the users to choose wat mode they want to attempt the course in
        # self.course_mode_combo = customtkinter.CTkComboBox(master=self.window, values=["Normal", "Serious"], width=200,
        #                                        height=30)
        # self.course_mode_combo.grid(row=1, column=0, padx=20, pady=20)
        # Create a button for the users to confirm their choice
        self.confirm_quiz_button = customtkinter.CTkButton(self.window, text='Select Course',
                                                          command=lambda: self.get_listbox_content())
        self.confirm_quiz_button.grid(row=2, column=0, padx=20, pady=20)

        self.window.mainloop()

    def get_listbox_content(self):
        choice  = self.course_listbox.get(tk.ANCHOR)
        # mode = self.course_mode_combo.get()
        for course in self.course_list:
            if course[0] == choice:
                course_id =  course[1]
                print(course_id)
        selected_course_content = self.db.retrieve_course_content_based_on_course_id(course_id)
        # Specify the file name and path
        file_name = "page.txt"
        file_path = "C:/Users/ASUS/Documents/"  # Replace with the desired path

        # Open the file in write mode
        with open(file_path + file_name, "w") as file:
            # Write content to the file
            file.write("0")

        print(f"File '{file_name}' created and written to at '{file_path}'")
        page_num = len(selected_course_content)
        self.slp.course_list_to_learner_content(selected_course_content, page_num, self.slp, 0, self.window, self.ins, self.username, course_id)