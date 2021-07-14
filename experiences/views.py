from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from django.views.generic import ListView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Experience
from .forms import ExperienceFormSet, ExperienceForms
from resumes.models import Resume


class ExperienceCreateView(LoginRequiredMixin, TemplateView):
    template_name = 'experience_form.html'

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
    form_class = ExperienceForms
    success_url = reverse_lazy('skills:create_skill')
    template_name = 'experiences/experience_update.html'


class ExperienceListView(LoginRequiredMixin, ListView):
    model = Experience
    template_name = 'experience_list.html'