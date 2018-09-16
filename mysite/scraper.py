from teams.models import *
from bs4 import BeautifulSoup
import requests


#page_url = "https://play.usaultimate.org/events/TCT-Pro-Championships-2018/schedule/Men/Club-Men/"
#page = requests.get(page_url).content
soup = BeautifulSoup(open('/Users/andersjuengst/Downloads/tctMens.html'), 'html.parser')


def scrapePoolsPage(soup):
	pools = soup.find_all('div', 'pool')
	numPools = len(pools)
	teams = {}
	
	print(len(pools))


	#print(soup.get_text())

scrapePoolsPage(soup)
#scandal = Team(name="Scandal", city="Washington, D.C.", division=Division.WOMENS, twitterHandle="scandalultimate", twitterLink="http://www.twitter.com/scandalultimate/")
#scandal.save()