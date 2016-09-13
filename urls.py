from django.conf.urls import url
from resume_machine import views

urlpatterns = [
    url(r'^$', views.api_document, name='resume_api'),
    url(r'^resume.pdf', views.get_resume_pdf, name='get_resume_pdf'),
    url(r'^resume.json', views.get_resume_json, name='get_resume_json'),
    url(r'^resume/$', views.resume_detail),
    url(r'^resumes/$', views.api_document),
    url(r'^resumes/basic/$', views.basic_detail),
    url(r'^resumes/profiles/$', views.profile_list),
    url(r'^resumes/profiles/(?P<username>\w+)/$', views.profile_list),
    url(r'^resumes/work/$', views.work_list),
    url(r'^resumes/work/(?P<username>\w+)/$', views.work_list),
    url(r'^resumes/work/(?P<username>\w+)/(?P<resume_name>\w+)/$', views.work_list),
    # url(r'^resumes/(?P<username>\w+)/(?P<resume_name>\w+)/work/(?P<date1>\d{4}-\d{2}-\d{2})/(?P<date2>\d{4}-\d{2}-\d{2})/$', views.work_list),
    # url(r'^resumes/(?P<username>\w+)/(?P<resume_name>\w+)/work/start_date/(?P<date1>\d{4}-\d{2}-\d{2})/$', views.work_list),
    url(r'^resumes/volunteer/$', views.volunteer_list),
    url(r'^resumes/volunteer/(?P<username>\w+)/$', views.volunteer_list),
    url(r'^resumes/volunteer/(?P<username>\w+)/(?P<resume_name>\w+)/$', views.volunteer_list),
    # url(r'^resumes/(?P<username>\w+)/(?P<resume_name>\w+)/volunteer/start_date/(?P<date1>\d{4}-\d{2}-\d{2})/$', views.volunteer_list),
    # url(r'^resumes/(?P<username>\w+)/(?P<resume_name>\w+)/volunteer/(?P<date1>\d{4}-\d{2}-\d{2})/(?P<date2>\d{4}-\d{2}-\d{2})/$', views.volunteer_list),
    url(r'^resumes/education/$', views.education_list),
    url(r'^resumes/education/(?P<username>\w+)/$', views.education_list),
    url(r'^resumes/education/(?P<username>\w+)/(?P<resume_name>\w+)/$', views.education_list),
    # url(r'^resumes/(?P<username>\w+)/(?P<resume_name>\w+)/education/(?P<date1>\d{4}-\d{2}-\d{2})/', views.education_list),
    url(r'^resumes/awards/$', views.awards_list),
    url(r'^resumes/awards/(?P<username>\w+)/$', views.awards_list),
    url(r'^resumes/awards/(?P<username>\w+)/(?P<resume_name>\w+)/$', views.awards_list),
    # url(r'^resumes/(?P<username>\w+)/(?P<resume_name>\w+)/awards/(?P<date>\d{4}-\d{2}-\d{2})/', views.awards_list),
    url(r'^resumes/publications/$', views.publications_list),
    url(r'^resumes/publications/(?P<username>\w+)/$', views.publications_list),
    url(r'^resumes/publications/(?P<username>\w+)/(?P<resume_name>\w+)/$', views.publications_list),
    # url(r'^resumes/(?P<username>\w+)/(?P<resume_name>\w+)/publications/(?P<date>\d{4}-\d{2}-\d{2})/', views.publications_list),
    url(r'^resumes/skills/$', views.skills_list),
    url(r'^resumes/skills/(?P<username>\w+)/$', views.skills_list),
    url(r'^resumes/skills/(?P<username>\w+)/(?P<resume_name>\w+)/$', views.skills_list),
    url(r'^resumes/languages/$', views.languages_list),
    url(r'^resumes/languages/(?P<username>\w+)/$', views.languages_list),
    url(r'^resumes/languages/(?P<username>\w+)/(?P<resume_name>\w+)/$', views.languages_list),
    url(r'^resumes/interests/$', views.interests_list),
    url(r'^resumes/interests/(?P<username>\w+)/$', views.interests_list),
    url(r'^resumes/interests/(?P<username>\w+)/(?P<resume_name>\w+)/$', views.interests_list),
    url(r'^resumes/references/$', views.references_list),
    url(r'^resumes/references/(?P<username>\w+)/$', views.references_list),
    url(r'^resumes/references/(?P<username>\w+)/(?P<resume_name>\w+)/$', views.references_list),
    # url(r'^resumes/search/(?P<username>\w+)/(?P<term>\w+)/', views.search),
    url(r'^resumes/(?P<username>\w+)/$', views.resume_detail),
    url(r'^resumes/(?P<username>\w+)/(?P<resume_name>\w+)/$', views.resume_detail),

]
