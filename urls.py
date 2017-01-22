from django.conf.urls import url
from resume_machine import views

urlpatterns = [
    url(r'^$', views.resume_html, name='resume_showcase'),
    url(r'^api/$', views.api_document, name='resume_api'),
    url(r'^pdf/$', views.get_resume_pdf, name='get_resume_pdf'),
    url(r'^json/$', views.get_resume_json, name='get_resume_json'),
    url(r'^html/$', views.resume_html, name='resume_html'),
    url(r'^works/$', views.works, name='works'),
    url(r'^api/resume/$', views.resume_detail),
    url(r'^api/basic/$', views.basic_detail),
    url(r'^api/profiles/$', views.profile_list),
    url(r'^api/work/$', views.work_list),
    url(r'^api/volunteer/$', views.volunteer_list),
    url(r'^api/education/$', views.education_list),
    url(r'^api/awards/$', views.awards_list),
    url(r'^api/publications/$', views.publications_list),
    url(r'^api/skills/$', views.skills_list),
    url(r'^api/languages/$', views.languages_list),
    url(r'^api/interests/$', views.interests_list),
    url(r'^api/references/$', views.references_list),
    url(r'^job_search/$', views.job_search, name='job_search'),
    url(r'^create/profile/$', views.create_profile, name='create_profile'),
    url(r'^create/language/$', views.create_language, name='create_language'),
    url(r'^create/reference/$', views.create_reference, name='create_reference'),
    url(r'^update/account/form/$', views.update_account_form, name='update_account_form'),
    url(r'^update/account/name/$', views.update_name, name='update_name'),
    url(r'^update/account/label/$', views.update_label, name='update_label'),
    url(r'^update/account/summary/$', views.update_summary, name='update_summary'),
    url(r'^update/account/website/$', views.update_website, name='update_website'),
    url(r'^update/account/phone/$', views.update_phone, name='update_phone'),
    url(r'^update/account/address/$', views.update_address, name='update_address'),
    url(r'^update/account/location/$', views.update_location, name='update_location'),
    url(r'^update/account/publishreferences/$', views.update_publishreferences, name='update_publishreferences'),
    url(r'^update/account/defaultresume/$', views.update_defaultresume, name='update_defaultresume'),
    url(r'^update/language/(?P<language_pk>[0-9]+)/$', views.update_language, name='update_language'),
    url(r'^update/reference/(?P<reference_pk>[0-9]+)/$', views.update_reference, name='update_reference'),
    url(r'^update/profile/form/$', views.update_profile_form, name='update_profile_form'),
    url(r'^update/profile/(?P<profile_id>[0-9]+)/$', views.update_profile, name='update_profile'),
    url(r'^update/work/form/$', views.update_work_form, name='update_work_form'),
    url(r'^update/skills/form/$', views.update_skills_form, name='update_skills_form'),
    url(r'^update/awards/form/$', views.update_awards_form, name='update_awards_form'),
    url(r'^update/education/form/$', views.update_education_form, name='update_education_form'),
    url(r'^update/publications/form/$', views.update_publications_form, name='update_publications_form'),
    url(r'^update/interests/form/$', views.update_interests_form, name='update_interests_form'),
    url(r'^delete/profile/(?P<profile_pk>[0-9]+)/$', views.delete_profile, name='delete_profile'),
    url(r'^delete/language/(?P<language_pk>[0-9]+)/$', views.delete_language, name='delete_language'),
    url(r'^delete/reference/(?P<reference_pk>[0-9]+)/$', views.delete_reference, name='delete_reference'),

    #url(r'^$', views.resume_showcase, name='resume_showcase'),
]
