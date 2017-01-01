from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.contrib.sites.models import Site

# Create your models here.
class Image(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=50, unique=True)
    image = models.URLField()
    alt_image = models.URLField(null=True, blank=True)
    attribution = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Account(models.Model):
    user = models.OneToOneField(User)
    site = models.OneToOneField(Site)
    firstname = models.CharField(max_length=255)
    middleinitial = models.CharField(max_length=5)
    lastname = models.CharField(max_length=255)
    label = models.CharField(max_length=255)
    picture = models.ForeignKey(Image, null=True)
    phone = models.CharField(max_length=14)
    website = models.URLField()
    summary = models.TextField()
    address = models.CharField(max_length=255, null=True)
    postalcode = models.CharField(max_length=9, null=True)
    city = models.CharField(max_length=255, null=True)
    countrycode = models.CharField(max_length=2, null=True)
    region = models.CharField(max_length=255, null=True)
    publishReferences = models.BooleanField(default=False)

    def __str__(self):
        return self.user.email

    def get_full_name(self):
        return ' '.join([self.firstname, self.middleinitial, self.lastname]).title()

    def location_as_json(self):
        return {
            "address" : self.address,
            "postalCode" : self.postalcode,
            "city" : self.city,
            "countryCode" : self.countrycode,
            "region" : self.region,
        }

    def profiles_as_json(self):
        profiles_list = []
        for profile in Profile.objects.filter(user=self.user):
            profiles_list.append(profile.as_json())
        return profiles_list


    def as_json(self):
        return {
            "name" : self.get_full_name(),
            "label" : self.label,
            "picture" : self.picture.image,
            "email" : self.user.email,
            "phone" : self.phone,
            "website" : self.website,
            "summary" : self. summary,
            "location" : self.location_as_json(),
            "profiles" : self.profiles_as_json(),
        }

    def as_resume_json(self):
        resume_dict = {}
        work_list = []
        volunteer_list = []
        education_list = []
        awards_list = []
        publications_list = []
        skills_list = []
        language_list = []
        interests_list = []
        references_list = []

        for work in Work.objects.filter(user=self.user):
            if work.volunteer:
                volunteer_list.append(work.as_json())
            else:
                work_list.append(work.as_json())

        for education in Education.objects.filter(user=self.user):
            education_list.append(education.as_json())

        for award in Award.objects.filter(user=self.user):
            awards_list.append(award.as_json())

        for publication in Publication.objects.filter(user=self.user):
            publications_list.append(publication.as_json())

        for skill in Skill.objects.filter(user=self.user):
            skills_list.append(skill.as_json())

        for language in Language.objects.filter(user=self.user):
            language_list.append(language.as_json())

        for interest in Interest.objects.filter(user=self.user):
            interests_list.append(interest.as_json())

        for reference in Reference.objects.filter(user=self.user):
            references_list.append(reference.as_json())

        return {
            "basics" : self.as_json(),
            "work" : work_list,
            "volunteer" : volunteer_list,
            "education" : education_list,
            "awards" : awards_list,
            "publications" : publications_list,
            "skills" : skills_list,
            "languages" : language_list,
            "interests" : interests_list,
            "references" : references_list,
        }


class Profile(models.Model):
    user = models.ForeignKey(User)

    FACEBOOK = 'FB'
    TWITTER = 'TW'
    LINKEDIN = 'LI'
    GITHUB = 'GH'
    NETWORK_CHOICES = (
        (FACEBOOK, 'Facebook'),
        (TWITTER, 'Twitter'),
        (LINKEDIN, 'Linkedin'),
        (GITHUB, 'Github')
    )

    network = models.CharField(max_length=2, choices=NETWORK_CHOICES)
    username = models.CharField(max_length=150)
    url = models.URLField()

    class Meta:
        unique_together = ('user', 'network')

    def __str__(self):
        return self.network + " " + self.username

    def as_json(self):
        return {
            "network" : self.get_network_display(),
            "username" : self.username,
            "url" : self.url
        }


class Work(models.Model):
    user = models.ForeignKey(User)

    volunteer = models.BooleanField()
    company = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    website = models.URLField()
    startDate = models.DateField()
    endDate = models.DateField(null=True, blank=True)
    summary = models.TextField()

    class Meta:
        ordering = ['-startDate']

    def __str__(self):
        return self.company + " - " + self.position

    def get_work_highlights(self):
        highlights_list = []
        for highlight in WorkHighlight.objects.filter(work=self):
            highlights_list.append(highlight.text)
        return highlights_list

    def as_json(self):
        work_dict = {
            "position" : self.position,
            "website" : self.website,
            "startDate" : self.startDate,
            "endDate" : self.endDate,
            "summary" : self.summary,
        }

        if self.volunteer:
            work_dict["organization"] = self.company
        else:
            work_dict["company"] = self.company

        work_dict["highlights"] = self.get_work_highlights()

        return work_dict



class WorkHighlight(models.Model):
    work = models.ForeignKey(Work)

    text = models.TextField()

    def __str__(self):
        return self.text[:30] + " - " + self.work.company


class Education(models.Model):
    user = models.ForeignKey(User)

    institution = models.CharField(max_length=150)
    area = models.CharField(max_length=100)
    studyType = models.CharField(max_length=50)
    startDate = models.DateField()
    endDate = models.DateField(null=True, blank=True)
    gpa = models.CharField(max_length=3)

    class Meta:
        ordering = ['-startDate']

    def __str__(self):
        return self.area + " - " + self.institution

    def as_json(self):
        course_list = []
        for course in Course.objects.filter(education=self):
            course_list.append(course.__str__())

        return {
            "institution" : self.institution,
            "area" : self.area,
            "studyType" : self.studyType,
            "startDate" : self.startDate,
            "endDate" : self.endDate,
            "gpa" : self.gpa,
            "courses" : course_list,
        }


class Course(models.Model):
    education = models.ForeignKey(Education)

    coursecode = models.CharField(max_length=10)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.coursecode + " - " + self.description


class Award(models.Model):
    user = models.ForeignKey(User)

    title = models.CharField(max_length=100)
    date = models.DateField()
    awarder = models.CharField(max_length=100)
    summary = models.TextField()

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.title

    def as_json(self):
        return {
            "title" : self.title,
            "date" : self.date,
            "awarder" : self.awarder,
            "summary" : self.summary,
        }


class Publication(models.Model):
    user = models.ForeignKey(User)

    name = models.CharField(max_length=150)
    publisher = models.CharField(max_length=150)
    releaseDate = models.DateField()
    website = models.URLField()
    summary = models.TextField()

    class Meta:
        ordering = ['-releaseDate']

    def __str__(self):
        return self.name + " - " + self.publisher

    def as_json(self):
        return {
            "name" : self.name,
            "publisher" : self.publisher,
            "releaseDate" : self.releaseDate,
            "website" : self.website,
            "summary" : self.summary,
        }


class Keyword(models.Model):
    word = models.CharField(max_length=50)

    def __str__(self):
        return self.word


class Skill(models.Model):
    user = models.ForeignKey(User)

    name = models.CharField(max_length=150)
    level = models.CharField(max_length=25)
    keywords = models.ManyToManyField(Keyword)

    def __str__(self):
        return self.name

    def as_json(self):
        keyword_list = []

        for keyword in self.keywords.all():
            keyword_list.append(keyword.word)

        return {
            "name" : self.name,
            "level" : self.level,
            "keywords" : keyword_list,
        }


class Language(models.Model):
    user = models.ForeignKey(User)

    name = models.CharField(max_length=25)
    level = models.CharField(max_length=25)

    def __str__(self):
        return self.name

    def as_json(self):
        return {
            "name" : self.name,
            "level" : self.level,
        }


class Interest(models.Model):
    user = models.ForeignKey(User)

    name = models.CharField(max_length=50)
    keywords = models.ManyToManyField(Keyword)

    def __str__(self):
        return self.name

    def as_json(self):
        keyword_list = []

        for keyword in self.keywords.all():
            keyword_list.append(keyword.word)

        return {
            "name" : self.name,
            "keywords" : keyword_list,
        }


class Reference(models.Model):
    user = models.ForeignKey(User)

    name = models.CharField(max_length=150)
    reference = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def as_json(self):
        return {
            "name" : self.name,
            "reference" : self.reference,
        }

class Resume(models.Model):
    name = models.CharField(max_length=50)
    RESUME_TYPES =(
        ('generic', 'Generic'),
        ('programmer', 'Computer Programmer')
    )
    resumeType = models.CharField(max_length=25, choices=RESUME_TYPES)
    user = models.ForeignKey(User)
    published = models.BooleanField(default=False)
    publishReferences = models.BooleanField(default=False)
    profiles = models.ManyToManyField(Profile, blank=True)
    work = models.ManyToManyField(Work, blank=True)
    education = models.ManyToManyField(Education, blank=True)
    awards = models.ManyToManyField(Award, blank=True)
    publications = models.ManyToManyField(Publication, blank=True)
    skills = models.ManyToManyField(Skill, blank=True)
    languages = models.ManyToManyField(Language, blank=True)
    interests = models.ManyToManyField(Interest, blank=True)
    references = models.ManyToManyField(Reference, blank=True)

    class Meta:
        unique_together = ('user', 'name')

    def basic_as_json(self):
        account = Account.objects.get(user=self.user)
        return account.as_json()

    def work_as_json(self):
        work_list = []
        for work in self.work.all():
            if not work.volunteer:
                work_list.append(work.as_json())
        return work_list

    def volunteer_as_json(self):
        volunteer_list = []
        for work in self.work.all():
            if work.volunteer:
                volunteer_list.append(work.as_json())
        return volunteer_list

    def education_as_json(self):
        education_list = []
        for education in self.education.all():
            education_list.append(education.as_json())
        return education_list

    def awards_as_json(self):
        awards_list = []
        for award in self.awards.all():
            awards_list.append(award.as_json())
        return awards_list

    def publications_as_json(self):
        publications_list = []
        for publication in self.publications.all():
            publications_list.append(publication.as_json())
        return publications_list

    def skills_as_json(self):
        skills_list = []
        for skill in self.skills.all():
            skills_list.append(skill.as_json())
        return skills_list

    def languages_as_json(self):
        languages_list = []
        for language in self.languages.all():
            languages_list.append(language.as_json())
        return languages_list

    def interests_as_json(self):
        interests_list = []
        for interest in self.interests.all():
            interests_list.append(interest.as_json())
        return interests_list

    def references_as_json(self):
        references_list = []
        for reference in self.references.all():
            references_list.append(reference.as_json())
        return references_list

    def as_json(self):
        return {
            "basics" : self.basic_as_json(),
            "work" : self.work_as_json(),
            "volunteer" : self.volunteer_as_json(),
            "education" : self.education_as_json(),
            "awards" : self.awards_as_json(),
            "publications" : self.publications_as_json(),
            "skills" : self.skills_as_json(),
            "languages" : self.languages_as_json(),
            "interests" : self.interests_as_json(),
            "references" : self.references_as_json(),
        }
