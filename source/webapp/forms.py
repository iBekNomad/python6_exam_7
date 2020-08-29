from django import forms
from .models import Poll, Choice, Answer


class PollForm(forms.ModelForm):
    question = forms.CharField(max_length=2500, required=True, label='Вопрос', widget=forms.Textarea)

    class Meta:
        model = Poll
        fields = ['question']


class ChoiceSelectForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ['text']


class AnswerOptionForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['poll', 'option']
        widgets = {'option': forms.CheckboxSelectMultiple}
