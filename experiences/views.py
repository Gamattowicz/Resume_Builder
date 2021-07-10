from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView
from django.contrib.auth.decorators import login_required
from .models import Experience
from .forms import ExperienceFormSet


@login_required(login_url='users:login')
class ExperienceListView(ListView):
    model = Experience
    template_name = 'experience_list.html'


@login_required(login_url='users:login')
class ExperienceAddView(TemplateView):
    template_name = 'add_experience.html'

    def get(self, *args, **kwargs):
        formset = ExperienceFormSet(queryset=Experience.objects.none())
        return self.render_to_response({'experience_formset': formset})

    def post(self, *args, **kwargs):
        formset = ExperienceFormSet(data=self.request.POST)

        if formset.is_valid():
            formset.save()
            return redirect(reverse_lazy('experiences:experience_list'))

        return self.render_to_response({'experience_formset': formset})
