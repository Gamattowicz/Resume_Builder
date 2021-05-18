from django.shortcuts import render, get_object_or_404
from .forms import ResumeForms, SchoolForms, ExperienceForms, SkillForms, HobbyForms
from .models import Resume, School, Experience, Skill, Hobby
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa


def home(request):
    return render(request, 'api/home.html', {})


def resume(request):
    if request.method == 'POST':
        resume_form = ResumeForms(request.POST)
        school_form = SchoolForms(request.POST)
        exp_form = ExperienceForms(request.POST)
        skill_form = SkillForms(request.POST)
        hobby_form = HobbyForms(request.POST)

        if resume_form.is_valid() and school_form.is_valid() and exp_form.is_valid() and skill_form.is_valid() and \
           hobby_form.is_valid():
            first_name = resume_form.cleaned_data["first_name"]
            last_name = resume_form.cleaned_data["last_name"]
            email = resume_form.cleaned_data["email"]
            phone = resume_form.cleaned_data["phone"]
            lin = resume_form.cleaned_data["lin"]
            description = resume_form.cleaned_data["description"]
            hobby = hobby_form.cleaned_data["hobby"]
            skill = skill_form.cleaned_data["skill"]
            skill_level = skill_form.cleaned_data["skill_level"]
            school = school_form.cleaned_data["school"]
            school_city = school_form.cleaned_data["school_city"]
            degree = school_form.cleaned_data["degree"]
            field_study = school_form.cleaned_data["field_study"]
            start_date_study = school_form.cleaned_data["start_date_study"]
            end_date_study = school_form.cleaned_data["end_date_study"]
            company = exp_form.cleaned_data["company"]
            exp_city = exp_form.cleaned_data["exp_city"]
            position = exp_form.cleaned_data["position"]
            start_date_exp = exp_form.cleaned_data["start_date_exp"]
            end_date_exp = exp_form.cleaned_data["end_date_exp"]
            description_exp = exp_form.cleaned_data["description_exp"]
            r = Resume(first_name=first_name, last_name=last_name, email=email, phone=phone, lin=lin, description=description)
            r.save()
            request.user.resume.add(r)

            e = Experience(resume=r, company=company, city=exp_city, position=position, start_date=start_date_exp, end_date=end_date_exp,
                           description=description_exp)
            e.save()

            s = School(resume=r, name=school, city=school_city, degree=degree, field_study=field_study, start_date=start_date_study,
                       end_date=end_date_study,)
            s.save()

            sk = Skill(resume=r, name=skill, level=skill_level)
            sk.save()

            h = Hobby(resume=r, name=hobby)
            h.save()

    else:
        resume_form = ResumeForms()
        school_form = SchoolForms()
        exp_form = ExperienceForms()
        skill_form = SkillForms()
        hobby_form = HobbyForms()
    return render(request, 'api/resume.html', {"resume_form": resume_form, 'school_form': school_form, 'exp_form': exp_form,
                                               'skill_form': skill_form, 'hobby_form': hobby_form})


def view(request):
    return render(request, 'api/view.html', {})


def detail(request, resume_id):
    resume = get_object_or_404(Resume, pk=resume_id)
    school = get_object_or_404(School, resume=resume_id)
    experience = get_object_or_404(Experience, resume=resume_id)
    hobby = get_object_or_404(Hobby, resume=resume_id)
    skill = get_object_or_404(Skill, resume=resume_id)
    return render(request, 'api/detail.html', {'resume': resume, 'school': school, 'experience': experience,
                                               'hobby': hobby, 'skill': skill})


def resume_render_pdf_view(request, *args, **kwargs):
    pk = kwargs.get('pk')
    resume = get_object_or_404(Resume, pk=pk)

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



