from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import ListView, DetailView, CreateView

from webapp.forms import AnswerOptionForm
from webapp.models import Answer, Poll, Choice


class AnswerOptionIndexViews(ListView):
    template_name = 'answer/answers.html'
    context_object_name = 'answers'
    model = Answer
    ordering = ['-created_at']
    paginate_by = 10
    paginate_orphans = 1

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        return context


class AnswerSelectView(CreateView):
    template_name = 'answer/select_answer.html'
    model = Answer
    form_class = AnswerOptionForm

    def get(self, request, *args, **kwargs):
        poll = get_object_or_404(Poll, pk=kwargs['pk'])
        choices = poll.choices.all()
        context = {
            'poll': poll,
            'choices': choices
        }
        return render(request, 'answer/select_answer.html', context)

    def post(self, request, *args, **kwargs):
        pk = request.POST['option']
        choice = get_object_or_404(Choice, pk=pk)

        poll = get_object_or_404(Poll, pk=kwargs['pk'])
        Answer.objects.create(option=choice, poll=poll)
        return redirect('poll_index')
