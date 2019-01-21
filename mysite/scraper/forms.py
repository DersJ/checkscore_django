from django import forms
from .models import ScraperQuery
from .scraper import Scraper
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _

class ScraperQueryForm(forms.ModelForm):
	class Meta:
		model = ScraperQuery
		fields = [
			"url",
			"pageType",
		]
	def clean_url(self):
		val = URLValidator()
		url = self.cleaned_data['url']
		val(url)
		if(url.split('//')[1][:20] != 'play.usaultimate.org'):
			raise ValidationError(_('Url not usaultimate.org'), code='not_usau')
		return url
	def scrape_data(self):
		url = self.cleaned_data['url']
		return Scraper.scrapePoolsPage(url)