from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from django.views.generic import ListView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Experience
from .forms import ExperienceFormSet
from resumes.models import Resume
from django.contrib import messages


class ExperienceCreateView(LoginRequiredMixin, TemplateView):
    template_name = 'experience_form.html'
    success_message = "Experience was created successfully"

    def get(self, *args, **kwargs):
        formset = ExperienceFormSet(queryset=Experience.objects.none())
        return self.render_to_response({'formset': formset})

    def post(self, *args, **kwargs):
        formset = ExperienceFormSet(data=self.request.POST)
        if formset.is_valid():
            instances = formset.save(commit=False)
            for instance in instances:
                resume_id = self.kwargs['pk']
                instance.resume = Resume.objects.get(id=resume_id)
                instance.save()
            formset.save()
            return redirect(reverse_lazy('skills:create_skill', kwargs={'pk': self.kwargs['pk']}))
        return self.render_to_response({'formset': formset})


class ExperienceUpdateView(LoginRequiredMixin, UpdateView):
    model = Experience
    template_name = 'experience_update.html'
    success_url = reverse_lazy('resumes:resumes',)
    success_message = "Experience was updated successfully"

    def get(self, *args, **kwargs):
        formset = ExperienceFormSet(queryset=Experience.objects.filter(resume_id=self.kwargs['pk']))
        return self.render_to_response({'formset': formset})

    def post(self, request, *args, **kwargs):
        formset = ExperienceFormSet(data=self.request.POST)

        if formset.is_valid():
            formset.save()
            messages.success(self.request, self.success_message)
            return redirect(reverse_lazy('resumes:resumes'))
        return self.render_to_response({'formset': formset})


class ExperienceListView(LoginRequiredMixin, ListView):
    model = Experience
    template_name = 'experience_list.html'