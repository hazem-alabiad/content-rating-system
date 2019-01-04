from django.shortcuts import render
from django.shortcuts import render_to_response
from django.views.generic import TemplateView
from django.template import RequestContext
from .modules import converter
from django.core.files.storage import FileSystemStorage

from .modules import preprocessor
import os
from datasketch import MinHash
from .models import Book

import datetime
from pytz import timezone
import ast

# Create your views here.
class Rater(TemplateView):
    """
    The rater class, responsible for rating the uploaded books
    Exceptions:
        1- The uploaded books is not in english words
        2- The uploaded books is not in right format
        3- The uploaded file is corrupted or no text can be extracted from it
        4- 
    """
    def post(self, request):
        if request.FILES["uploaded_book"]:
            #Save the file to the raw file dir under "basedir + /media"
            #Note: i did not check if previously books with the same name has been uploaded, because user can have book is incorect name
            input_file = request.FILES['uploaded_book']
            save_or_not = request.POST.get("save")

            input_file_name = input_file.name
            fs = FileSystemStorage()     #For raw books

            filename = fs.save(input_file.name, input_file)
            uploaded_file_url = fs.url(filename)
            
            #Convert the file to text, if it contain non english words or nothing or in not supported format. then save it
            text = converter.convert_to_text(uploaded_file_url)
            
            save_txt_file_path = os.getcwd() + "/media2/" + filename.split(".")[0] + ".txt"
            saved_txt_file = open(save_txt_file_path, "w")
            saved_txt_file.write(str(text))
            saved_txt_file.close()            
        

            if save_or_not == "dont_save":
                fs.delete(filename)

            #Return error message if the text extraing process was not successful   
            if text == "00":
                response = {
                    "message" : "Error while opening the book, make sure that the book exist and its name does not contain spaces!"
                }
                return render(request, "./rater/error.html", context=response)
            elif text == "01":
                response = {
                    "message" : "Book is corraped or with no format, please try another book!"
                }
                return render(request, "./rater/error.html", context=response)
            elif text == "10":
                response = {
                    "message" : "Book has a format rather than pdf, txt or equb, please try another book!"
                }
                return render(request, "./rater/error.html", context=response)
            elif text == "11":
                response = {
                    "message" : "Error while extracting text from the book, please try another book!"
                }
                return render(request, "./rater/error.html", context=response)
            
            else:         

                #First step, preprocess the book and check it is fully english or not
                book_tokens, percent_of_non_english_words = preprocessor.preprocess_file(save_txt_file_path)

                print(percent_of_non_english_words)

                if percent_of_non_english_words > 0.2 :
                    message = "Please submit an English book, for now we can not handle non-English books"
                    response = {
                    "message" : message
                    }
                    return render(request, "./rater/error.html", context=response)

                if save_or_not == "dont_save":
                    fs.delete(filename)
                    new_book_rating = ""
                    
                    if new_book_rating == "1":
                        rating  = "Appropriate for children",
                    elif new_book_rating == "0":
                        rating  = "Not Appropriate for children",

                    response = {
                        "message" : "The rating of the book is ",
                        "rating"  : rating,
                        "book_name" : filename
                    }
                
                output = open(filename + ".txt", "w")

                output.write(str(book_tokens))

                #Third step calculate the min hash of the tokens
                new_book_hash = MinHash(num_perm=256)
                for token in book_tokens:
                    new_book_hash.update(token.encode("utf8"))
                
                # Fourth step, Check if there is similar rated book in the database, by comparing the hashes and if the two hash has jasccard similarity more than 0.8
                # then the two books havethe same rating
                # finally return the ground-truth rating if aviable. If not return the predicated one. 
                books = Book.objects.all()
                for book in books:
                    book_hash_values = book.book_hash
                    book_hash_values= ast.literal_eval(book_hash_values)

                    #Convert the stored string min hash to min hash object
                    book_min_hash_object = MinHash(num_perm=256,hashvalues=book_hash_values)

                    if new_book_hash.jaccard(book_min_hash_object) >= 0.8 :
                        
                        if book.ground_truth_label != "":
                            new_book_rating =  book.ground_truth_label

                            if new_book_rating == "1":
                                rating  = "Appropriate for children",
                            elif new_book_rating == "0":
                                rating  = "Not Appropriate for children",

                            response = {
                                "message" : "The rating of the book is ",
                                "rating"  : rating,
                                "book_name" : filename
                            }
                            return render(request, "./rater/success.html", context=response)
                        else:
                            new_book_rating =  book.predicted_label

                            if new_book_rating == "1":
                                rating  = "Appropriate for children",
                            elif new_book_rating == "0":
                                rating  = "Not Appropriate for children",

                            print("same book as before")

                            response = {
                                "message" : "The rating of the book is ",
                                "rating"  : rating,
                                "book_name" : filename
                            }
                            
                            return render(request, "./rater/success.html", context=response)
                        
                    else:
                        pass

                #Fifth step. If no similar book is uploaded, rate the book and save it
                new_book_rating = "1"
                
                #Save the book with time equal to the time in the gmt timezone
                new_book = Book(book_hash=str(list(new_book_hash.hashvalues)), book_name = filename, upload_date=datetime.datetime.now(), update_date=datetime.datetime.now(), predicted_label=new_book_rating, ground_truth_label="")
                new_book.save()

                if new_book_rating == "1":
                    rating  = "Appropriate for children",
                elif new_book_rating == "0":
                    rating  = "Not Appropriate for children",
                
                response = {
                    "message" : "The rating of the book is ",
                    "rating"  : rating,
                    "book_name" : filename
                }

                return render(request, "./rater/success.html", context=response)