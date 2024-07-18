import tensorflow as tf
import os
import pandas as pd
import numpy as np
from collections import Counter
import pickle
from keras.layers import TextVectorization
from Database import *
import tkinter.messagebox as messagebox


class Harmful_Content_Model:
    def __init__(self, List):
        self.list = List

    def execute_model(self):
        content_predictions = []
        # Load the saved config and weights
        from_disk = pickle.load(open(
            "C:\\Users\\ASUS\\PycharmProjects\\Final_Year_Project\\Harmful_Content_Detection_Dataset\\vectorizer\\tv_layer.pkl",
            "rb"))

        # Create a new TextVectorization layer using the loaded config
        vectorizer = TextVectorization.from_config(from_disk['config'])

        # Call `adapt` with some dummy data (this is a bug in Keras)
        vectorizer.adapt(tf.data.Dataset.from_tensor_slices(["xyz"]))

        # Set the weights from the loaded weights
        vectorizer.set_weights(from_disk['weights'])

        reconstructed_model = tf.keras.models.load_model(
            'C:\\Users\\ASUS\\PycharmProjects\\Final_Year_Project\\Harmful_Content_Detection_Dataset\\model\\my_model5.h5',
            compile=False)
        print(reconstructed_model.summary())
        for content in self.list:
            input_str = vectorizer(f'{content}')
            res = (reconstructed_model.predict(np.expand_dims(input_str,0))>0.5).astype(int)
            content_predictions.append(res[0])

        content_indexes_with_ones = []
        ones_indexes_per_content = []

        for i, array in enumerate(content_predictions):
            if 1 in array:
                content_indexes_with_ones.append(i)
                ones_indexes = [idx for idx, val in enumerate(array) if val == 1]
                ones_indexes_per_content.append(ones_indexes)

        return content_indexes_with_ones, ones_indexes_per_content















# list = ['Fuck you lah whore', 'Liaw Yu Jay', 'I think you should go ahead and kill yourself', 'Subtopic 1: The secret to life', 'Image 1', 'Image 2', 'Image 3', '- In this world full of lies and sadness, we must learn to protect ourselves and do what we can do love ourselves.\n- Alwys know your worth and do not give in to failure.\n- Work hard towards you goal everyday.', 'Subtopic 2: Things to do', 'Image 1', 'Image 2', 'Image 3', '- Learn to code for four hourse everyday\n- Learn to make you make your bed everyday\n- Sleep for 8 hours everyda', 'Subtopic 3: Know yourself', 'Image 1', 'You stupid pig you deserve to die', 'Image 3', '- Discover yourself\n- Attend courses that will enrich yourself\n- Love Your Family']
# harm = Harm_Content_Model(list)
#
# list1, list2  = harm.execute_model()
# print(list1)
# print(list2)
#
# root = tk.Tk()
#
# def show_content_and_indexes():
#     message = ""
#     for i, content_index in enumerate(list1):
#         content = list[content_index]
#         ones_indexes = list2[i]
#         harmful_list = []
#         for harmful_type in ones_indexes:
#             if harmful_type == 0:
#                 harmful_list.append("toxic")
#             if harmful_type == 1:
#                 harmful_list.append("severe_toxic")
#             if harmful_type == 2:
#                 harmful_list.append("obscene")
#             if harmful_type == 3:
#                 harmful_list.append("threat")
#             if harmful_type == 4:
#                 harmful_list.append("insult")
#             if harmful_type == 5:
#                 harmful_list.append("identity_hate")
#         message += f"Content at index {content_index}: {content}\n"
#         message += f"The above sentence contais: {harmful_list}\n\n"
#     messagebox.showinfo("Content and Indexes", message)
#
# button = tk.Button(root, text="Show Content and Indexes", command=show_content_and_indexes)
# button.pack()
#
# root.mainloop()