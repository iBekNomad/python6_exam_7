from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse

from webapp.models import Poll, Choice
from webapp.forms import ChoiceSelectForm

from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, ListView


class ChoiceSelectView(CreateView):
    model = Choice
    template_name = 'choice/choice_create.html'
    form_class = ChoiceSelectForm

    def form_valid(self, form):
        poll = get_object_or_404(Poll, pk=self.kwargs.get('pk'))
        option = form.save(commit=False)
        option.poll = poll
        option.save()
        # form.save_m2m()  ## для сохранения связей многие-ко-многим
        return redirect('poll_view', pk=poll.pk)

    # def form_valid(self, form):
    #     poll = get_object_or_404(Poll, pk=self.kwargs.get('pk'))
    #     form.instance.poll = poll
    #     return super().form_valid(form)


class ChoiceUpdateView(UpdateView):
    model = Choice
    form_class = ChoiceSelectForm
    template_name = 'choice/choice_update.html'

    def get_success_url(self):
        return reverse('poll_view', kwargs={'pk': self.object.poll.pk})


class ChoiceDeleteView(DeleteView):
    template_name = 'choice/choice_delete.html'
    model = Choice

    def get_success_url(self):
        return reverse('poll_view', kwargs={'pk': self.object.poll.pk})
