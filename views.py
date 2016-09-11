from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.template.loader import get_template
from django.template import RequestContext
from django.views.decorators.http import require_GET
from resume_machine.models import Resume, User
from app.settings import DEFAULT_RESUME

import weasyprint

# Create your views here.
@require_GET
def get_resume_pdf(request):
    user = get_object_or_404(User, username=DEFAULT_RESUME)
    resume = Resume.objects.get(
        user=user,
        resumeType='programmer'
        )
    context = {'user': user, 'resume':resume}

    if resume.resumeType == 'programmer':
        template = get_template('resume_machine/programmer.html')
    else:
        template = get_template('resume_machine/general.html')

    html = template.render(RequestContext(request, context))
    pdf = weasyprint.HTML(string=html).write_pdf()
    response = HttpResponse(pdf, content_type='application/pdf')
    return response

@require_GET
def get_resume_json(request):
    user = get_object_or_404(User, username=DEFAULT_RESUME)
    resume = Resume.objects.get(
        user=user,
        resumeType='programmer'
        )
    return JsonResponse(resume.as_json())
