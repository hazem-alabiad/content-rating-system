import pickle
import numpy as np

def in_pickle(pick_name):
    with open(pick_name + ".pkl", "rb") as pkl:
        return pickle.load(pkl)


# returns the average, n dimensioned, vector embedding of every word in a given document
# it sums all the vector values of every word in the document and then divides them by their count
# if a given word is not in the vocabulary of the model, it ignores it
def average_word_vectors(words, model, vocabulary, num_features):
    feature_vector = np.zeros((num_features,), dtype="float64")
    nwords = 0.
    for word in words:
        if word in vocabulary:
            nwords = nwords + 1.
            feature_vector = np.add(feature_vector, model[word])

    if nwords:
        feature_vector = np.divide(feature_vector, nwords)

    return feature_vector

svm_classifier = in_pickle("./pickles/svm_final_classifier")
word2vec_model = in_pickle("./pickles/word2vecModel_glove_6b_300d")

vocabulary = set(word2vec_model.wv.vocab)

# takes a list of tokens (words)
# returns the predicted classification of the document (0: not suitable, 1: suitable)
def classify(list_of_words):
    text_vector_representation = average_word_vectors(list_of_words, word2vec_model, vocabulary, 300)
    prediction = svm_classifier.predict([text_vector_representation])

    return prediction
