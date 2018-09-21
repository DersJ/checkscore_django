from django.conf.urls import url, include
from teams import views
from teams.models import Team

urlpatterns = [
    url(r'^$', views.teamlist, name='teamlist'),
    url(r'^scraper/$', views.ScraperView.as_view()),
    url(r'^scraper/results/$', views.ScraperResults.as_view()),
    url(r'^(?P<pk>\w+)/$', views.TeamDetailView.as_view()),
    url(r'^rosters/(?P<id>\d+)/$', views.rosterDetailView, name='roster_detail')
    

]
