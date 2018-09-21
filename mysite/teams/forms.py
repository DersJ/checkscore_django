from django import forms
from .scraper import Scraper
from django.core.validators import URLValidator
from django.contrib import messages

class ScraperInputForm(forms.Form):
	url = forms.CharField()
	def clean_url(self):
		val = URLValidator()
		url = self.cleaned_data['url']
		val(url)
		return url

	def scrape_data(self):
		
		url = self.cleaned_data['url']
		print(Scraper.scrapePoolsPage(url))