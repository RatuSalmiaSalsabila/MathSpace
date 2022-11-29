from dataclasses import fields
from django.forms import ModelForm
from guru.models import guru

class FormGuru(ModelForm):
    class Meta:
        model = guru
        fields = '__all__'

widgets = {
            'nama' : forms.TextInput({'class':'form-control'}),
            'nip' : forms.TextInput({'class':'form-control'}),
            'tanggal_lahir' : forms.TextInput({'class':'form-control'}),
            'email' : forms.TextInput({'class':'form-control'}),
            'jenis_kelamin' : forms.TextInput({'class':'form-control'}),
        }
