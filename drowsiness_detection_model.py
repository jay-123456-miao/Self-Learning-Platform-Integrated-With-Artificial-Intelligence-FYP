import torch
from matplotlib import pyplot as plt
import numpy as np
import cv2
import time
import pygame


class drowsiness_detection_model:
    def __init__(self, slp, username, ins):
        pygame.mixer.init()
        self.model = torch.hub.load('ultralytics/yolov5', 'custom',
                                   path=r'C:\Users\ASUS\PycharmProjects\Final_Year_Project\best.pt',
                                   force_reload=True)
        self.audio_path = r"C:\Users\USER\PycharmProjects\pythonProject2\warning.mp3"
        self.cap = cv2.VideoCapture(0)
        self.drowsy_count = 0
        self.start_time = None
        self.warning_count = 0
        self.status = "run"
        self.window = None
        self.slp = slp
        self.username = username
        self.ins = ins
    def set_status(self, status):
        self.status = status

    def set_learner_obj(self, learner_obj):
        self.learner_obj = learner_obj

    def set_window(self, window):
        self.window = window

    def play_audio(self):
        try:
            self.warning_count = self.warning_count+1
            pygame.mixer.music.load(r"C:\Users\ASUS\PycharmProjects\Final_Year_Project\warning.mp3")
            pygame.mixer.music.play()
        except Exception as e:
            print(f"Failed to play audio: {e}")

    def run(self):
        from learner_content import Learner_course_content
        while self.cap.isOpened():
            if self.status == "end":
                self.cap.release()
                cv2.destroyAllWindows()

            if self.warning_count == 3:
                self.cap.release()
                cv2.destroyAllWindows()
                self.content_to_menu()


            ret, frame = self.cap.read()

            # Convert the image to RGB format
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Make detections
            results = self.model(frame_rgb)

            # Access the class labels
            class_labels = results.xyxy[0].t()[5].tolist()

            # if self.warning_count == 3:
            #     print("Your session has been terminated after three warnings")


            # Check if the 'drowsy' class (15.0) is detected
            if 16.0 in class_labels:
                self.drowsy_count += 1
                if self.start_time is None:
                    self.start_time = time.time()
            else:
                self.drowsy_count = 0
                self.start_time = None

            # If the 'drowsy' class is detected for at least 5 seconds, play an audio output
            if self.drowsy_count >= 5 * 5 and (time.time() - self.start_time) >= 5:
                self.play_audio()
                self.drowsy_count = 0
                self.start_time = None
            cv2.imshow('YOLO', np.squeeze(results.render()))

            if cv2.waitKey(10)& 0xFF == ord('/'):
                break


        self.cap.release()
        cv2.destroyAllWindows()

    def content_to_menu(self):
        from learner_menu import Learner_Landing_Page
        self.window.destroy()
        print(self.username)
        Learner_Landing_Page(self.slp, self.username, self.ins)


import threading
from playsound import playsound

# class PlayVideo:
#     def __init__(self):
#         self.audio_path = r"C:\Users\USER\PycharmProjects\pythonProject2\warning.mp3"
#
#     def play_audio(self):
#         try:
#             playsound(self.audio_path)
#         except Exception as e:
#             print(f"Failed to play audio: {e}")
#
#     def PlayVideo(self):
#         print("Hello")
#         audio_thread = threading.Thread(target=self.play_audio)
#         audio_thread.start()
#
# drow = drowsiness_detection_model()
# drow.run()

