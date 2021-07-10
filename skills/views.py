from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Skill
from .forms import SkillFormSet


class SkillListView(LoginRequiredMixin, ListView):
    model = Skill
    template_name = 'skill_list.html'


class SkillAddView(LoginRequiredMixin, TemplateView):
    template_name = 'add_skill.html'

    def get(self, *args, **kwargs):
        formset = SkillFormSet(queryset=Skill.objects.none())
        return self.render_to_response({'skill_formset': formset})

    def post(self, *args, **kwargs):
        formset = SkillFormSet(data=self.request.POST)

        if formset.is_valid():
            formset.save()
            return redirect(reverse_lazy('skills:skill_list'))

        return self.render_to_response({'skill_formset': formset})
