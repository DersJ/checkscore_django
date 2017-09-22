import django_tables2 as tables
from .models import Team

class TeamTable(tables.Table):
    class Meta:
        model = Team
        # add class="paleblue" to <table> tag
        attrs = {'class': 'table'}