from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
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


class ScraperView(View):
	template_name = 'teams/scraper.html'
	success_url = '/teams/scraper/results/'

	def render(self, request, context):
		print('request method: ' + request.method)
		if(context.get('results')):
			print("hello world")
		return render(request, 'teams/scraper.html', {'form': self.form})

	def post(self, request):
		print('request.POST:')
		print(request.POST)
		if request.POST.get('url'):
			self.form = ScraperInputForm(request.POST)
			if self.form.is_valid():
				results = self.form.scrape_data()
				context = {
					"results": results
					}
				#return render(request, 'teams/scraper_results.html', context)
				print(context)
				return self.render(request, context)
		context = {}
		return self.render(request, context)

	def get(self, request):
		self.form=ScraperInputForm()

		context = {}
		return self.render(request, context)

	
class ScraperResults(View):
	def get(self, request):
		context = {}
		return render(request, 'teams/scraper_results.html', context)

