from django.shortcuts import render
from django.views.generic import TemplateView

class ContactUs(TemplateView):
    
    def get(self, request):
        return render(request, "./contactUs/contactUs.html", context=None)
