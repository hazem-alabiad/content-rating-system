import re
import os
from nltk.corpus import stopwords
import pickle


from nltk.tokenize import word_tokenize
import pandas as pd

# Parse each translation file inside the translates_path directory and output them to the output_path directory
def parse_raw_translates(translates_path, output_path):
    file_number = 1
    
    for directory_name in os.listdir(translates_path):
        translate_file_name = os.listdir(os.path.join(translates_path, directory_name))[0]
        film_rating = directory_name.split("_")[0]
        print(film_rating)

        read_file = open(os.path.join(translates_path, directory_name, translate_file_name), encoding = "utf-8", errors="ignore")
        write_file = open(os.path.join(output_path, film_rating + "_" + str(file_number)), "w")
        file_number +=1

        write_buffer = ""
        lines_count = 0
        lines = []

        for line in read_file:
            line=str(line)
            if line[0] == '\n':
                for i, already_read_lines in enumerate(lines):
                    if i != 0 and i !=1:
                        already_read_lines = already_read_lines.split('\n')[0]
                        write_buffer = write_buffer + already_read_lines
                        write_buffer = write_buffer + " "

                lines = []
            else:
                lines.append(line)

        write_file.write(write_buffer)

        read_file.close()
        write_file.close()

# cleaning function for the whole text
def clean_text(text):
    """
    Remove "(strings)" or "<string>" or "[string]" or {string}" from text file.
    """
    regex = re.compile('(<.*?>) | (\(.*?\)) | (\[.*?\]) | (\{.*?\})' )
    cleantext = re.sub(regex, '', text)
    return cleantext

# Cleaning function for each token
def clean_tokens(tokens_list):
    """
    General purpose tokens cleaning function.
    Note : The order of the functions is important.
    """

    # To lowercase
    cleaned_tokens = [token.lower() for token in tokens_list]

    # Remove numbers, punctuation marks or words contains non-characters like "don`t"
    cleaned_tokens = [token for token in cleaned_tokens if token.isalpha()]

    # Remove stop words
    stop_words = set(stopwords.words('english'))
    cleaned_tokens = [token for token in cleaned_tokens if not token in stop_words]

    # Remove words with one character
    cleaned_tokens = [token for token in cleaned_tokens if len(token) > 1]

    """ #Words stemming
    porter = PorterStemmer()
    cleaned_tokens = [porter.stem(token) for token in cleaned_tokens] 
    """
    return cleaned_tokens

# Tokenize and pickle, takes the directory that contatins
def preprocess_file(directory_path, file_name,utf_8):
    print(file_name)
    if(utf_8):
        input_file = open(directory_path + file_name, "r",encoding="utf8")
    else:
        input_file = open(directory_path + file_name, "r")

    text = input_file.read()
    cleaned_text = clean_text(text)
    tokens = word_tokenize(cleaned_text)
    cleaned_tokens = clean_tokens(tokens)
    return cleaned_tokens

######After tokenization more cleaning#######


#read the whole dataset into one Pandas DataFrame
def read_into_dataframe(input_path, output_path):
    movies_dic = {
   "rating" : [],
   "movie_words" : []
    }

    for file_name in os.listdir(input_path):
        rating = file_name.split("_")[0]
        pickle_object = open("./pickle_files_1/" + file_name, "rb")
        movie_dic = pickle.load(pickle_object)
        sentence_list = [movie_dic[key] for key in movie_dic.keys()]
        word_list = []
    
    for sentence in sentence_list:    
        word_list = word_list + sentence
        
    if rating == "G" or rating == "PG" or rating == "PG-13" or rating == "R" or rating == "NC-17":
        movies_dic["rating"].append(rating)
        movies_dic["movie_words"].append(word_list)
    else: 
        #Any film without rating, or rated with different rating system
        #or even a series(We foucs just on films right now) will be considered "OTHER"
        movies_dic["rating"].append("OTHER")       
        movies_dic["movie_words"].append(word_list)

    movies_table = pd.DataFrame(movies_dic)
    return movies_table

#Calculate the frequency of words for each rating categorey
def calculate_word_frequency(movies_table, rating):
    rated_movies_table = movies_table.loc[movies_table["rating"] == rating]["movie_words"]
    movies_word_list = []
    for index in rated_movies_table.index:
        movies_word_list = movies_word_list + rated_movies_table[index]

    movies_word_Series = pd.Series(movies_word_list)
    movies_words_frequency = movies_word_Series.value_counts()
    
    return movies_words_frequency

#Delete most frequent n words
def delete_most_frequent(movies_table, rating, n):
    top_words = calculate_word_frequency(movies_table, rating)
    top_10_words = set(top_words.head(n).keys().tolist())

    new_words = []

    for words_list in movies_table[movies_table["rating"] == rating]["movie_words"]:
        new_words_list = [i for i in words_list if not i in top_10_words]
        new_words.append(new_words_list)

    movies_table.loc[movies_table["rating"] == rating,"movie_words"] = new_words.copy()

#Delete words with count equal to "count"
def delete_rare_words(movie_table, rating, count):
    freq = calculate_word_frequency(movie_table, rating).to_dict()
    rare_words_list = {key for key in freq.keys() if freq[key] == count}

    new_words = []

    for words_list in movie_table[movie_table["rating"] == rating]["movie_words"]:
        new_words_list = [i for i in words_list if not i in rare_words_list]
        new_words.append(new_words_list)

        movie_table.loc[movie_table["rating"] == rating,"movie_words"] = new_words.copy()

##################################################################################
### Steps of the programs:
   # 1- Just run the previous function in order and then pickle your dataset(movies) table into one file and its ready for the
   ### model

