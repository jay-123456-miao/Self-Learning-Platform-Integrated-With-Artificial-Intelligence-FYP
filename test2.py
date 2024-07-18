from tkinter import Label, messagebox, Toplevel
from Database import *
import customtkinter
import tkinter.messagebox as messagebox
from learner_menu import *
import cv2
import numpy as np
import os
from matplotlib import pyplot as plt
import time
import mediapipe as mp
from sklearn.model_selection import train_test_split
from keras.utils import to_categorical

from keras.models import Sequential
from keras.layers import LSTM, Dense
from keras.callbacks import TensorBoard
from sklearn.metrics import multilabel_confusion_matrix, accuracy_score

import tkinter as tk
import time





def run_quiz_content_window(slp, username, ins, quiz_index, quiz_len, quiz_pages_content):
    global status
    global countdown_label
    global radio_choice_1
    global radio_choice_2
    global radio_choice_3
    global radio_choice_4
    global entry_answer
    global next_question_button


    window = customtkinter.CTk()

    slp1 = slp
    username1 = username
    ins1 = ins
    quiz_index1 = quiz_index
    quiz_len1 = quiz_len
    selected_quiz_content1 = quiz_pages_content
    print("Length of the list: ", len(selected_quiz_content1))
    print(selected_quiz_content1)
    print("quiz index = ", quiz_index)
    quiz_page_content1 = selected_quiz_content1[quiz_index]
    quiz_type1 = quiz_page_content1[1]

    # Get the screen width and height
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    print(screen_width)
    print(screen_height)
    # Calculate the center position of the screen
    center_x = screen_width // 2
    center_y = screen_height // 2
    # Set the window size and position
    window.geometry(
        f"{screen_width}x{screen_height - 75}+{center_x - screen_width // 2}+{center_y - screen_height // 2}")
    window.title("Test Page")
    window.columnconfigure(1, weight = 1)
    title_label = tk.Label(window, bg = 'green',  text = 'Test Page', fg = 'white', font = ("ariel", 20, "bold"))
    title_label.grid(row = 0, column = 0, columnspan = 2 , sticky = 'we')
    countdown_label = tk.Label(window, font=("Helvetica", 48))
    countdown_label.grid(row =  1, column= 0)
    question_label = tk.Label(window, fg='black', font=("ariel", 20, "bold"))
    question_label.grid(row=2, column=0, sticky='we')
    question_textbox = customtkinter.CTkTextbox(window ,height= 100)
    question_textbox.grid(row=3, column=0, columnspan = 2, padx=(20, 20), pady=(40, 40), sticky="we")
    question_textbox.insert(tk.END, quiz_page_content1[3])

    #Creating the radio button frames first
    radiobutton_frame = customtkinter.CTkFrame(window)
    radiobutton_frame.grid_columnconfigure(1, weight=1)
    radio_var = tk.StringVar(value = quiz_page_content1[5])
    print(quiz_page_content1[5])
    radio_label_1 = tk.Label(radiobutton_frame, text='Choice 1: ', fg='black', font=("ariel", 20, "bold"))
    radio_label_1.grid(row=0, column=0)


    radio_choice_1 = customtkinter.CTkRadioButton(master=radiobutton_frame, variable=radio_var, value = quiz_page_content1[5], text = quiz_page_content1[5])
    radio_choice_1.grid(row=0, column=1, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="ew")
    radio_label_2 = tk.Label(radiobutton_frame, text='Choice 2: ', fg='black', font=("ariel", 20, "bold"))
    radio_label_2.grid(row=1, column=0)
    radio_choice_2 = customtkinter.CTkRadioButton(master=radiobutton_frame, variable=radio_var, value = quiz_page_content1[6], text = quiz_page_content1[6])
    radio_choice_2.grid(row=1, column=1, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="ew")
    radio_label_3 = tk.Label(radiobutton_frame, text='Choice 3: ', fg='black', font=("ariel", 20, "bold"))
    radio_label_3.grid(row=2, column=0)
    radio_choice_3 = customtkinter.CTkRadioButton(master=radiobutton_frame, variable=radio_var, value = quiz_page_content1[7], text = quiz_page_content1[7])
    radio_choice_3.grid(row=2, column=1, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="ew")
    radio_label_4 = tk.Label(radiobutton_frame, text='Choice 4: ', fg='black', font=("ariel", 20, "bold"))
    radio_label_4.grid(row=3, column=0)
    radio_choice_4 = customtkinter.CTkRadioButton(master=radiobutton_frame, variable=radio_var, value = quiz_page_content1[8], text = quiz_page_content1[8])
    radio_choice_4.grid(row=3, column=1, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="ew")

    radio_choice_1.configure(state = "disabled")
    radio_choice_2.configure(state= "disabled")
    radio_choice_3.configure(state= "disabled")
    radio_choice_4.configure(state= "disabled")
    # create entry frame first
    answer_frame = customtkinter.CTkFrame(window)
    answer_frame.grid_columnconfigure(1, weight=1)
    entry_answer_label = tk.Label(answer_frame, text='Please enter you answer: ', fg='black',
                                       font=("ariel", 20, "bold"))
    entry_answer_label.grid(row=0, column=0)


    entry_answer = customtkinter.CTkTextbox(answer_frame, height=100)

    entry_answer.configure(state = "disabled")
    entry_answer.grid(row=0, column=1, columnspan=2, padx=(20, 20), pady=(40, 40), sticky="we")

    #create the add new page button
    bottom_frame = customtkinter.CTkFrame(window)

    next_question_button = customtkinter.CTkButton(bottom_frame, text='Next Question', command = lambda : verify_asnwer("Next", selected_quiz_content1 , quiz_page_content1, quiz_type1, radio_var, quiz_len1, window, slp1, username1, ins1, entry_answer))
    if quiz_index == quiz_len-1:
        next_question_button = customtkinter.CTkButton(bottom_frame, text='Finish Attempt', command = lambda : verify_asnwer("Finish", selected_quiz_content1, quiz_page_content1, quiz_type1, radio_var, quiz_len1, window, slp1, username1, ins1, entry_answer))

    next_question_button.grid(row=0, column=0, padx=(1000, 100), pady=20, sticky = 'e')
    next_question_button.configure(state='disabled')

    if quiz_type1 == "Multiple Choice":
        radiobutton_frame.grid(row=4, column=0, columnspan=2, padx=(20, 20), pady=(20, 0), sticky="nsew")
        bottom_frame.grid(row=5, column=1, padx=(20, 20), pady=(20, 0), sticky="nsew")
    elif quiz_type1 == "Short Answer":
        answer_frame.grid(row=4, column=0, columnspan=2, padx=(20, 20), pady=(20, 0), sticky="nsew")
        bottom_frame.grid(row=5, column=1, padx=(20, 20), pady=(20, 0), sticky="nsew")

    question_textbox.configure(state = "disabled")

    def toplevel():
        global model_countdown_label
        top = Toplevel()
        top.title('Cheating Detection Model')
        top.wm_geometry("794x700")
        optimized_canvas = tk.Canvas(top)
        optimized_canvas.pack(fill=tk.BOTH, expand=1)
        instructions_label = tk.Label(top, font=("Helvetica", 20), text="Please click start model button within 5 seconds\n"
                                                                        "System will terminate session after 5s!")
        instructions_label.pack(pady= (0, 20))
        model_countdown_label = tk.Label(top, font=("Helvetica", 20))
        model_countdown_label.pack(pady = 20)
        countdown(10, "start", slp1, username1, ins1, window)
        login_btn = customtkinter.CTkButton(master=top, text='Start Model',
                                            command=lambda: run_cheating_detection_model(slp1, username1, ins1, window))
        login_btn.pack(pady = 20)
    toplevel()
    window.mainloop()


def verify_asnwer( type, selected_quiz_content, quiz_page_content, quiz_type1, radio_var, quiz_len1, window, slp1, username1, ins1, entry_answer):
    if quiz_type1 == "Multiple Choice":
        selected_value = radio_var.get()
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
                                                          f"Your current score is {new_quiz_score}/{quiz_len1}")

                        quiz_to_new_page(selected_quiz_content, quiz_len1, window, slp1, username1, ins1)
                    elif type == "Finish":
                        tk.messagebox.showinfo('Message', "Correct Answer ! \n"
                                                          f"Your final score is {new_quiz_score}/{quiz_len1}")

                        window.destroy()
                        Learner_Landing_Page(slp1, username1, ins1)

                if selected_value != quiz_page_content[9]:
                    new_quiz_score = quiz_score

                    # Write the new page number back to the file
                    file.seek(0)
                    file.write(str(new_quiz_score))
                    file.truncate()

                    if type == "Next":
                        tk.messagebox.showinfo('Message', "Incorrect Answer ! \n"
                                                          f"Your current score is {new_quiz_score}/{quiz_len1} \n"
                                                                 f"The correct answer is {quiz_page_content[9]}")

                        quiz_to_new_page(selected_quiz_content, quiz_len1, window, slp1, username1, ins1)
                    elif type == "Finish":
                        tk.messagebox.showinfo('Message', "Incorrect Answer ! \n"
                                                          f"Your final score is {new_quiz_score}/{quiz_len1} \n"
                                                                f"The correct answer is {quiz_page_content[9]}")
                        window.destroy()
                        Learner_Landing_Page(slp1, username1, ins1)
        except FileNotFoundError:
            # Handle the case where the file doesn't exist
            pass
        except Exception as e:
            # Handle any other exceptions that may occur
            print(f"An error occurred: {e}")

    elif quiz_type1 == "Short Answer":
        selected_value = entry_answer.get("1.0", "end-1c")
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
                                                          f"Your current score is {new_quiz_score}/{quiz_len1}")


                        quiz_to_new_page(selected_quiz_content, quiz_len1, window, slp1, username1, ins1)
                    elif type == "Finish":
                        tk.messagebox.showinfo('Message', "Correct Answer ! \n"
                                                          f"Your final score is {new_quiz_score}/{quiz_len1}")

                        window.destroy()
                        Learner_Landing_Page(slp1, username1, ins1)

                if selected_value != quiz_page_content[4]:
                    new_quiz_score = quiz_score

                    # Write the new page number back to the file
                    file.seek(0)
                    file.write(str(new_quiz_score))
                    file.truncate()

                    if type == "Next":
                        tk.messagebox.showinfo('Message', "Incorrect Answer ! \n"
                                                          f"Your current score is {new_quiz_score}/{quiz_len1} \n"
                                                            f"The correct answer is {quiz_page_content[4]}")


                        quiz_to_new_page(selected_quiz_content, quiz_len1, window, slp1, username1, ins1)
                    elif type == "Finish":
                        tk.messagebox.showinfo('Message', "Incorrect Answer ! \n"
                                                          f"Your final score is {new_quiz_score}/{quiz_len1} \n"
                                                            f"The correct answer is {quiz_page_content[4]}")

                        window.destroy()
                        Learner_Landing_Page(slp1, username1, ins1)


        except FileNotFoundError:
            # Handle the case where the file doesn't exist
            pass
        except Exception as e:
            # Handle any other exceptions that may occur
            print(f"An error occurred: {e}")

def quiz_to_new_page( selected_quiz_content, quiz_len1, window, slp1, username1, ins1):

    # Specify the file name and path
    file_name = "quizpage.txt"
    file_path = "C:/Users/ASUS/Documents/"  # Replace with the desired path

    try:
        with open(file_path + file_name, "r+") as file:
            # Read the content from the file
            page_num = int(file.read())
            print("quiz len = ", quiz_len1)
            print(" page_num = ", page_num)
            if page_num < quiz_len1 - 1:
                new_page_num = page_num + 1
                window.destroy()

                # Write the new page number back to the file
                file.seek(0)
                file.write(str(new_page_num))
                file.truncate()

                new_test_content = run_quiz_content_window(slp1, username1, ins1, new_page_num, quiz_len1, selected_quiz_content)
                new_test_content

    except FileNotFoundError:
        # Handle the case where the file doesn't exist
        pass
    except Exception as e:
        # Handle any other exceptions that may occur
        print(f"An error occurred: {e}")

def quiz_to_menu(slp1, username1, ins1, window):
    from learner_menu import Learner_Landing_Page
    window.destroy()
    Learner_Landing_Page(slp1, username1, ins1)



def countdown(duration, type, slp1, username1, ins1, window):
    mins, secs = divmod(duration, 60)
    timer = '{:02d}:{:02d}'.format(mins, secs)
    if type == "end":
        countdown_label.config(text=timer)
        if duration > 0:
            countdown_label.after(1000, lambda: countdown(duration - 1, type, slp1, username1, ins1, window))
        else:

                radio_choice_1.configure(state = 'disabled')
                radio_choice_2.configure(state='disabled')
                radio_choice_3.configure(state='disabled')
                radio_choice_4.configure(state='disabled')
                entry_answer.configure(state='disabled')
                countdown_label.config(text="Time is up!")
    else:
        model_countdown_label.config(text = timer)
        if duration > 0:
            countdown_label.after(1000, lambda: countdown(duration - 1, type, slp1, username1, ins1, window))
        else:
            model_countdown_label.config(text = "Time is up")
            quiz_to_menu(slp1, username1, ins1, window)


def mediapipe_detection(image, model):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) # COLOR CONVERSION BGR 2 RGB
    image.flags.writeable = False                  # Image is no longer writeable
    results = model.process(image)                 # Make prediction
    image.flags.writeable = True                   # Image is now writeable
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR) # COLOR COVERSION RGB 2 BGR
    return image, results

def draw_landmarks(image, results, mp_pose):
    mp_drawing = mp.solutions.drawing_utils  # Drawing utilities
    mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                              mp_drawing.DrawingSpec(color=(80, 22, 10), thickness=2, circle_radius=4),
                              mp_drawing.DrawingSpec(color=(80, 44, 121), thickness=2, circle_radius=2)
                              )
def extract_keypoints(results):
    pose = np.array([[res.x, res.y, res.z, res.visibility] for res in results.pose_landmarks.landmark]).flatten() if results.pose_landmarks else np.zeros(33*4)
    return pose


def run_cheating_detection_model(slp1, username1, ins1, window):
    mp_pose = mp.solutions.pose  # Holistic model
    actions = np.array(['normal', 'head_facing_left', 'head_facing_right', 'head_facing_down', 'on_phone'])
    model = Sequential()
    model.add(LSTM(64, return_sequences=True, activation='relu', input_shape=(30, 132)))
    model.add(LSTM(128, return_sequences=True, activation='relu'))
    model.add(LSTM(64, return_sequences=False, activation='relu'))
    model.add(Dense(64, activation='relu'))
    model.add(Dense(32, activation='relu'))
    model.add(Dense(actions.shape[0], activation='softmax'))
    #
    model.compile(optimizer='Adam', loss='categorical_crossentropy', metrics=['categorical_accuracy'])
    model.load_weights(r'C:\Users\ASUS\PycharmProjects\Final_Year_Project\cheating_weights\action2.h5')
    sequence = []
    sentence = []
    threshold = 0.8

    # Counter to track consecutive "normal" frames
    consecutive_cheating_frames = 0

    cap = cv2.VideoCapture(0)
    # Set mediapipe model
    with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:
        while cap.isOpened():
            # Read feed
            ret, frame = cap.read()

            # Make detections
            image, results = mediapipe_detection(frame, holistic)
            print(results)

            # Draw landmarks
            draw_landmarks(image, results, mp_pose)

            # Prediction logic
            keypoints = extract_keypoints(results)
            sequence.append(keypoints)
            sequence = sequence[-30:]

            if len(sequence) == 30:
                res = model.predict(np.expand_dims(sequence, axis=0))[0]
                print(actions[np.argmax(res)])

                # Detect if the result class is "cheating class"
                if actions[np.argmax(res)] == 'on_phone' or 'head_facing_left' or 'head_facing_right' or 'head_facing_down':
                    consecutive_cheating_frames += 1
                    # Execute certain functions if "normal" is detected for 60 consecutive frames
                    if consecutive_cheating_frames >= 200:
                        cap.release()
                        cv2.destroyAllWindows()
                        quiz_to_menu(slp1, username1, ins1, window)

                else:
                    consecutive_cheating_frames = 0

                # Viz logic
                if res[np.argmax(res)] > threshold:
                    if len(sentence) > 0:
                        if actions[np.argmax(res)] != sentence[-1]:
                            sentence.append(actions[np.argmax(res)])
                    else:
                        sentence.append(actions[np.argmax(res)])

                if len(sentence) > 5:
                    sentence = sentence[-5:]

                cv2.rectangle(image, (0, 0), (640, 40), (245, 117, 16), -1)
                cv2.putText(image, ' '.join(sentence), (3, 30),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)

            # Show to screen
            cv2.imshow('OpenCV Feed', image)

            # Break gracefully
            if cv2.waitKey(10) & 0xFF == ord('q'):
                entry_answer.configure(state = "normal")
                radio_choice_1.configure(state='normal')
                radio_choice_2.configure(state='normal')
                radio_choice_3.configure(state='normal')
                radio_choice_4.configure(state='normal')
                next_question_button.configure(state='normal')
                countdown(20, "end", slp1, username1, ins1, window)
                break

    cap.release()
    cv2.destroyAllWindows()


