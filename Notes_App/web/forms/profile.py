from django import forms

from Notes_App.web.models import Profile, Note


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class ProfileDeleteForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].disabled = 'disabled'

    class Meta:
        model = Profile
        fields = '__all__'

    def save(self, commit=True):
        if commit:
            self.instance.delete()

            notes = Note.objects.all()
            notes.delete()

            return self.instance
