from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Personal
from .forms import PersonalForms


class PersonalCreateView(LoginRequiredMixin, CreateView):
    model = Personal
    form_class = PersonalForms
    success_url = reverse_lazy('schools:add_school')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(PersonalCreateView, self).form_valid(form)