from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Personal
from .forms import PersonalForms
from resumes.models import Resume


class PersonalCreateView(LoginRequiredMixin, CreateView):
    model = Personal
    form_class = PersonalForms
    success_url = reverse_lazy('schools:add_school')

    def form_valid(self, form):
        resume_id = self.kwargs['pk']
        form.instance.resume = Resume.objects.get(id=resume_id)
        return super(PersonalCreateView, self).form_valid(form)


class PersonalUpdateView(LoginRequiredMixin, UpdateView):
    model = Personal
    form_class = PersonalForms
    success_url = reverse_lazy('schools:add_school')
    template_name = 'personals/personal_update.html'