from django.conf.urls import url, include
from django.views.generic import TemplateView
from django.urls import path, re_path
from scraper import views


urlpatterns = [
	url(r'^$', views.ScraperView.as_view(), name='scraper'),
]