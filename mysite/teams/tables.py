import django_tables2 as tables
from django_tables2.utils import A
from .models import Team

class TeamTable(tables.Table):
	twitter = tables.TemplateColumn('<a href="{{  record.twitterLink }}" target="_blank"> {{record.twitterHandle}} </a>')
	
	class Meta:
		model = Team
		# add class="paleblue" to <table> tag
		attrs = {'class': 'table'}