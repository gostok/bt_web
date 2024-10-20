from django import forms
from .models import *

class SessionForm(forms.ModelForm):
    class Meta:
        model = Session
        fields = ['date', 'time', 'name', 'contact_info']