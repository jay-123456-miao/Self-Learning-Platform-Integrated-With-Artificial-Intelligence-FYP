import tensorflow as tf
import os
import pandas as pd
import numpy as np
from collections import Counter
import pickle

print(tf.config.list_physical_devices())

print("Num GPUs Available: ", len(tf.config.list_physical_devices('GPU')))
with tf.device('/gpu:0'):
    import keras
    from keras.layers import TextVectorization

    path_ds = 'C:\\Users\\ASUS\\PycharmProjects\\Final_Year_Project\\Harmful_Content_Detection_Dataset\\train\\train.csv'
    df = pd.read_csv(path_ds)
    # The number of words we want in the vocabulary (Tokenization)

    ## splttting the data into X(input) and Y(output)

    X = df['comment_text']
    y = df[df.columns[2:]].values

    # MAX_FEATURES  = 200000
    #
    # vectorizer = TextVectorization(max_tokens = MAX_FEATURES,
    #                                output_sequence_length= 400,
    #                                output_mode='int')
    #
    # vectorizer.adapt(X.values)
    #
    #
    #
    # # Pickle the config and weights
    # pickle.dump({'config': vectorizer.get_config(), 'weights': vectorizer.get_weights()}, open("C:\\Users\\ASUS\\PycharmProjects\\Final_Year_Project\\Harmful_Content_Detection_Dataset\\vectorizer\\tv_layer.pkl", "wb"))

    # Load the saved config and weights
    from_disk = pickle.load(open("C:\\Users\\ASUS\\PycharmProjects\\Final_Year_Project\\Harmful_Content_Detection_Dataset\\vectorizer\\tv_layer.pkl", "rb"))

    # Create a new TextVectorization layer using the loaded config
    vectorizer = TextVectorization.from_config(from_disk['config'])

    # Call `adapt` with some dummy data (this is a bug in Keras)
    vectorizer.adapt(tf.data.Dataset.from_tensor_slices(["xyz"]))

    # Set the weights from the loaded weights
    vectorizer.set_weights(from_disk['weights'])
    vectorized_text = vectorizer(X.values)
    print(vectorized_text.shape)


    # Data pipeline #MCSHBAP - map, chache, shuffle, batch, prefetch from tensor_slices, list_file
    dataset = tf.data.Dataset.from_tensor_slices((vectorized_text, y))
    dataset = dataset.cache()
    dataset = dataset.shuffle(160000)
    dataset = dataset.batch(16)
    dataset = dataset.prefetch(8)

    train = dataset.take(int(len(dataset)*.7))
    val = dataset.skip(int(len(dataset)*.7)).take(int(len(dataset)*.2))
    test = dataset.skip(int(len(dataset)*.9)).take(int(len(dataset)*.1))

    reconstructed_model = tf.keras.models.load_model('C:\\Users\\ASUS\\PycharmProjects\\Final_Year_Project\\Harmful_Content_Detection_Dataset\\model\\my_model5.h5', compile=False)
    input_str = vectorizer('You are a piece of dog shit and fuck you and everyone you know')

    res = (reconstructed_model.predict(np.expand_dims(input_str,0))>0.5).astype(int)
    print(res)
    print(res.shape)
    #Evaluate the model
    from  keras.metrics import Precision, Recall, CategoricalAccuracy

    pre = Precision()
    re = Recall()
    acc = CategoricalAccuracy()



    all_y_true = []
    all_y_pred = []

    for batch in test.as_numpy_iterator():
        # Unpack the batch
        X_true, y_true = batch
        # Make a prediction
        yhat = reconstructed_model.predict(X_true)

        # Flatten the predictions
        y_true = y_true.flatten()
        yhat = yhat.flatten()

        all_y_true.extend(y_true)
        all_y_pred.extend(yhat)

        pre.update_state(y_true, yhat)
        re.update_state(y_true, yhat)
        acc.update_state(y_true, yhat)

    print(f'Precision: {pre.result().numpy()}, Recall:{re.result().numpy()}, Accuracy:{acc.result().numpy()}')