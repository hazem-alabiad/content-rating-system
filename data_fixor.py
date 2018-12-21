import pandas  as pd
import matplotlib.pyplot as plt
import numpy as np
from helper_functions import open_pickle

from imblearn.over_sampling import ADASYN   

from imblearn.under_sampling import TomekLinks

from imblearn.combine import SMOTETomek

data = open_pickle("./pandas_data_frame.pkl")
data_frame = pd.DataFrame(data=data)

x = data_frame["movie_words"].tolist()

y = data_frame["rating"].tolist()


#make all the movies with same length of words, im not sure if the problem is from it or not

max_words = 0

for words in x: 
    if len(words) > max_words: 
        max_words = len(words)

all_words_list = []

for words in x:
    while len(words) < max_words:
        words.append(" ")

    all_words_list.append(words)

data["movie_words"] = all_words_list.copy()

#Make a matrix with ( number_of_movies * max_words ) size

x = data_frame["movie_words"].tolist()

all_words = []

for words in x:
    all_words.extend(words)


all_words = np.array(all_words)
all_words = all_words.reshape((len(x), max_words))

x_resample, y_resample = ada.fit_resample(all_words, y.ravel())


