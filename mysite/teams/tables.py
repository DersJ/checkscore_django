import django_tables2 as tables
from django_tables2.utils import A
from .models import Team

class TeamTable(tables.Table):
	twitterLink = tables.TemplateColumn('<b> {{  record.twitterLink }} </b>')
	
	class Meta:
		model = Team
		# add class="paleblue" to <table> tag
		attrs = {'class': 'table'}