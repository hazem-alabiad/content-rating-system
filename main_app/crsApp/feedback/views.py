from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Feedbacks
from rater.models import Book
import datetime

class Feedback(TemplateView):
    
    def post(self, request):
        #extract the data from the feedback
        feedback_message = request.POST.get("comment")
        feedback_email = request.POST.get("email")
        feedback_book_name = request.POST.get("book_name")
        feedback_book_id = request.POST.get("book_id")
         
        book = Book.objects.get(pk= feedback_book_id)
        new_feedback = Feedbacks(upload_date = datetime.datetime.now(), email=feedback_email, content=feedback_message, book=book)
        new_feedback.save()

        response = {
            "message" : "Thanks you for your feedback, we will definitely consider it in improving our system"
        }

        return render(request, "./feedback/success.html", context=response)