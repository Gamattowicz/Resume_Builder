from django.shortcuts import render, get_object_or_404
from .forms import ResumeForms
from hobby.forms import HobbyFormSet
from personals.models import Personal
from skills.models import Skill
from hobby.models import Hobby
from schools.models import School
from experiences.models import Experience
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa


def home(request):
    return render(request, 'api/home.html', {})


def resume(request):
    if request.method == 'POST':
        resume_form = ResumeForms(request.POST)
        hobby_formset = HobbyFormSet(data=request.POST)

        if resume_form.is_valid() and hobby_formset.is_valid():
            first_name = resume_form.cleaned_data["first_name"]
            last_name = resume_form.cleaned_data["last_name"]
            email = resume_form.cleaned_data["email"]
            phone = resume_form.cleaned_data["phone"]
            lin = resume_form.cleaned_data["lin"]
            description = resume_form.cleaned_data["description"]
            # skill = skill_form.cleaned_data["skill"]
            # skill_level = skill_form.cleaned_data["skill_level"]
            # school = school_form.cleaned_data["school"]
            # school_city = school_form.cleaned_data["school_city"]
            # degree = school_form.cleaned_data["degree"]
            # field_study = school_form.cleaned_data["field_study"]
            # start_date_study = school_form.cleaned_data["start_date_study"]
            # end_date_study = school_form.cleaned_data["end_date_study"]
            # company = exp_form.cleaned_data["company"]
            # exp_city = exp_form.cleaned_data["exp_city"]
            # position = exp_form.cleaned_data["position"]
            # start_date_exp = exp_form.cleaned_data["start_date_exp"]
            # end_date_exp = exp_form.cleaned_data["end_date_exp"]
            # description_exp = exp_form.cleaned_data["description_exp"]
            r = Personal(first_name=first_name, last_name=last_name, email=email, phone=phone, lin=lin, description=description)
            r.save()
            hobby_formset.resume_id = r.pk
            request.user.resume.add(r)
            hobby_formset.save()

    else:
        resume_form = ResumeForms()
        hobby_formset = HobbyFormSet(queryset=Hobby.objects.none())
    return render(request, 'api/resume.html', {"resume_form": resume_form, "hobby_formset": hobby_formset})


def view(request):
    return render(request, 'api/view.html', {})


def detail(request, resume_id):
    resume = get_object_or_404(Personal, pk=resume_id)
    school = get_object_or_404(School, resume=resume_id)
    experience = get_object_or_404(Experience, resume=resume_id)
    hobby = get_object_or_404(Hobby, resume=resume_id)
    skill = get_object_or_404(Skill, resume=resume_id)
    return render(request, 'api/detail.html', {'resume': resume, 'school': school, 'experience': experience,
                                               'hobby': hobby, 'skill': skill})


def resume_render_pdf_view(request, *args, **kwargs):
    pk = kwargs.get('pk')
    resume = get_object_or_404(Personal, pk=pk)

    template_path = 'api/detail.html'
    context = {'resume': resume}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    # if download:
    # response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # if display:
    response['Content-Disposition'] = 'filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response
