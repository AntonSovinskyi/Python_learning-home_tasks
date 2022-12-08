from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

from .forms import NoteForm
from .models import Notes, Categories


def greeting(request):
    return HttpResponse("Hello from Notes app.")


def test(request):
    print(request.method)
    latest_note_list = Notes.objects.order_by('text')
    template = loader.get_template('notes/test.html')
    context = {
        'list': latest_note_list,
    }
    return HttpResponse(template.render(context, request))

def create_note(request):
    template = loader.get_template('notes/note.html')
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            Notes.objects.create(**form.cleaned_data)
            return HttpResponseRedirect('test/')
    else:
        form = NoteForm()
    return HttpResponse(template.render({'form': form}, request))

def update_note(request, id):
    note = Notes.objects.get(id=id)
    template = loader.get_template('notes/update.html')
    context = {'quest': note}
    return HttpResponse(template.render(context, request))

def perform_update(request, id):
    data = request.POST.dict()
    data.pop('csrfmiddlewaretoken', None)
    Notes.objects.filter(id=id).update(**data)
    return HttpResponseRedirect(reverse('test'))

def delete_note(request, id):
    note = Notes.objects.get(id=id)
    template = loader.get_template('notes/delete.html')
    context = {'quest': note}
    return HttpResponse(template.render(context, request))

def perform_delete(request, id):
    data = request.POST.dict()
    data.pop('csrfmiddlewaretoken', None)
    Notes.objects.filter(id=id).update(**data)
    return HttpResponseRedirect(reverse('test'))