import tkinter as tk
import tkinter.messagebox
from tkinter import Label
from tkinter import filedialog
from PIL import Image, ImageTk
import customtkinter

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        img = Image.open('bg.jpg')

        img_1 = img.resize((400, 150))

        self.pic1 = ImageTk.PhotoImage(img_1)
        self.pic2 = ImageTk.PhotoImage(img_1)
        self.pic3 = ImageTk.PhotoImage(img_1)

        # Get the screen width and height
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # Calculate the center position of the screen
        center_x = screen_width // 2
        center_y = screen_height // 2

        # Set the window size and position
        self.geometry(f"{screen_width}x{screen_height - 75}+{center_x - screen_width // 2}+{center_y - screen_height // 2}")

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        # self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0,1), weight = 0 )
        self.grid_rowconfigure((2,3), weight=1)

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=5, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="CustomTkinter", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"],                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))

        # create title, Author, Date:
        self.title_frame = customtkinter.CTkFrame(self, corner_radius= 0 )
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
        self.date_label = customtkinter.CTkLabel(self.title_frame, text="Date:")
        self.date_label.grid(row = 2, column = 0, padx=20, pady=(10, 0), sticky="w")
        self.date_entry = customtkinter.CTkEntry(self.title_frame, placeholder_text="CTkEntry")
        self.date_entry.grid(row = 2, column = 1, padx=20, pady=(10, 10), sticky="we")

        # create an abstract frame
        self.abtract_frame = customtkinter.CTkFrame(self, corner_radius= 0)
        self.abtract_frame.grid(row=1, column=1, padx=(20, 20), pady=(20, 0), sticky="nsew")
        self.abtract_frame.grid_columnconfigure(0, weight = 1)
        self.abtract_label = customtkinter.CTkLabel(self.abtract_frame, text="Abtract:")
        self.abtract_label.grid(row=0, column=0, padx=20, pady=(10, 0), sticky="w")
        self.textbox = customtkinter.CTkTextbox(self.abtract_frame ,height= 100)
        self.textbox.grid(row=1, column=0, padx=(20, 20), pady=(20, 20), sticky="nsew")

        # create tabview
        self.tabview = customtkinter.CTkTabview(self)
        self.tabview.grid(row=2, column=1, padx=(20, 20), pady=(0, 0), sticky="nsew")
        self.tabview.add("Subtopic 1")
        self.tabview.add("Subtopic 2")
        self.tabview.add("Subtopic 3")

        # Usage example
        self.setup_tab_design(self.tabview.tab("Subtopic 1"), "Subtopic 1", self.pic1)
        self.setup_tab_design(self.tabview.tab("Subtopic 2"), "Subtopic 2", self.pic2)
        self.setup_tab_design(self.tabview.tab("Subtopic 3"), "Subtopic 3", self.pic3)

        # submit button, add button , create quiz
        self.submit_frame = customtkinter.CTkFrame(self, corner_radius= 0)
        self.submit_frame.grid(row= 3, column = 1, padx=(20, 20), pady=(20, 0), sticky="nsew")
        self.submit_frame.grid_columnconfigure((0,1,2), weight=1)
        self.submit_button = customtkinter.CTkButton(self.submit_frame, text='Submit', command = lambda : self.menu_to_none(self))
        self.submit_button.grid(row=0, column=2, padx=20, pady=20)
        self.add_button = customtkinter.CTkButton(self.submit_frame, text='Add', command = lambda :self.clear_content())
        self.add_button.grid(row=0, column=1, padx=20, pady=20)
        self.create_quiz_button = customtkinter.CTkButton(self.submit_frame, text='Create Quiz', command = lambda : self.menu_to_none(self))
        self.create_quiz_button.grid(row=0, column=0, padx=20, pady=20)

        # # set default values
        self.appearance_mode_optionemenu.set("Dark")

        self.mainloop()

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

    def setup_tab_design(self, tab, num, img):
        # self.tabview.tab(num).grid_rowconfigure(3, weight=1)
        self.tabview.tab(num).grid_columnconfigure(( 0, 1, 2, 3), weight=1)  # configure grid of individual tabs
        # adding background image

        self.subtopic_entry = customtkinter.CTkEntry(tab, placeholder_text="CTkEntry")
        self.subtopic_entry.grid(row=0, column=0, columnspan = 3, padx=20, pady=(10, 10), sticky="we")

        self.imgLabel1 = Label(tab, image= img)
        self.imgLabel1.grid(row=1, column=0, sticky="ns")

        self.imgLabel2 = Label(tab, image= img)
        self.imgLabel2.grid(row=1, column=1, sticky="ns")

        self.imgLabel3 = Label(tab, image= img)
        self.imgLabel3.grid(row=1, column=2, sticky="ns")

        self.data_entry1 = customtkinter.CTkEntry(tab, placeholder_text="CTkEntry", )
        self.data_entry1.grid(row=2, column=0, padx=20, pady=(10, 10), sticky="ns")

        self.data_entry2 = customtkinter.CTkEntry(tab, placeholder_text="CTkEntry")
        self.data_entry2.grid(row=2, column=1, padx=20, pady=(10, 10), sticky="ns")

        self. data_entry3 = customtkinter.CTkEntry(tab, placeholder_text="CTkEntry")
        self.data_entry3.grid(row=2, column=2, padx=20, pady=(10, 10), sticky="ns")

        self.upload_button1 = customtkinter.CTkButton(tab,  text='Upload', command=lambda: self.imageUploader(self.imgLabel1))
        self.upload_button1.grid(row=3, column=0, padx=20, pady=10,  sticky="ns")

        self.upload_button2 = customtkinter.CTkButton(tab, text='Upload', command=lambda: self.imageUploader(self.imgLabel2))
        self.upload_button2.grid(row=3, column=1, padx=20, pady=10, sticky="ns")

        self.upload_button3 = customtkinter.CTkButton(tab, text='Upload', command=lambda: self.imageUploader(self.imgLabel3))
        self.upload_button3.grid(row=3, column=2, padx=20, pady=10, sticky="ns")

        self.textbox = customtkinter.CTkTextbox(tab)
        self.textbox.grid(row=4, column=0, columnspan=3, padx=(20, 20), pady=(20, 20), sticky="nsew")

    def captureData(self):
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

        for item in data:
            print(item)

    def clear_content(self):
        # Clear the entry widgets
        self.title_entry.delete(0, 'end')
        self.author_entry.delete(0, 'end')
        self.date_entry.delete(0, 'end')

        # Clear the textbox widget
        self.textbox.delete('1.0', 'end')

        self.clear_tab_contents("Subtopic 1")
        self.clear_tab_contents("Subtopic 2")
        self.clear_tab_contents("Subtopic 3")

    def clear_tab_contents(self, tab_name):
        # Get the current tab
        current_tab = self.tabview.tab(tab_name)

        # Find the widgets in the current tab
        subtopic_entry = current_tab.nametowidget("subtopic_entry")
        data_entry1 = current_tab.nametowidget("data_entry1")
        data_entry2 = current_tab.nametowidget("data_entry2")
        data_entry3 = current_tab.nametowidget("data_entry3")
        textbox = current_tab.nametowidget("textbox")

        # Clear the contents of the widgets
        subtopic_entry.delete(0, tk.END)
        data_entry1.delete(0, tk.END)
        data_entry2.delete(0, tk.END)
        data_entry3.delete(0, tk.END)
        textbox.delete('1.0', tk.END)


    def menu_to_none(self, window):
        window.destroy()

    def add_new_topic(self, window):
        window.destroy()
        App()

if __name__ == "__main__":
    app = App()
