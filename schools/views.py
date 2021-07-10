from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import School
from .forms import SchoolFormSet


class SchoolListView(LoginRequiredMixin, ListView):
    model = School
    template_name = 'school_list.html'


class SchoolAddView(LoginRequiredMixin, TemplateView):
    template_name = 'add_school.html'

    def get(self, *args, **kwargs):
        formset = SchoolFormSet(queryset=School.objects.none())
        return self.render_to_response({'school_formset': formset})

    def post(self, *args, **kwargs):
        formset = SchoolFormSet(data=self.request.POST)

        if formset.is_valid():
            formset.save()
            return redirect(reverse_lazy('api:school_list'))

        return self.render_to_response({'school_formset': formset})
