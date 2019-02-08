from django.shortcuts import render, get_object_or_404, render_to_response, redirect
from .forms import ScraperQueryForm
from django.views import View
from django.http import JsonResponse
from .scraper import Scraper
from .models import *
from teams.models import Team
# Create your views here.
class ScraperView(View):
	template_name = 'scraper/scraper.html'
	success_url = '/teams/scraper/results/'

	def render(self, request, context):
		if(context.get('matched') or context.get('unmatched')):
			num_results=context.get('num_results')

			return render(request, 'teams/scraper_results.html', context)
		return render(request, 'scraper/scraper.html', {'form': self.form})

	def get(self, request):
		if not request.user.is_authenticated:
			return redirect('/401/')
		self.form=ScraperQueryForm()
		context = {}
		return self.render(request, context)

	def post(self, request):
		self.form = ScraperQueryForm(request.POST)
		if self.form.is_valid():
			query = self.form.save(request.user)
			scraper = Scraper(query)
			scraper.scrape()

			#results = self.form.scrape_data()
			return redirect('/scraper/results/')
		context = {}
		return self.render(request, context)


class ScraperQueryResultsView(View):
	def render(self, request, context):
		return render(request, 'scraper/results.html', context)

	def get(self, request):
		if not request.user.is_authenticated:
			return redirect('/401/')
		queries = request.user.scraper_queries.all()


		
		context = {
			"queries": queries,
		}
		return self.render(request, context)

class ResultDetailView(View):
	def render(self, request, context):
		return render(request, 'scraper/result_detail.html', context)

	def get_object(self):
		return get_object_or_404(ScraperQuery, pk=self.kwargs.get('pk'))

	def get(self, request, pk):
		self.obj = self.get_object()
		return self.render(request, {"teams": self.obj.teams.all(), "query": self.obj})

def ajax_save_team(request):
	poolPageTeamInfo = get_object_or_404(PoolPageTeamInfo, id=request.GET.get('id', None))
	results = Scraper.scrapeTeamEventPage(poolPageTeamInfo.eventTeamURL)
	print(results)
	team = Team(name=poolPageTeamInfo.name, city=results['City'], division=results['Division'], twitterLink=results['Twitter'])
	team.save()
	print(team)
	return JsonResponse({'saved': True})

#{'City': 'Washington', 'Competition Level': 'Club', 'Gender Division': 'Men', 'Twitter': 'https://twitter.com/truckstopulti'}
