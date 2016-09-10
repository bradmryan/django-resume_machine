from django.db import models

# Create your models here.
from django.contrib.auth.models import User

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


class Profile(models.Model):
    user = models.ForeignKey(User)

    FACEBOOK = 'FB'
    TWITTER = 'TW'
    LINKEDIN = 'LI'
    NETWORK_CHOICES = (
        (FACEBOOK, 'Facebook'),
        (TWITTER, 'Twitter'),
        (LINKEDIN, 'Linkedin'),
    )

    network = models.CharField(max_length=2, choices=NETWORK_CHOICES)
    username = models.CharField(max_length=150)
    url = models.URLField()

    class Meta:
        unique_together = ('user', 'network')

    def __str__(self):
        return self.network + " " + self.username


class Work(models.Model):
    user = models.ForeignKey(User)

    volunteer = models.BooleanField()
    company = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    website = models.URLField()
    startDate = models.DateField()
    endDate = models.DateField()
    summary = models.TextField()

    class Meta:
        ordering = ['-startDate']

    def __str__(self):
        return self.company + " - " + self.position


class WorkHighlight(models.Model):
    work = models.ForeignKey(Work)

    highlight = models.TextField()

    def __str__(self):
        return self.highlight[:30] + " - " + self.work.company


class Education(models.Model):
    user = models.ForeignKey(User)

    institution = models.CharField(max_length=150)
    area = models.CharField(max_length=100)
    studyType = models.CharField(max_length=50)
    startDate = models.DateField()
    endDate = models.DateField()
    gpa = models.CharField(max_length=3)

    class Meta:
        ordering = ['-startDate']

    def __str__(self):
        return self.area + " - " + self.institution


class Course(models.Model):
    education = models.ForeignKey(Education)

    coursecode = models.CharField(max_length=10)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.coursecode + " - " + self.education.institution


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


class Keyword(models.Model):
    word = models.CharField(max_length=50)

    def __str__(self):
        return self.word


class Skill(models.Model):
    user = models.ForeignKey(User)

    name = models.CharField(max_length=150)
    level = models.CharField(max_length=25)
    keyword = models.ManyToManyField(Keyword)

    def __str__(self):
        return self.name


class Language(models.Model):
    user = models.ForeignKey(User)

    name = models.CharField(max_length=25)
    level = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class Interest(models.Model):
    user = models.ForeignKey(User)

    name = models.CharField(max_length=50)
    keyword = models.ManyToManyField(Keyword)

    def __str__(self):
        return self.name


class Reference(models.Model):
    user = models.ForeignKey(User)

    name = models.CharField(max_length=150)
    reference = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Resume(models.Model):
    name = models.CharField(max_length=50)
    resumeType = models.CharField(max_length=25)
    user = models.ForeignKey(User)
    published = models.BooleanField(default=False)
    profiles = models.ManyToManyField(Profile)
    work = models.ManyToManyField(Work)
    education = models.ManyToManyField(Education)
    awards = models.ManyToManyField(Award)
    publications = models.ManyToManyField(Publication)
    skills = models.ManyToManyField(Skill)
    languages = models.ManyToManyField(Language)
    interests = models.ManyToManyField(Interest)
