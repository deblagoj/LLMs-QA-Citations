from django import forms

class QuestionForm(forms.Form):
    question = forms.CharField(label='question', max_length=100)