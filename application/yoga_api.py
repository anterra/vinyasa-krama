import pickle
import numpy as np
import pandas as pd
import keras
import tensorflow as tf
from keras import Model
from tensorflow.keras.models import load_model


f = open("../word_embeddings.pkl", "rb")
embeddings = pickle.load(f)
f.close()

f = open("../tokenizer.pkl", "rb")
tokenizer = pickle.load(f)
f.close()

f = open("../tokenizer2.pkl", "rb")
tokenizer2 = pickle.load(f)
f.close()

f = open("../peak_poses.pkl", "rb")
peak_poses = pickle.load(f)
f.close()

f = open("../peak_pose_dict.pkl", "rb")
peak_pose_dict = pickle.load(f)
f.close()

lstm_model = load_model("../lstm_model.h5")
model = load_model("../model.h5")


def get_peak_pose(user_selection):
    fields = list(user_selection.values())
    peak_pose = [i for i in fields if i != '']
    return peak_pose[0]


# check that code runs properly from terminal
if __name__ == "__main__":
    from pprint import pprint
