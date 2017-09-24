from django.shortcuts import render
from django_tables2 import RequestConfig
from teams.models import *
from teams.tables import TeamTable
from django.views.generic import DetailView

def teamlist(request, *args, **kwargs):
	table = TeamTable(Team.objects.all())
	table.exclude = ('id', 'twitterHandle', 'twitterLink')
	RequestConfig(request).configure(table)
	return render(request, 'teams/teamslist.html', {'table': table})

class TeamDetailView(DetailView):
	queryset = Team.objects.all()



