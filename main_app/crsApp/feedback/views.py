from django.shortcuts import render
from django.views.generic import TemplateView
from time import gmtime, strftime

class Feedback(TemplateView):
    
    def post(self, request):
        #extract the data from the feedback
        feedback_time =  strftime("%Y-%m-%d %H:%M:%S", gmtime())
        feedback_message = request.POST.get("comment")
        feedback_email = request.POST.get("email")
        feedback_book_name = request.POST.get("book_name")

        response = {
            "message" : "Thanks you for your feedback, we will definitely consider it in improving our system"
        }

        return render(request, "./feedback/success.html", context=response)

