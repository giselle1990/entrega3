from django import forms 

from . import models 

class deudorform(forms.ModelForm):
    class Meta:
        model= models.Deudor
        fields= "__all__"
        