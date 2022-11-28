from django.shortcuts import render

# Create your views here.
def siswa(request):
    return render(request, 'loginsiswa.html')

def siswa1(request):
    return render(request, 'registrasisiswa.html')