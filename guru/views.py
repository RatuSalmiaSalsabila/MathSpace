from django.shortcuts import render

# Create your views here.
def guru(request):
    return render(request, 'loginguru.html')

def guru1(request):
    return render(request, 'registrasiguru.html')
