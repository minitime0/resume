from django.shortcuts import render
from django.views.generic import TemplateView

def main(request):
    return render(request, 'main.html')

class MainView(TemplateView):
    template_name = 'main.html'
