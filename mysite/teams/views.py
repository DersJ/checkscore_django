from django.shortcuts import render
from django_tables2 import RequestConfig
from teams.models import *
from teams.tables import TeamTable


# Create your views here.
def index(request):
	return render(request, 'teams/home.html')

def contact(request):
	return render(request, 'teams/basic.html', {'content': ['Created by Anders Juengst', 'anders.juengst@gmail.com']})

def teamlist(request, *args, **kwargs):
	table = TeamTable(Team.objects.all())
	table.exclude = ('id', 'twitterHandle', 'twitterLink')
	RequestConfig(request).configure(table)
	return render(request, 'teams/teamslist.html', {'table': table})

def teampage(request):
	pass




