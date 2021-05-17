from django.shortcuts import render, get_object_or_404
from .forms import CreateResume
from .models import Resume
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
            skills = form.cleaned_data["skills"]
            school = form.cleaned_data["school"]
            school_city = form.cleaned_data["school_city"]
            degree = form.cleaned_data["degree"]
            field_study = form.cleaned_data["field_study"]
            start_date = form.cleaned_data["start_date"]
            end_date = form.cleaned_data["school_cityend_date"]
            r = Resume(first_name=first_name, last_name=last_name, email=email, phone=phone, lin=lin, hobby=hobby, skills=skills,
                       school=school, school_city=school_city, degree=degree, field_study=field_study, start_date=start_date, end_date=end_date)
            r.save()
            request.user.resume.add(r)

    else:
        form = CreateResume()
    return render(request, 'api/resume.html', {"form":form})


def view(request):
    return render(request, 'api/view.html', {})


def detail(request, resume_id):
    resume = get_object_or_404(Resume, pk=resume_id)
    return render(request, 'api/detail.html', {'resume': resume})


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



