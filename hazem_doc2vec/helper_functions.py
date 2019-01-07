import pickle
import random

def out_pickle(pickle_path, variable_name):
    """
    Function that pickles out a variable
    :param pickle_path: in pickle's path including the name
    :param variable_name: the variable to be pickled out
    :return: nothing
    """
    with open(pickle_path + ".pkl", "wb") as pkl:
        pickle.dump(variable_name, pkl)


def in_pickle(pickle_path):
    """
    Function that pickles in a variable
    :param pickle_path: in pickle's path including the name
    :return: the variable that contains pickled in data
    """
    with open(pickle_path + ".pkl", "rb") as pkl:
        return pickle.load(pkl)

def shuffle_corpus_labels(corpus, labels):
    """
    Function to shuffle corpus & labels in the same order
    :rtype:
    """
    z = list(zip(corpus, labels))
    random.shuffle(z)
    c, l = zip(*z)
    return c, l

