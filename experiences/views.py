from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView

from resumes.models import Resume
from .forms import ExperienceForms, ExperienceDescriptionFormSet, ExperienceFormSet
from .models import Experience, ExperienceDescription


class ExperienceCreateView(LoginRequiredMixin, CreateView):
    template_name = 'experience_form.html'
    success_message = "Experience was created successfully"

    def get(self, request, *args, **kwargs):
        form = ExperienceForms()
        formset = ExperienceDescriptionFormSet(queryset=ExperienceDescription.objects.none())
        return self.render_to_response({'form': form, 'formset': formset})

    def post(self, request, *args, **kwargs):
        form = ExperienceForms(data=self.request.POST)
        formset = ExperienceDescriptionFormSet(data=self.request.POST)
        if form.is_valid() and formset.is_valid():
            instance = form.save(commit=False)
            resume_id = self.kwargs['pk']
            instance.resume = Resume.objects.get(id=resume_id)
            instance.save()
            description_instances = formset.save(commit=False)
            for description_instance in description_instances:
                resume_id = self.kwargs['pk']
                description_instance.experience = Experience.objects.filter(resume_id=resume_id).last()
                description_instance.save()
            form.save()
            formset.save()
            if 'create_exp' in self.request.POST:
                return redirect(reverse_lazy('experiences:create_experience', kwargs={'pk': self.kwargs['pk']}))
            else:
                return redirect(reverse_lazy('skills:create_skill', kwargs={'pk': self.kwargs['pk']}))
        return self.render_to_response({'form': form, 'formset': formset})


class ExperienceUpdateView(LoginRequiredMixin, UpdateView):
    model = Experience
    template_name = 'experience_update.html'
    success_message = "Experience was updated successfully"

    def get(self, *args, **kwargs):
        formset = ExperienceFormSet(queryset=Experience.objects.filter(resume_id=self.kwargs['pk']))
        return self.render_to_response({'formset': formset})

    def post(self, request, *args, **kwargs):
        formset = ExperienceFormSet(data=self.request.POST)

        if formset.is_valid():
            if 'save' in self.request.POST:
                formset.save()
                messages.success(self.request, self.success_message)
                return redirect(reverse_lazy('resumes:resumes'))
            else:
                print(self.request.POST)
        return self.render_to_response({'formset': formset})


class ExperienceDescriptionUpdateView(LoginRequiredMixin, UpdateView):
    model = ExperienceDescription
    template_name = 'experience_description_update.html'
    success_message = "Experience description was updated successfully"

    def get(self, *args, **kwargs):
        formset = ExperienceDescriptionFormSet(queryset=ExperienceDescription.objects.filter(experience_id=self.kwargs['pk']))

        return self.render_to_response({'formset': formset})

    def post(self, request, *args, **kwargs):
        formset = ExperienceDescriptionFormSet(data=self.request.POST)

        if formset.is_valid():
            formset.save()
            messages.success(self.request, self.success_message)
            return redirect(reverse_lazy('resumes:resumes'))
        return self.render_to_response({'formset': formset})