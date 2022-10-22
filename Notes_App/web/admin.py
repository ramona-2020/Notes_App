from django.contrib import admin
from Notes_App.web.models import Profile, Note


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('title', )
