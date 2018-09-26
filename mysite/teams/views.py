from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django_tables2 import RequestConfig
from teams.models import *
from teams.tables import TeamTable
from django.views.generic import DetailView, TemplateView
from django.views.generic.edit import FormView
from django.views import View
from teams.forms import ScraperInputForm, ScraperResultsForm


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
		if(context.get('matched') or context.get('unmatched')):
			num_results=context.get('num_results')

			return render(request, 'teams/scraper_results.html', context)
		return render(request, 'teams/scraper.html', {'form': self.form})

	def post(self, request):
		if request.POST.get('url'):
			self.form = ScraperInputForm(request.POST)
			if self.form.is_valid():
				results = self.form.scrape_data()
				unmatched = results[0]
				matched = results[1]
	
				num_results = results[2]
				for i in range(len(unmatched)):
					unmatched[i][1].append('<input type="checkbox" class="form-check-input" name="save{0}" id="id_save{0}">'.format(i))
				
				self.form=ScraperResultsForm(num_results=num_results)
				context = {
					"unmatched": unmatched,
					"matched": matched,
					"num_results": num_results,
					'form': self.form
					}

				#return render(request, 'teams/scraper_results.html', context)
				return self.render(request, context)
		elif request.POST.get('save_all'):
			num_results=0
			while(True):
				if(request.POST.get("save"+str(num_results))):
					num_results +=1
				else:
					break
			self.form = ScraperResultsForm(data=request.POST, num_results=num_results)
			if self.form.is_valid():
				save_all = self.form.cleaned_data['save_all']
				return HttpResponseRedirect('/teams/scraper/success/')
		context = {"form": self.form}
		return self.render(request, context)

	def get(self, request):
		self.form=ScraperInputForm(initial={"url": "https://play.usaultimate.org/events/TCT-Pro-Championships-2018/schedule/Men/Club-Men/"})
		context = {}
		return self.render(request, context)

	
class ScraperResults(View):
	def get(self, request):
		context = {}
		return render(request, 'teams/scraper_results.html', context)

