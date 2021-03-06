from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView

from resumes.models import Resume
from .forms import HobbyFormSet
from .models import Hobby


class HobbyCreateView(LoginRequiredMixin, CreateView):
    template_name = "hobby_form.html"
    success_message = "Hobby was created successfully"

    def get(self, *args, **kwargs):
        formset = HobbyFormSet(queryset=Hobby.objects.none())
        return self.render_to_response({"formset": formset})

    def post(self, *args, **kwargs):
        formset = HobbyFormSet(data=self.request.POST)
        if formset.is_valid():
            instances = formset.save(commit=False)
            for instance in instances:
                resume_id = self.kwargs["pk"]
                instance.resume = Resume.objects.get(id=resume_id)
                instance.save()
            formset.save()
            messages.success(self.request, self.success_message)
            return redirect(reverse_lazy("resumes:resumes"))
        return self.render_to_response({"formset": formset})


class HobbyUpdateView(LoginRequiredMixin, UpdateView):
    model = Hobby
    template_name = "hobby_update.html"
    success_url = reverse_lazy(
        "resumes:resumes",
    )
    success_message = "Hobby was updated successfully"

    def get(self, *args, **kwargs):
        formset = HobbyFormSet(
            queryset=Hobby.objects.filter(resume_id=self.kwargs["pk"])
        )
        return self.render_to_response({"formset": formset})

    def post(self, request, *args, **kwargs):
        formset = HobbyFormSet(data=self.request.POST)

        if formset.is_valid():
            formset.save()
            messages.success(self.request, self.success_message)
            return redirect(reverse_lazy("resumes:resumes"))
        return self.render_to_response({"formset": formset})


class HobbyListView(LoginRequiredMixin, ListView):
    model = Hobby
    template_name = "hobby_list.html"
