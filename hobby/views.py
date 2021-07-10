from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView
from django.contrib.auth.decorators import login_required
from .models import Hobby
from .forms import HobbyFormSet


@login_required(login_url='users:login')
class HobbyListView(ListView):
    model = Hobby
    template_name = 'hobby_list.html'


@login_required(login_url='users:login')
class HobbyAddView(TemplateView):
    template_name = 'add_hobby.html'

    def get(self, *args, **kwargs):
        formset = HobbyFormSet(queryset=Hobby.objects.none())
        return self.render_to_response({'hobby_formset': formset})

    def post(self, *args, **kwargs):
        formset = HobbyFormSet(data=self.request.POST)

        if formset.is_valid():
            formset.save()
            return redirect(reverse_lazy('hobby:hobbies_list'))

        return self.render_to_response({'hobby_formset': formset})