# pyright: reportMissingModuleSource=false
from django import forms

class CreateNewCommit(forms.Form):
    name = forms.CharField(label="Name", max_length=255)
    day = forms.CharField(label="Day", max_length=255)
    date = forms.DateField(label="Date")
    time = forms.TimeField(label="Time")
    message = forms.CharField(label="Message", max_length=500)
    # check = forms.BooleanField(label="Check", required=False)