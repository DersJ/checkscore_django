from teams.models import *
from bs4 import BeautifulSoup
from django.conf import settings
import requests, string

#page_url = "https://play.usaultimate.org/events/TCT-Pro-Championships-2018/schedule/Men/Club-Men/"

class Scraper():
	def scrapePoolsPage(url):
		soup = BeautifulSoup(requests.get(url).text, 'html.parser')
		pools = soup.find_all('div', 'pool')
		numPools = len(pools)
		teams = []
		
		print(str(len(pools)) + ' pools')
		print(type(pools))

		for p in pools:
			teamlinks = p.find_all('a')
			for team in teamlinks:
				link = team['href']
				team_str = str(team)
				seed = int(team_str.split('(')[1].split(')')[0])
				name = team_str.split('>')[1].split('(')[0][:-1]
				teams.append((name, seed, link))
		return teams

	def scrapeTeamPage(url):
		soup = BeautifulSoup(requests.get(url).text, 'html.parser')
		teamInfo = soup.find('div', 'profile_info')

		city = teamInfo.find(id='CT_Main_0_dlCity')
		city_str = str(city).split('>')[1].split('\t')[3][:-1]

		competitionLevel = teamInfo.find(id="CT_Main_0_dlCompetitionLevel")
		competitionLevel_str = str(competitionLevel).split('>')[4].split('\t')[4][:-4]

		genderDivision = teamInfo.find(id="CT_Main_0_dlGenderDivision")
		genderDivision_str = str(genderDivision).split('>')[4].split('\t')[4][:-4]

		twitterLink = teamInfo.find(id="CT_Main_0_dlTwitter").find('a')['href']
		twitterHandle = twitterLink.split('/')[-1]
		print(city_str + ' ' + competitionLevel_str + ' ' + genderDivision_str + ' ' + twitterLink)




def saveTeams(teams):
	for team in teams:
		pass

#scandal = Team(name="Scandal", city="Washington, D.C.", division=Division.WOMENS, twitterHandle="scandalultimate", twitterLink="http://www.twitter.com/scandalultimate/")
#scandal.save()