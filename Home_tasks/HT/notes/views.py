from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Notes


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