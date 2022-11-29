from dataclasses import fields
from django.forms import ModelForm
from siswa.models import siswa

class FormSiswa(ModelForm):
    class Meta:
        model = siswa
        fields = '__all__'
