from teams.models import *
from bs4 import BeautifulSoup
from django.conf import settings
import requests, string

#page_url = "https://play.usaultimate.org/events/TCT-Pro-Championships-2018/schedule/Men/Club-Men/"

class Scraper():
	def cleanCityString(citystring):
		return citystring.replace('\n', '').replace('\t','').replace('\r', '')
	def scrapeTeamEventPage(url):
		soup = BeautifulSoup(requests.get(url).text, 'html.parser')
		teamInfo = soup.find('div', 'profile_info')
		results = {}

		city = teamInfo.find('p', 'team_city')
		results['City']=Scraper.cleanCityString(city.get_text())

		dl_list = teamInfo.find_all('dl')
		for dl in dl_list:
			descriptor = dl.find('dt').get_text()
			description = dl.find('dd')
			if(descriptor == "Competition Level:"):
				results["Competition Level"] = description.get_text()
			if(descriptor == "Gender Division:"):
				results["Gender Division"] = description.get_text()
			if(descriptor == "Twitter:"):
				results["Twitter"] = description.find('a').get_text()

		return results
	def scrapePoolsPage(url):
		#soup = BeautifulSoup(requests.get(url).text, 'html.parser')
		soup = BeautifulSoup(open('./tctMens.html'), 'html.parser')
		pools = soup.find_all('div', 'pool')
		teams = []
		results =[]
		
		print(str(len(pools)) + ' pools')

		for p in pools:
			teamlinks = p.find_all('a')
			for team in teamlinks:
				link = team['href']
				team_str = str(team)
				seed = int(team_str.split('(')[1].split(')')[0])
				name = team_str.split('>')[1].split('(')[0][:-1]
				teams.append([name, seed, link])
		# for team in teams:
		# 	team_url = 'https://play.usaultimate.org' + team[2]
		# 	print(team[0])
		# 	team_page_info = Scraper.scrapeTeamEventPage(team_url)
		# 	team_info = [team_page_info['City'], team_page_info['Gender Division'], team_page_info['Competition Level'], team_page_info['Twitter']]
		# 	results.append([team[0], team_info])
		team_url = 'https://play.usaultimate.org' + teams[1][2]
		team_page_info = Scraper.scrapeTeamEventPage(team_url)
		team_info = [team_page_info['City'], team_page_info['Gender Division'], team_page_info['Competition Level'], team_page_info['Twitter']]
		results.append([teams[1][0], team_info])
		print(results)
		return results

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
		return (city_str, competitionLevel_str, genderDivision_str, twitterLink)


	



def saveTeams(teams):
	for team in teams:
		pass

#scandal = Team(name="Scandal", city="Washington, D.C.", division=Division.WOMENS, twitterHandle="scandalultimate", twitterLink="http://www.twitter.com/scandalultimate/")
#scandal.save()