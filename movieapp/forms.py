from django import forms

class MovieSearchForm(forms.Form):
    search = forms.CharField(max_length=100)
