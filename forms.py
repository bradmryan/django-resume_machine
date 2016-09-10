from django.forms import ModelForm, inlineformset_factory
from resume_machine.models import Account, Image, Resume, Profile, Work, Education, Award, Publication, Skill, Language, Interest

class AccountForm(ModelForm):
    current_user = None

    def __init__(self, *args, **kwargs):
        super(AccountForm, self).__init__(*args, **kwargs)
        self.fields['picture'].queryset = Image.objects.filter(user=self.current_user)

    class Meta:
        model = Account
        exclude = ('user',)


class ResumeForm(ModelForm):
    current_user = None

    def __init__(self, *args, **kwargs):
        super(ResumeForm, self).__init__(*args, **kwargs)
        self.fields['profiles'].queryset = Profile.objects.filter(user=self.current_user)
        self.fields['work'].queryset = Work.objects.filter(user=self.current_user)
        self.fields['education'].queryset = Education.objects.filter(user=self.current_user)
        self.fields['awards'].queryset = Award.objects.filter(user=self.current_user)
        self.fields['publications'].queryset = Publication.objects.filter(user=self.current_user)
        self.fields['skills'].queryset = Skill.objects.filter(user=self.current_user)
        self.fields['languages'].queryset = Language.objects.filter(user=self.current_user)
        self.fields['interests'].queryset = Interest.objects.filter(user=self.current_user)

    class Meta:
        model = Resume
        exclude = ('user',)
