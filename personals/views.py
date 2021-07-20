from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Personal
from .forms import PersonalForms
from resumes.models import Resume
from django.shortcuts import get_object_or_404
from django.contrib.messages.views import SuccessMessageMixin


class PersonalCreateView(LoginRequiredMixin, CreateView):
    model = Personal
    form_class = PersonalForms

    def form_valid(self, form):
        resume_id = self.kwargs['pk']
        form.instance.resume = Resume.objects.get(id=resume_id)
        return super(PersonalCreateView, self).form_valid(form)


class PersonalUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = Personal
    form_class = PersonalForms
    success_url = reverse_lazy('resumes:resumes')
    template_name = 'personals/personal_update.html'
    success_message = "Personal was updated successfully"

    def get_object(self, queryset=None):
        obj = get_object_or_404(Personal, resume_id=self.kwargs['pk'])
        return obj