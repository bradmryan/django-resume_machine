from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse, Http404
from django.template.loader import get_template
from django.template import RequestContext
from django.views.decorators.http import require_GET
from resume_machine.models import Resume, User, Account
from django.conf import settings


import weasyprint

# Create your views here.
@require_GET
def get_resume_pdf(request):
    resume_name = request.GET.get('resume', settings.DEFAULT_RESUME)
    user = get_object_or_404(User, username=settings.DEFAULT_USER)
    resume = get_object_or_404(Resume, user=user, name=resume_name)

    context = {'user': user, 'resume':resume}

    if resume.resumeType == 'programmer':
        template = get_template('resume_machine/programmer.html')
    elif resume.resumeType == 'generic':
        template = get_template('resume_machine/general.html')
    else:
        raise Http404

    html = template.render(RequestContext(request, context))
    pdf = weasyprint.HTML(string=html).write_pdf()
    response = HttpResponse(pdf, content_type='application/pdf')
    return response


@require_GET
def api_document(request):
    current_site = get_current_site(request)
    default_user = settings.DEFAULT_USER
    default_resume = settings.DEFAULT_RESUME
    context = {
        'site' : current_site,
        'default_user' : default_user,
        'default_resume' : default_resume,
    }
    return render(request, 'resume_machine/api_doc.html', context)


@require_GET
def get_resume_json(request):
    resume = get_object_or_404(Account, user=User.objects.get(username=settings.DEFAULT_USER))
    return JsonResponse(resume.as_resume_json())


@require_GET
def resume_detail(request, username=settings.DEFAULT_USER, resume_name=settings.DEFAULT_RESUME):
    user = get_object_or_404(User, username=username)
    resume = Resume.objects.get(
        user=user,
        name=resume_name,
        )
    return JsonResponse(resume.as_json())


@require_GET
def basic_detail(request, username=settings.DEFAULT_USER, resume_name=settings.DEFAULT_RESUME):
    user = get_object_or_404(User, username=username)
    resume = Resume.objects.get(
        user=user,
        name=resume_name,
        )
    return JsonResponse(resume.basic_as_json())


@require_GET
def profile_list(request, username=settings.DEFAULT_USER):
    account = get_object_or_404(
        Account,
        user=User.objects.get(username=username)
        )
    return JsonResponse({'profiles' : account.profiles_as_json()})


@require_GET
def work_list(request, username=settings.DEFAULT_USER, resume_name=settings.DEFAULT_RESUME):
    user = get_object_or_404(User, username=username)
    resume = Resume.objects.get(
        user=user,
        name=resume_name,
        )
    return JsonResponse({'work' : resume.work_as_json()})


@require_GET
def volunteer_list(request, username=settings.DEFAULT_USER, resume_name=settings.DEFAULT_RESUME):
    user = get_object_or_404(User, username=username)
    resume = Resume.objects.get(
        user=user,
        name=resume_name,
        )
    return JsonResponse({'volunteer' : resume.volunteer_as_json()})


@require_GET
def education_list(request, username=settings.DEFAULT_USER, resume_name=settings.DEFAULT_RESUME):
    user = get_object_or_404(User, username=username)
    resume = Resume.objects.get(
        user=user,
        name=resume_name,
        )
    return JsonResponse({'education' : resume.education_as_json()})


@require_GET
def awards_list(request, username=settings.DEFAULT_USER, resume_name=settings.DEFAULT_RESUME):
    user = get_object_or_404(User, username=username)
    resume = Resume.objects.get(
        user=user,
        name=resume_name,
        )
    return JsonResponse({'awards' : resume.awards_as_json()})


@require_GET
def publications_list(request, username=settings.DEFAULT_USER, resume_name=settings.DEFAULT_RESUME):
    user = get_object_or_404(User, username=username)
    resume = Resume.objects.get(
        user=user,
        name=resume_name,
        )
    return JsonResponse({'publications' : resume.publications_as_json()})


@require_GET
def skills_list(request, username=settings.DEFAULT_USER, resume_name=settings.DEFAULT_RESUME):
    user = get_object_or_404(User, username=username)
    resume = Resume.objects.get(
        user=user,
        name=resume_name,
        )
    return JsonResponse({'skills' : resume.skills_as_json()})


@require_GET
def languages_list(request, username=settings.DEFAULT_USER, resume_name=settings.DEFAULT_RESUME):
    user = get_object_or_404(User, username=username)
    resume = Resume.objects.get(
        user=user,
        name=resume_name,
        )
    return JsonResponse({'languages' : resume.languages_as_json()})


@require_GET
def interests_list(request, username=settings.DEFAULT_USER, resume_name=settings.DEFAULT_RESUME):
    user = get_object_or_404(User, username=username)
    resume = Resume.objects.get(
        user=user,
        name=resume_name,
        )
    return JsonResponse({'interests' : resume.interests_as_json()})


@require_GET
def references_list(request, username=settings.DEFAULT_USER, resume_name=settings.DEFAULT_RESUME):
    user = get_object_or_404(User, username=username)
    account = Account.objects.get(user=user)
    if account.publishReferences:
        resume = Resume.objects.get(
            user=user,
            name=resume_name,
            )
        return JsonResponse({'references' : resume.references_as_json()})
    else:
        return JsonResponse({'References Not Published' : 'References are available only by request'})


# @require_GET
# def search(request, username, term):
#     user = get_object_or_404(User, username=username)
#     return JsonResponse({'None': None})
