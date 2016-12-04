from django.conf.urls import url
from resume_machine import views

urlpatterns = [
    url(r'^$', views.api_document, name='resume_api'),
    url(r'^resume.pdf', views.get_resume_pdf, name='get_resume_pdf'),
    url(r'^resume.json', views.get_resume_json, name='get_resume_json'),
    url(r'^resume/$', views.resume_detail),
    url(r'^resume/basic/$', views.basic_detail),
    url(r'^resume/profiles/$', views.profile_list),
    url(r'^resume/work/$', views.work_list),
    url(r'^resume/volunteer/$', views.volunteer_list),
    url(r'^resume/education/$', views.education_list),
    url(r'^resume/awards/$', views.awards_list),
    url(r'^resume/publications/$', views.publications_list),
    url(r'^resume/skills/$', views.skills_list),
    url(r'^resume/languages/$', views.languages_list),
    url(r'^resume/interests/$', views.interests_list),
    url(r'^resume/references/$', views.references_list),
]
