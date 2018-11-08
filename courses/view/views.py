''' view.views.py '''

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("Here are the codez.")
