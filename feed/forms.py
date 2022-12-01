from django import forms

class PostForm(forms.Form):
    Title= forms.CharField()
    image= forms.FileField()