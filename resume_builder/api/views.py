from django.shortcuts import render, get_object_or_404
from .forms import CreateResume
from .models import Resume, School, Experience, Skill, Hobby
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa


def home(request):
    return render(request, 'api/home.html', {})


def resume(request):
    if request.method == 'POST':
        form = CreateResume(request.POST)

        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            email = form.cleaned_data["email"]
            phone = form.cleaned_data["phone"]
            lin = form.cleaned_data["lin"]
            hobby = form.cleaned_data["hobby"]
            skill = form.cleaned_data["skill"]
            skill_level = form.cleaned_data["skill_level"]
            school = form.cleaned_data["school"]
            school_city = form.cleaned_data["school_city"]
            degree = form.cleaned_data["degree"]
            field_study = form.cleaned_data["field_study"]
            start_date_study = form.cleaned_data["start_date_study"]
            end_date_study = form.cleaned_data["end_date_study"]
            description = form.cleaned_data["description"]
            company = form.cleaned_data["company"]
            exp_city = form.cleaned_data["exp_city"]
            position = form.cleaned_data["position"]
            start_date_exp = form.cleaned_data["start_date_exp"]
            end_date_exp = form.cleaned_data["end_date_exp"]
            description_exp = form.cleaned_data["description_exp"]
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
        form = CreateResume()
    return render(request, 'api/resume.html', {"form":form})


def view(request):
    return render(request, 'api/view.html', {})


def detail(request, resume_id):
    resume = get_object_or_404(Resume, pk=resume_id)
    school = get_object_or_404(School, pk=resume_id)
    experience = get_object_or_404(Experience, pk=resume_id)
    hobby = get_object_or_404(Hobby, pk=resume_id)
    skill = get_object_or_404(Skill, pk=resume_id)
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



