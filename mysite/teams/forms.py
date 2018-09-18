from django import forms
from .scraper import Scraper

class ScraperInputForm(forms.Form):
	url = forms.CharField()
	def scrape_data(self):
		url = self.cleaned_data['url']
		print(Scraper.scrapePoolsPage(url))