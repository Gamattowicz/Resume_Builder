from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Resume
from .forms import ResumeForms


class ResumeCreateView(LoginRequiredMixin, CreateView):
    model = Resume
    form_class = ResumeForms

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(ResumeCreateView, self).form_valid(form)