from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Resume
from .forms import ResumeForms


class ResumeCreateView(LoginRequiredMixin, CreateView):
    model = Resume
    form_class = ResumeForms

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(ResumeCreateView, self).form_valid(form)


class ResumeListView(LoginRequiredMixin, ListView):
    model = Resume
    context_object_name = 'resumes'

    def get_queryset(self):
        queryset = Resume.objects.filter(user=self.request.user)
        return queryset


class ResumeDetailView(LoginRequiredMixin, DetailView):
    model = Resume
    context_object_name = 'resume'
    template_name = 'resume_2.html'


class ResumeDeleteView(LoginRequiredMixin, DeleteView):
    model = Resume
    context_object_name = 'resume'
    success_url = reverse_lazy('resumes:resumes')
    template_name = 'resume_delete.html'