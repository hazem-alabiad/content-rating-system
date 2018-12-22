from django.shortcuts import render
from django.views.generic import TemplateView

class AboutUs(TemplateView):
    
    def get(self, request):
        return render(request, "./aboutUs/aboutUs.html", context=None)
