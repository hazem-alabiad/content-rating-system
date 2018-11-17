import requests
import json
import zipfile
import os

def get_rating(movie_id):
    api_key = "6da2935ca2ac0b1e97263a0027a2edeb"
    base_url = "https://api.themoviedb.org/3/movie/{0}?api_key={1}&append_to_response=release_dates".format(movie_id, api_key)
    response = requests.get(base_url)

    if response.status_code == 200 :
        response_json = json.loads(response.content.decode('utf-8'))
        
        #Extract film rating from json response (certificate)
        resutls_array = (response_json["release_dates"])["results"]
        for element_dic in resutls_array:
            if element_dic["iso_3166_1"] == "US":
                release_dates_array =  element_dic["release_dates"]
                certificate = release_dates_array[0]["certification"]
                if certificate == "":
                    return  "---UNRATED----"
                else:
                    return certificate
        return "---UNRATED----"
          
    else:
        return "ERROR"

def rat_unrated_films(intput_path, output_path):
    for filename in os.listdir(intput_path):
        print(filename)
        imbd_id = filename.split("_")[1]
        file_number = filename.split("_")[0]
        
        try:
            movie_rating = get_rating(imbd_id)
            zf = zipfile.ZipFile(os.path.join(intput_path, filename))
            zf.extractall(path = output_path + movie_rating + "_" +  file_number)
        except:
            pass




def unziped_files(intput_path, output_path):
    for filename in os.listdir(intput_path):
        print(filename)
        try:
            zf = zipfile.ZipFile(os.path.join(intput_path, filename))
            zf.extractall(path = output_path + filename)
        except:
            pass


