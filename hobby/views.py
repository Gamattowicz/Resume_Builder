from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from django.views.generic import ListView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Hobby
from .forms import HobbyFormSet, HobbyForms
from resumes.models import Resume
from django.http import HttpResponseRedirect


class HobbyCreateView(LoginRequiredMixin, TemplateView):
    template_name = 'hobby_form.html'

    def get(self, *args, **kwargs):
        formset = HobbyFormSet(queryset=Hobby.objects.none())
        return self.render_to_response({'formset': formset})

    def post(self, *args, **kwargs):
        formset = HobbyFormSet(data=self.request.POST)
        if formset.is_valid():
            instances = formset.save(commit=False)
            for instance in instances:
                resume_id = self.kwargs['pk']
                instance.resume = Resume.objects.get(id=resume_id)
                instance.save()
            formset.save()
            return redirect(reverse_lazy('resumes:resume', kwargs={'pk': self.kwargs['pk']}))
        return self.render_to_response({'formset': formset})


class HobbyUpdateView(LoginRequiredMixin, UpdateView):
    model = Hobby
    form_class = HobbyForms
    formset_class = HobbyFormSet
    template_name = 'hobby_update.html'
    success_url = reverse_lazy('resumes:resumes',)

    def get(self, *args, **kwargs):
        formset = HobbyFormSet(queryset=Hobby.objects.filter(resume_id=self.kwargs['pk']))
        return self.render_to_response({'formset': formset})

    def post(self, request, *args, **kwargs):
        formset = HobbyFormSet(data=self.request.POST)

        if formset.is_valid():
            formset.save()
            return redirect(reverse_lazy('resumes:resumes'))
        return self.render_to_response({'formset': formset})


class HobbyListView(LoginRequiredMixin, ListView):
    model = Hobby
    template_name = 'hobby_list.html'