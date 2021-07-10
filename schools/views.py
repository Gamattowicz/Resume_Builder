from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView
from django.contrib.auth.decorators import login_required
from .models import School
from .forms import SchoolFormSet


@login_required(login_url='users:login')
class SchoolListView(ListView):
    model = School
    template_name = 'school_list.html'


@login_required(login_url='users:login')
class SchoolAddView(TemplateView):
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
