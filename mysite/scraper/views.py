from django.shortcuts import render, get_object_or_404, render_to_response, redirect
from .forms import ScraperQueryForm
from django.views import View
from .scraper import Scraper

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
			results = self.form.scrape_data()
			return redirect('/')
