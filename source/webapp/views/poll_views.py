from django.urls import reverse, reverse_lazy

from webapp.models import Poll
from webapp.forms import PollForm

from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, ListView


class IndexPollView(ListView):
    context_object_name = 'polls'
    model = Poll
    template_name = 'poll/poll_index.html'
    ordering = ['-created_at']
    paginate_by = 5
    paginate_orphans = 1

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        return context


class PollView(DetailView):
    template_name = 'poll/poll_view.html'
    model = Poll

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class PollCreateView(CreateView):
    template_name = 'poll/poll_create.html'
    model = Poll
    form_class = PollForm

    def get_success_url(self):
        return reverse('poll_view', kwargs={'pk': self.object.pk})


class PollUpdateView(UpdateView):
    template_name = 'poll/poll_update.html'
    model = Poll
    form_class = PollForm

    def get_success_url(self):
        return reverse('poll_view', kwargs={'pk': self.object.pk})


class PollDeleteView(DeleteView):
    template_name = 'poll/poll_delete.html'
    model = Poll
    success_url = reverse_lazy('poll_index')
