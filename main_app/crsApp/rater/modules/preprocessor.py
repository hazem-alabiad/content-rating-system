import re
import os
from nltk.corpus import stopwords
import pickle
from nltk.corpus import words
from nltk.tokenize import word_tokenize
import pandas as pd
from nltk.corpus import wordnet

def in_pickle(pickle_path, pick_name):
    with open(pickle_path + pick_name + ".pkl", "rb") as pkl:
        return pickle.load(pkl)

def out_pickle(pickle_path, pick_name, variable_name):
    with open(pickle_path + pick_name + ".pkl", "wb") as pkl:
        pickle.dump(variable_name, pkl)


nltk_word_set = set(words.words())
slang_words_set = set(in_pickle(os.getcwd() + "/rater/modules/pickles/", "english_slang_words_set"))
full_word_set = nltk_word_set.union(slang_words_set)

stop_words = set(stopwords.words('english'))

#Cleaning function for the whole text
def clean_text(text):
    """
    Remove "(strings)" or "<string>" or "[string]" or {string}" from text file.
    """
    regex = re.compile('(<.*?>) | (\(.*?\)) | (\[.*?\]) | (\{.*?\})' )
    cleantext = re.sub(regex, '', text)
    return cleantext

# Cleaning function for each token
def clean_tokens(tokens_list):
    cleaned_tokens = []
    for token in tokens_list:
        token = token.lower()
        if token.isalpha():
            if token not in stop_words:
                if len(token) > 1:
                    
                    if (token in full_word_set) or (wordnet.synsets(token) != []):
                        cleaned_tokens.append(token)

    return cleaned_tokens

# Clean the input text file and tokenize it
def preprocess_file(full_file_path):
    input_file = open(full_file_path, "r")

    text = input_file.read()
    cleaned_text = clean_text(text)
    tokens = word_tokenize(cleaned_text)
    cleaned_tokens = clean_tokens(tokens)
    return cleaned_tokens

# returns a dictionary and the total number of non-english words
# key: non-english word
# value: number of occurrences in text
def get_non_english_words(text_words):
    total_number_of_non_english_words = 0
    # key: non_english_word
    # value: number of occurrences
    non_english_words_dict = {}

    for word in text_words:
        if word not in full_word_set:
            if (not wordnet.synsets(word)):
                if word in non_english_words_dict:
                    non_english_words_dict[word] += 1
                    total_number_of_non_english_words += 1
                else:
                    non_english_words_dict[word] = 1
                    total_number_of_non_english_words += 1

    return non_english_words_dict, total_number_of_non_english_words