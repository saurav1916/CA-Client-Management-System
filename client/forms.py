from django import forms
from .models import Clientinfo

class addform(forms.ModelForm):
    class Meta:
        model = Clientinfo
        fields='__all__'