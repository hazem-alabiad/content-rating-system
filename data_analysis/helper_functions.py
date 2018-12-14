import pickle


def open_pickle(path_to_pickle):
    pickle_in = open(path_to_pickle,'rb')
    data = pickle.load(pickle_in)
    return data


def combine_values_of_dict(dict):
    combined_values = []
    for key in dict:
        for word in dict[key]:
            combined_values.append(word)
    return combined_values

