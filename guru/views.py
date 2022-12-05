from django.shortcuts import render
from guru.models import dataguru
from guru.forms import FormGuru

# Create your views here.
def loginguru(request):
    return render(request, 'loginguru.html')

def registrasiguru(request):
    return render(request, 'registrasiguru.html')
