from django.contrib import admin
from resume_machine.models import Account, Resume, Profile, Work, WorkHighlight, Education, Course, Award, Publication, Skill, Language, Interest, Reference, Image, Keyword
from resume_machine.forms import AccountForm, ResumeForm

# Register your models here.
@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('user', 'name')
    exclude = ('user',)

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'user', None) is None:
            obj.user = request.user
        obj.save()


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'middleinitial', 'lastname', 'user')
    exclude = ('user',)
    form = AccountForm

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'user', None) is None:
            obj.user = request.user
        obj.save()

    def get_form(self, request, obj=None, **kwargs):
        form = super(AccountAdmin, self).get_form(request, **kwargs)
        form.current_user = request.user
        return form


@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ('name', 'user')
    exclude = ('user',)
    form = ResumeForm

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'user', None) is None:
            obj.user = request.user
        obj.save()

    def get_form(self, request, obj=None, **kwargs):
        form = super(ResumeAdmin, self).get_form(request, **kwargs)
        form.current_user = request.user
        return form


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'url')
    exclude = ('user',)

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'user', None) is None:
            obj.user = request.user
        obj.save()


class WorkHighlightInline(admin.TabularInline):
    model = WorkHighlight

@admin.register(Work)
class WorkAdmin(admin.ModelAdmin):
    list_display = ('volunteer', 'company', 'position')
    exclude = ('user',)
    inlines = [
        WorkHighlightInline,
    ]

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'user', None) is None:
            obj.user = request.user
        obj.save()


class CourseInline(admin.TabularInline):
    model = Course

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('institution', 'area')
    exclude = ('user',)
    inlines = [CourseInline,]

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'user', None) is None:
            obj.user = request.user
        obj.save()


@admin.register(Award)
class AwardAdmin(admin.ModelAdmin):
    list_display = ('title', 'awarder')
    exclude = ('user',)

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'user', None) is None:
            obj.user = request.user
        obj.save()


@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    list_display = ('name', 'publisher')
    exclude = ('user',)

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'user', None) is None:
            obj.user = request.user
        obj.save()


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'level')
    exclude = ('user',)

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'user', None) is None:
            obj.user = request.user
        obj.save()


@admin.register(Interest)
class InterestAdmin(admin.ModelAdmin):
    list_display = ('name',)
    exclude = ('user',)

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'user', None) is None:
            obj.user = request.user
        obj.save()


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ('name', 'level')
    exclude = ('user',)

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'user', None) is None:
            obj.user = request.user
        obj.save()


@admin.register(Reference)
class ReferenceAdmin(admin.ModelAdmin):
    list_display = ('name',)
    exclude = ('user',)

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'user', None) is None:
            obj.user = request.user
        obj.save()


@admin.register(Keyword)
class KeywordAdmin(admin.ModelAdmin):
    list_display = ('word',)
