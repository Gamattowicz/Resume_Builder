from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView, CreateView
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import School
from .forms import SchoolFormSet, SchoolForms
from resumes.models import Resume


class SchoolCreateView(LoginRequiredMixin, CreateView):
    template_name = 'school_form.html'

    def get(self, *args, **kwargs):
        formset = SchoolFormSet(queryset=School.objects.none())
        return self.render_to_response({'formset': formset})

    def post(self, *args, **kwargs):
        formset = SchoolFormSet(data=self.request.POST)
        if formset.is_valid():
            instances = formset.save(commit=False)
            for instance in instances:
                resume_id = self.kwargs['pk']
                instance.resume = Resume.objects.get(id=resume_id)
                instance.save()
            formset.save()
            return redirect(reverse_lazy('experiences:create_experience', kwargs={'pk': self.kwargs['pk']}))
        return self.render_to_response({'formset': formset})


class SchoolUpdateView(LoginRequiredMixin, UpdateView):
    model = School
    form_class = SchoolForms
    success_url = reverse_lazy('experiences:add_experience')
    template_name = 'schools/school_update.html'


class SchoolListView(LoginRequiredMixin, ListView):
    model = School
    template_name = 'school_list.html'