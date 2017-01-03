from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse, Http404
from django.template.loader import get_template
from django.template import RequestContext
from django.views.decorators.http import require_GET, require_POST
from django.contrib.auth.decorators import login_required
from resume_machine.models import Resume, Account
from django.contrib.sites.models import Site


import feedparser
import weasyprint

# Create your views here.
@login_required
def account_form(request):
    account = get_object_or_404(
        Account,
        user=request.user
    )
    resumes = Resume.objects.filter(user=account.user)
    context = {
        'account' : account,
        'resumes' : resumes
    }
    return render(request, 'resume_machine/account_form.html', context)

@require_GET
def works(request):
    context = {}
    return render(request, 'resume_machine/works.html', context)

@require_GET
def resume_html(request):
    account = get_object_or_404(
        Account,
        site=Site.objects.get(id=1)
    )
    context = {
        'user': account.user,
        'resume':account.defaultResume
    }
    return render(request, 'resume_machine/resume.html', context)


@require_GET
def get_resume_pdf(request):
    account = get_object_or_404(
        Account,
        site=Site.objects.get(id=1)
    )
    context = {'user': account.user, 'resume':account.defaultResume}

    if account.defaultResume.resumeType == 'programmer':
        template = get_template('resume_machine/programmer.html')
    else:
        raise Http404

    html = template.render(RequestContext(request, context))
    pdf = weasyprint.HTML(string=html).write_pdf()
    response = HttpResponse(pdf, content_type='application/pdf')
    return response


@require_GET
def api_document(request):
    current_site = get_current_site(request)
    context = {
        'site' : current_site,
    }
    return render(request, 'resume_machine/api_doc.html', context)


@login_required
def job_search(request):
    context = {}
    feed = feedparser.parse('https://weworkremotely.com/categories/2-programming/jobs.rss')
    context['feed'] = feed
    return render(request, 'resume_machine/job_search.html', context)


@require_GET
def get_resume_json(request):
    resume = get_object_or_404(
        Account,
        site=Site.objects.get(id=1)
    )
    return JsonResponse(resume.as_resume_json())


@require_GET
def resume_detail(request):
    account = get_object_or_404(
        Account,
        site=Site.objects.get(id=1)
    )
    return JsonResponse(account.defaultResume.as_json())


@require_GET
def basic_detail(request):
    account = get_object_or_404(
        Account,
        site=Site.objects.get(id=1)
    )
    return JsonResponse(account.defaultResume.basic_as_json())


@require_GET
def profile_list(request):
    account = get_object_or_404(
        Account,
        site=Site.objects.get(id=1)
    )
    return JsonResponse({'profiles' : account.profiles_as_json()})


@require_GET
def work_list(request):
    account = get_object_or_404(
        Account,
        site=Site.objects.get(id=1)
    )

    return JsonResponse({'work' : account.defaultResume.work_as_json()})


@require_GET
def volunteer_list(request):
    account = get_object_or_404(
        Account,
        site=Site.objects.get(id=1)
    )
    return JsonResponse({'volunteer' : account.defaultResume.volunteer_as_json()})


@require_GET
def education_list(request):
    account = get_object_or_404(
        Account,
        site=Site.objects.get(id=1)
    )
    return JsonResponse({'education' : account.defaultResume.education_as_json()})


@require_GET
def awards_list(request):
    account = get_object_or_404(
        Account,
        site=Site.objects.get(id=1)
    )
    return JsonResponse({'awards' : account.defaultResume.awards_as_json()})


@require_GET
def publications_list(request):
    account = get_object_or_404(
        Account,
        site=Site.objects.get(id=1)
    )
    return JsonResponse({'publications' : account.defaultResume.publications_as_json()})


@require_GET
def skills_list(request):
    account = get_object_or_404(
        Account,
        site=Site.objects.get(id=1)
    )
    return JsonResponse({'skills' : account.defaultResume.skills_as_json()})


@require_GET
def languages_list(request):
    account = get_object_or_404(
        Account,
        site=Site.objects.get(id=1)
    )
    return JsonResponse({'languages' : account.defaultResume.languages_as_json()})


@require_GET
def interests_list(request):
    account = get_object_or_404(
        Account,
        site=Site.objects.get(id=1)
    )
    return JsonResponse({'interests' : account.defaultResume.interests_as_json()})


@require_GET
def references_list(request):
    account = get_object_or_404(
        Account,
        site=Site.objects.get(id=1)
    )
    if account.publishReferences:
        return JsonResponse({'references' : account.defaultResume.references_as_json()})
    else:
        return JsonResponse({'error' : 'References Not Published'})


# @require_GET
# def search(request, username, term):
#     user = get_object_or_404(User, username=username)
#     return JsonResponse({'None': None})


@require_POST
def update_name(request):
    data = { ' message' : 'fail' }
    try:
        account = get_object_or_404(Account, user=request.user)
        firstname = request.POST.get('first_name', '')
        middleinitial = request.POST.get('middle_initial', '')
        lastname = request.POST.get('last_name', '')
        account.firstname = firstname
        account.middleinitial = middleinitial
        account.lastname = lastname
        account.save(update_fields=['firstname', 'middleinitial', 'lastname'])
        data = { 'message' : 'Name changed', 'success': True }
    except:
        pass
    return JsonResponse(data)


@require_POST
def update_label(request):
    data = {}
    try:
        account = get_object_or_404(Account, user=request.user)
        label = request.POST.get('label', '')
        account.label = label.title();
        account.save(update_fields=['label'])
        data = { 'success': True }
    except:
        pass
    return JsonResponse(data)


@require_POST
def update_summary(request):
    data = {}
    try:
        account = get_object_or_404(Account, user=request.user)
        summary = request.POST.get('summary', '')
        account.summary = summary;
        account.save(update_fields=['summary'])
        data = { 'success': True }
    except:
        pass
    return JsonResponse(data)


@require_POST
def update_website(request):
    data = {}
    try:
        account = get_object_or_404(Account, user=request.user)
        website = request.POST.get('website', '')
        account.website = website;
        account.save(update_fields=['website'])
        data = { 'success': True }
    except:
        pass
    return JsonResponse(data)


@require_POST
def update_phone(request):
    data = {}
    try:
        account = get_object_or_404(Account, user=request.user)
        phone = request.POST.get('phone', '')
        account.phone = phone;
        account.save(update_fields=['phone'])
        data = { 'success': True }
    except:
        pass
    return JsonResponse(data)


@require_POST
def update_address(request):
    data = {}
    try:
        account = get_object_or_404(Account, user=request.user)
        address = request.POST.get('address', '')
        account.address = address;
        account.save(update_fields=['address'])
        data = { 'success': True }
    except:
        pass
    return JsonResponse(data)


@require_POST
def update_location(request):
    data = {}
    try:
        account = get_object_or_404(Account, user=request.user)
        postalcode = request.POST.get('postalcode', '')
        city = request.POST.get('city', '')
        country = request.POST.get('country', '')
        region = request.POST.get('region', '')
        account.postalcode = postalcode;
        account.city = city;
        account.countrycode = country;
        account.region = region;
        account.save(update_fields=['postalcode', 'city', 'countrycode', 'region'])
        data = { 'success': True }
    except:
        pass
    return JsonResponse(data)


@require_POST
def update_publishreferences(request):
    data = {}
    try:
        account = get_object_or_404(Account, user=request.user)
        publishReferences = request.POST.get('publishReferences', '')
        if publishReferences.lower() == 'true':
            account.publishReferences = True
        elif publishReferences.lower() == 'false':
            account.publishReferences = False
        account.save(update_fields=['publishReferences'])
        data = { 'success': True }
    except:
        pass
    return JsonResponse(data)


@require_POST
def update_defaultresume(request):
    data = {}
    try:
        account = get_object_or_404(Account, user=request.user)
        defaultResume = request.POST.get('defaultResume', '')
        account.defaultResume = get_object_or_404(Resume, pk=defaultResume)
        account.save(update_fields=['defaultResume'])
        data = { 'success': True }
    except:
        pass
    return JsonResponse(data)
