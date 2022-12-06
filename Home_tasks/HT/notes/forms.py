from django import forms
from django.contrib.auth.models import User

from notes.models import Notes


# class NoteForm(forms.Form):
#     title = forms.CharField(max_length=200)
#     text = forms.CharField(widget=forms.Textarea)
#     reminder = forms.DateTimeField()
#     category = forms.('Categories', related_name='note_category', on_delete=models.CASCADE)