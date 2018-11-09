''' course_app.views.py '''

from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader


def index(request):
    return HttpResponse("Here are the codez.")

def test_video(request):
    return render(request, 'videos/index.html')
