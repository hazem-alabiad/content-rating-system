from django.shortcuts import render
from django.views.generic import TemplateView

class Feedback(TemplateView):
    
    def post(self, request):
        return ""
