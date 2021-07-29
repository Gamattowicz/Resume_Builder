from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Skill
from .forms import SkillFormSet
from resumes.models import Resume
from django.contrib import messages


class SkillCreateView(LoginRequiredMixin, CreateView):
    template_name = 'skill_form.html'
    success_message = 'Skill was created successfully'

    def get(self, *args, **kwargs):
        formset = SkillFormSet(queryset=Skill.objects.none())
        return self.render_to_response({'formset': formset})

    def post(self, *args, **kwargs):
        formset = SkillFormSet(data=self.request.POST)
        if formset.is_valid():
            instances = formset.save(commit=False)
            for instance in instances:
                resume_id = self.kwargs['pk']
                instance.resume = Resume.objects.get(id=resume_id)
                instance.save()
            formset.save()
            return redirect(reverse_lazy('hobby:create_hobby', kwargs={'pk': self.kwargs['pk']}))
        return self.render_to_response({'formset': formset})


class SkillUpdateView(LoginRequiredMixin, UpdateView):
    model = 'Skill'
    template_name = 'skill_update.html'
    success_url = reverse_lazy('resumes:resumes',)
    success_message = 'Skill was updated successfully'

    def get(self, *args, **kwargs):
        formset = SkillFormSet(queryset=Skill.objects.filter(resume_id=self.kwargs['pk']))
        return self.render_to_response({'formset': formset})

    def post(self, request, *args, **kwargs):
        formset = SkillFormSet(data=self.request.POST)

        if formset.is_valid():
            formset.save()
            messages.success(self.request, self.success_message)
            return redirect(reverse_lazy('resumes:resumes'))
        return self.render_to_response({'formset': formset})


class SkillListView(LoginRequiredMixin, ListView):
    model = Skill
    template_name = 'skill_list.html'