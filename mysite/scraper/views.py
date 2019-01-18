from django.shortcuts import render
from .forms import ScraperQueryForm
from django.views import View

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