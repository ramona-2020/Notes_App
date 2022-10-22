from django import forms

from Notes_App.web.models import Note


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = '__all__'


class EditNoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = '__all__'


class DeleteNoteForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].disabled = 'disabled'

    class Meta:
        model = Note
        fields = '__all__'

    def save(self, commit=True):
        if commit:
            self.instance.delete()
            return self.instance
