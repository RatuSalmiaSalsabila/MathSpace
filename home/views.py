from django.shortcuts import render

# Create your views here.
def bukahome(request):
    return render(request, 'bukahome.html')