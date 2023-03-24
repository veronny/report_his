from django import forms
from .models import Disa, Red, Microred, Establecimiento 

class MiFormulario(forms.Form):  
    diresa = forms.ModelChoiceField(queryset=Disa.objects.all())
    red = forms.ModelChoiceField(queryset=Red.objects.all())    
    microred = forms.ModelChoiceField(queryset=Microred.objects.all())
    establecimiento = forms.ModelChoiceField(queryset=Establecimiento.objects.all())
