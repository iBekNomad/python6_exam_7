from django import forms
from .models import Poll


class PollForm(forms.ModelForm):
    question = forms.CharField(max_length=2500, required=True, label='Вопрос', widget=forms.Textarea)

    class Meta:
        model = Poll
        fields = ['question']
