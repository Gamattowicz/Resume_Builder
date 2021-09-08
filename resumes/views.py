from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import DeleteView, TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView

from .forms import ResumeForms
from .models import Resume


class ResumeCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = Resume
    form_class = ResumeForms
    success_message = "Resume was created successfully"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(ResumeCreateView, self).form_valid(form)


class ResumeUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = Resume
    form_class = ResumeForms
    success_url = reverse_lazy("resumes:resumes")
    template_name = "resumes/resume_update.html"
    success_message = "Resume template was updated successfully"


class ResumeListView(LoginRequiredMixin, ListView):
    model = Resume
    context_object_name = "resumes"
    paginate_by = 6

    def get_queryset(self):
        queryset = Resume.objects.filter(user=self.request.user)
        return queryset


class ResumeDetailView(LoginRequiredMixin, DetailView):
    model = Resume
    context_object_name = "resume"

    def get_template_names(self):
        object = Resume.objects.get(id=self.kwargs["pk"])
        return f"resume_{object.template}.html"


class ResumeDeleteView(LoginRequiredMixin, DeleteView):
    model = Resume
    context_object_name = "resume"
    success_url = reverse_lazy("resumes:resumes")
    template_name = "resume_delete.html"
    success_message = "Resume deleted"

    def delete(self, request, *args, **kwargs):
        messages.error(self.request, self.success_message)
        return super(ResumeDeleteView, self).delete(request, *args, **kwargs)


class HomeView(TemplateView):
    template_name = "home.html"
