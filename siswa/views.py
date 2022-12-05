from django.shortcuts import render
from siswa.models import datasiswa
from siswa.forms import FormSiswa


# Create your views here.
def loginsiswa(request):
    return render(request, 'loginsiswa.html')


def registrasisiswa(request):
    return render(request, 'registrasisiswa.html')