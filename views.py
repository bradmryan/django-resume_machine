from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse, Http404
from django.template.loader import get_template
from django.template import RequestContext
from django.views.decorators.http import require_GET, require_POST
from django.contrib.auth.decorators import login_required
from resume_machine.models import Resume, Account, Profile, Skill, Award, Publication, Interest, Language, Reference
from django.contrib.sites.models import Site


import feedparser
import weasyprint

# Create your views here.
@login_required
def update_account_form(request):
    account = get_object_or_404(
        Account,
        user=request.user
    )
    resumes = Resume.objects.filter(user=request.user)
    languages = Language.objects.filter(user=request.user)
    references = Reference.objects.filter(user=request.user)
    context = {
        'account' : account,
        'resumes' : resumes,
        'languages' : languages,
        'references' : references
    }
    return render(request, 'resume_machine/update_account_form.html', context)

@login_required
def resume_create(request):
    account = get_object_or_404(
        Account,
        user=request.user
    )
    context = { 'account' : account }
    return render(request, 'resume_machine/resume_form.html', context)


@login_required
def update_profile_form(request):
    network_list = []
    profiles = Profile.objects.filter(user=request.user)
    for profile in profiles:
        network_list.append(profile.network)
    context = { 'profiles' : profiles, 'networks' : network_list }
    return render(request, 'resume_machine/update_profile_form.html', context)


@login_required
def update_work_form(request, resume_pk=None):
    if resume_pk:
        resume = get_object_or_404(
            Resume,
            pk=resume_pk,
            user=request.user
        )
        work_history = resume.work.all()
    else:
        account = get_object_or_404(
            Account,
            user=request.user
        )
        work_history = account.defaultResume.work.all()
    context = { 'jobs' : work_history }
    return render(request, 'resume_machine/update_work_form.html', context)


@login_required
def update_education_form(request, resume_pk=None):
    account = get_object_or_404(
        Account,
        user=request.user
    )
    context = { 'education' : account.defaultResume.education.all() }
    return render(request, 'resume_machine/update_education_form.html', context)


@login_required
def update_skills_form(request):
    skills = Skill.objects.filter(user=request.user)
    context = { 'skills' : skills }
    return render(request, 'resume_machine/update_skills_form.html', context)


@login_required
def update_awards_form(request):
    awards = Award.objects.filter(user=request.user)
    context = { 'awards' : awards }
    return render(request, 'resume_machine/update_awards_form.html', context)


@login_required
def update_publications_form(request):
    publications = Publication.objects.filter(user=request.user)
    context = { 'publications' : publications }
    return render(request, 'resume_machine/update_publications_form.html', context)


@login_required
def update_interests_form(request):
    interests = Interest.objects.filter(user=request.user)
    context = { 'interests' : interests }
    return render(request, 'resume_machine/update_interests_form.html', context)


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
def create_profile(request):
    data = {}
    try:
        username = request.POST.get('username', '')
        network = request.POST.get('network', '')
        url = ""

        if network == "TW":
            url = "https://twitter.com/" + username
        elif network == "FB":
            url = "https://www.facebook.com/" + username
        elif network == "LI":
            url = "https://ca.linkedin.com/in/" + username
        elif network == "GH":
            url = "https://github.com/" + username

        profile = Profile(
            user = request.user,
            network = network,
            username = username,
            url = url
        )
        profile.save()
        data = { 'success' : True, 'url' : profile.url , 'pk' : profile.pk }
    except:
        pass
    return JsonResponse(data)


@require_POST
def create_language(request):
    data = {}
    try:
        name = request.POST.get('name', '')
        level = request.POST.get('level', '')
        if name and level:
            language = Language(
                user = request.user,
                name = name,
                level = level
            )
            language.save()
            data = { 'success' : True, 'language_pk' : language.pk }
        else:
            data = { 'success' : False }
    except:
        pass
    return JsonResponse(data)


@require_POST
def create_reference(request):
    data = {}
    try:
        name = request.POST.get('name', '')
        description = request.POST.get('description', '')
        if name and description:
            reference = Reference(
                user = request.user,
                name = name,
                reference = description
            )
            reference.save()
            data = { 'success' : True, 'reference_pk' : reference.pk }
        else:
            data = { 'success' : False }
    except:
        pass
    return JsonResponse(data)


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


@require_POST
def update_profile(request, profile_id):
    data = {}
    try:
        account = get_object_or_404(Account, user=request.user)
        profile = get_object_or_404(Profile, pk=profile_id)
        if profile in account.defaultResume.profiles.all():
            username = request.POST.get('username', '')
            profile.username = username
            if profile.network == "TW":
                profile.url = "https://twitter.com/" + username
            elif profile.network == "FB":
                profile.url = "https://www.facebook.com/" + username
            elif profile.network == "LI":
                profile.url = "https://ca.linkedin.com/in/" + username
            elif profile.network == "GH":
                profile.url = "https://github.com/" + username
            profile.save(update_fields=['username', 'url'])
            data = { 'success' : True, 'url' : profile.url }
    except:
        pass
    return JsonResponse(data)


@require_POST
def update_language(request, language_pk):
    data = {}
    try:
        language = get_object_or_404(Language, pk=language_pk, user=request.user)
        name = request.POST.get('name', '')
        level = request.POST.get('level', '')
        language.name = name
        language.level = level
        language.save(update_fields=['name', 'level'])
        data = { 'success': True }
    except:
        pass
    return JsonResponse(data)


@require_POST
def update_reference(request, reference_pk):
    data = {}
    try:
        reference = get_object_or_404(Reference, pk=reference_pk, user=request.user)
        name = request.POST.get('name', '')
        description = request.POST.get('description', '')
        reference.name = name
        reference.reference = description
        reference.save(update_fields=['name', 'reference'])
        data = { 'success': True }
    except:
        pass
    return JsonResponse(data)


@require_POST
def delete_profile(request, profile_pk):
    data = {}
    try:
        profile = get_object_or_404(Profile, pk=profile_pk, user=request.user)
        network_name = profile.get_network_display()
        count = profile.delete()
        data = { 'success': True, 'count' : count, 'profile_pk' : profile_pk, 'network_name' : network_name }
    except:
        pass
    return JsonResponse(data)


@require_POST
def delete_language(request, language_pk):
    data = {}
    try:
        language = get_object_or_404(Language, pk=language_pk, user=request.user)
        count = language.delete()
        data = { 'success': True, 'count' : count, 'language_pk' : language_pk }
    except:
        pass
    return JsonResponse(data)


@require_POST
def delete_reference(request, reference_pk):
    data = {}
    try:
        reference = get_object_or_404(Reference, pk=reference_pk, user=request.user)
        count = reference.delete()
        data = { 'success': True, 'count' : count, 'reference_pk' : reference_pk }
    except:
        pass
    return JsonResponse(data)
