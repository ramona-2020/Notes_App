from django.shortcuts import render, redirect

from Notes_App.web.forms.note import NoteForm, EditNoteForm, DeleteNoteForm
from Notes_App.web.forms.profile import ProfileForm, ProfileDeleteForm
from Notes_App.web.models import Profile, Note


def has_profile():
    return Profile.objects.first()


def create_profile(request):
    form = ProfileForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('homepage')

    context = {
        'form': form,
    }
    return render(request, 'home-no-profile.html', context)


def delete_profile(request):
    profile = Profile.objects.first()
    if request.method == 'POST':
        form = ProfileDeleteForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = ProfileDeleteForm(instance=profile)

    context = {
        'profile': profile,
        'form': form,
    }
    return render(request, 'profile-delete.html', context)


def homepage(request):
    user_profile = has_profile()
    notes = Note.objects.all()

    if not user_profile:
        return create_profile(request)

    context = {
        'notes': notes
    }
    return render(request, "home-with-profile.html", context)


def profile(request):
    profile = Profile.objects.first()
    notes_count = Note.objects.count()

    context = {
        'profile': profile,
        'notes_count': notes_count
    }

    return render(request, "profile.html", context)


def add_note(request):
    form = NoteForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('homepage')

    context = {
        'form': form,
    }
    return render(request, "note-create.html", context)


def edit_note(request, pk):
    note = Note.objects.get(pk=pk)
    if request.method == 'POST':
        form = EditNoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = EditNoteForm(instance=note)

    context = {
        'note': note,
        'form': form,
    }
    return render(request, "note-edit.html", context)


def delete_note(request, pk):
    note = Note.objects.get(pk=pk)
    if request.method == 'POST':
        form = DeleteNoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = DeleteNoteForm(instance=note)

    context = {
        'note': note,
        'form': form,
    }
    return render(request, "note-delete.html", context)


def note_details(request, pk):
    note = Note.objects.get(pk=pk)
    context = {
        'note': note
    }
    return render(request, "note-details.html", context)

