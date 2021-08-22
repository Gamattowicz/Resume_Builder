from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView, CreateView

from resumes.models import Resume
from .forms import SchoolFormSet
from .models import School


class SchoolCreateView(LoginRequiredMixin, CreateView):
    template_name = "school_form.html"
    success_message = "School was created successfully"

    def get(self, *args, **kwargs):
        formset = SchoolFormSet(queryset=School.objects.none())
        return self.render_to_response({"formset": formset})

    def post(self, *args, **kwargs):
        formset = SchoolFormSet(data=self.request.POST)
        if formset.is_valid():
            instances = formset.save(commit=False)
            for instance in instances:
                resume_id = self.kwargs["pk"]
                instance.resume = Resume.objects.get(id=resume_id)
                instance.save()
            formset.save()
            return redirect(
                reverse_lazy(
                    "experiences:create_experience", kwargs={"pk": self.kwargs["pk"]}
                )
            )
        return self.render_to_response({"formset": formset})


class SchoolUpdateView(LoginRequiredMixin, UpdateView):
    model = School
    template_name = "school_update.html"
    success_url = reverse_lazy(
        "resumes:resumes",
    )
    success_message = "School was updated successfully"

    def get(self, *args, **kwargs):
        formset = SchoolFormSet(
            queryset=School.objects.filter(resume_id=self.kwargs["pk"])
        )
        return self.render_to_response({"formset": formset})

    def post(self, request, *args, **kwargs):
        formset = SchoolFormSet(data=self.request.POST)

        if formset.is_valid():
            formset.save()
            messages.success(self.request, self.success_message)
            return redirect(reverse_lazy("resumes:resumes"))
        return self.render_to_response({"formset": formset})
