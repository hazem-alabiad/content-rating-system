from django.shortcuts import render
from django.views.generic import TemplateView

class CrsApp(TemplateView):
    
    def get(self, request):
        return render(request, "./crsApp/index.html", context=None)
