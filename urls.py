from django.conf.urls import url
from resume_machine import views

urlpatterns = [
    url(r'^resume.pdf', views.get_resume_pdf),
    url(r'^resume.json', views.get_resume_json),
]
