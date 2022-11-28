from dataclasses import fields
from django.forms import ModelForm
from guru.models import guru

class FormGuru(ModelForm):
    class Meta:
        model = guru
        fields = '__all__'
