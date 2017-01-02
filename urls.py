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
    url(r'^account/$', views.account_form, name='account_form'),
    url(r'^account/update_name/$', views.update_name, name='update_name'),
    url(r'^account/update_label/$', views.update_label, name='update_label'),
    url(r'^account/update_summary/$', views.update_summary, name='update_summary'),
    url(r'^account/update_website/$', views.update_website, name='update_website'),
    url(r'^account/update_phone/$', views.update_phone, name='update_phone'),
    url(r'^account/update_address/$', views.update_address, name='update_address'),
    url(r'^account/update_location/$', views.update_location, name='update_location')
    #url(r'^$', views.resume_showcase, name='resume_showcase'),
]
