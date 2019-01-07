from django.shortcuts import render
from django.views.generic import TemplateView
from rater.models import Book
import difflib
from collections import namedtuple


# Create your views here.
class Search(TemplateView):

    def get(self, request):
        return render(request, "./search/search.html", context=None)

    def post(self, request):
        input_book_name = request.POST.get("input_book_name")

        books = Book.objects.all()
        books_names = []
        for book in books:
            book_name = book.book_name.split(".")[len(book.book_name.split(".")) - 2 ]
            books_names.append(book_name)

        if len(books_names) > 0:
            similar_books = difflib.get_close_matches(input_book_name, books_names, n = 8, cutoff=0.4)
            print([i for i in similar_books])
            similar_books_rating = []
            similar_books_rating_string = []
            books = Book.objects.all()
            
            for book in books:
                book_name = book.book_name.split(".")[len(book.book_name.split(".")) - 2 ]
                if book_name in similar_books:
                    book_rating = book.predicted_label
                    similar_books_rating.append(book_rating)

            if len(similar_books_rating) > 0 :
                for (index,value) in enumerate(similar_books):
                    if  similar_books_rating[index] == 1 :
                            similar_books_rating_string.append("Appropriate For Chidlern")
                    elif similar_books_rating[index] == 0 :
                            similar_books_rating_string.append("Not Appropriate For Chidlern")
                    
                #convert each book name and book rating into one object in order to render in the template
                books_obj = []
                for (index, value) in enumerate(similar_books):
                    Book_obj = namedtuple("RoBook_objw", ["book_name", "book_rating"], verbose=False, rename=False)   
                    book_obj = Book_obj(book_name=similar_books[index],book_rating=similar_books_rating_string[index])
                    books_obj.append(book_obj)
                
                responce = {
                    "success" : True,
                    "books" : books_obj
                    #"book_names" : similar_books,
                    #"books_rating" : similar_books_rating_string
                }
                
                return render(request, "./search/search.html", context=responce)
            
            else: 

                responce = {
                    "not_sccuess" : True,
                    "message" : "Sorry. No matched books in our database!. Please try again later"
                }

                return render(request, "./search/search.html", context=responce)



            
        else: 

            responce = {
                "not_sccuess" : True,
                "message" : "Sorry. No matched books in our database!. Please try again later"
            }

            return render(request, "./search/search.html", context=responce)


