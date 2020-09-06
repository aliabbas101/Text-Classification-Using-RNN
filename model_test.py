import tensorflow as tf
from tensorflow import keras

import numpy as np
import pandas as pd
import os
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import pickle



def predict(text):
    new_model = keras.models.load_model('model1.h5')

    # Check its architecture
    classes=['Sarcastic', 'No Sarcasm']

    max_length= 100
    trunc_type='post'
    padding_type = 'post'

    with open('tokenizer.pickle', 'rb') as handle:
        tokenizer = pickle.load(handle)



    sentence= [text]
    sequences= tokenizer.texts_to_sequences(sentence)
    padded= pad_sequences(sequences, maxlen=max_length, padding=padding_type, truncating= trunc_type)
    prediction=new_model.predict(padded)

    return prediction[0] > 0.4

    

