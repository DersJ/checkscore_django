from django import forms
from .models import ScraperQuery

class ScraperQueryForm(forms.ModelForm):
	class Meta:
		model = ScraperQuery
		fields = [
			"url",
			"pageType",
		]