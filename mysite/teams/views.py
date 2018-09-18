from django.shortcuts import render, get_object_or_404, render_to_response
from django_tables2 import RequestConfig
from teams.models import *
from teams.tables import TeamTable
from django.views.generic import DetailView, TemplateView
from django.views.generic.edit import FormView
from django.views import View
from teams.forms import ScraperInputForm


def teamlist(request, *args, **kwargs):
	table = TeamTable(Team.objects.all())
	table.exclude = ('id', 'twitterHandle', 'twitterLink')
	RequestConfig(request).configure(table)
	return render(request, 'teams/teamslist.html', {'table': table})

class TeamDetailView(DetailView):
	queryset = Team.objects.all()

def rosterDetailView(request, id):
	instance = get_object_or_404(Roster, id=id)
	queryset = RosterMembership.objects.filter(roster=instance)

	context = {
		"roster": instance,
		"rm_list": queryset,
		"title": "Roster Detail"
	}
	return render(request, 'teams/roster_detail.html', context)


class ScraperView(FormView):
	template_name = 'teams/scraper.html'
	form_class = ScraperInputForm
	success_url = '/success/'

	def form_valid(self, form):
		form.scrape_data()
		return super().form_valid(form)

	# def get(self, request):
	# 	context = {
	# 		"name": "Truck Stop",
	# 	}
	# 	return render(request, 'teams/scraper.html', context)
