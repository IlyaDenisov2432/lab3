
from .models import Obj
from django import forms

class ObjForm(forms.ModelForm):
     address = forms.CharField(label='')

     class Meta:
        model = Obj
        fields = ['address', ]
