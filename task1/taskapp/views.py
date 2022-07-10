from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from taskapp.models import WhyUs, Team


def home(request):
    why_us = WhyUs.objects.all()
    team = Team.objects.all()
    return render(request, 'index.html',{'why_us':why_us, 'team':team})






