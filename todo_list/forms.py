from django import forms
from .models import List
#This page is dedicated to creating forms in django. Had to be manually created for us to use

class ListForm(forms.ModelForm):
    class Meta:
        model = List
        fields = "item", "completed" #Look at models.py file for what to insert here