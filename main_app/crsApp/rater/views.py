from django.shortcuts import render
from django.shortcuts import render_to_response
from django.views.generic import TemplateView
from django.template import RequestContext
from .modules import converter
from django.core.files.storage import FileSystemStorage

import os


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
            input_file_name = input_file.name
            fs = FileSystemStorage()
            filename = fs.save(input_file.name, input_file)
            uploaded_file_url = fs.url(filename)            
            #Convert the file to text, if it contain non english words or nothing or in not supported format
            text_file = converter.convert_to_text(uploaded_file_url)
            if text_file == "00":
                response = {
                    "message" : "Error while opening the book, make sure that the book exist and its name does not contain spaces!"
                }
                return render(request, "./rater/error.html", context=response)
            elif text_file == "01":
                response = {
                    "message" : "Book is  corraped or with no format, please try another book!"
                }
                return render(request, "./rater/error.html", context=response)
            elif text_file == "10":
                response = {
                    "message" : "Book has a format rather than pdf, txt or equb, please try another book!"
                }
                return render(request, "./rater/error.html", context=response)
            elif text_file == "11":
                response = {
                    "message" : "Error while extracting text from the book, please try another book!"
                }
                return render(request, "./rater/error.html", context=response)
            
            else:
                #First step check if the book is already stored in the database, if so return the rating input_book
                
                #Second step convert the file, if it is in the correct format, if not return error

                #Third preprocess the file and get its token and send to the model

                #Fourth, get the rating and return it to the user
                response = {
                    "message" : "The rating of the book is ",
                    "rating"  : "appropriate for children"
                }
                return render(request, "./rater/success.html", context=response)