from dataclasses import field
from django import forms
from store.models import *

class ContactForm(forms.ModelForm):

    class Meta:
        model=Usercontact
        fields=("__all__")