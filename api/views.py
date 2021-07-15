from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from personals.models import Personal
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa


def home(request):
    return render(request, 'api/home.html', {})


@login_required()
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
