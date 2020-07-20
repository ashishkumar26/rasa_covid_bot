from rasa_sdk import Action
from rasa_sdk.events import SlotSet
import requests
import logging
import time
from datetime import datetime
import math

logger = logging.getLogger()

names = ['',' Thousand',' Million',' Billion',' Trillion']

def _convert(n):
    n = float(n)
    millidx = max(0,min(len(names)-1,
                        int(math.floor(0 if n == 0 else math.log10(abs(n))/3))))
    return '{:.0f}{}'.format(n / 10**(3 * millidx), names[millidx])

class ActionWeather(Action):
    def name(self):
      return 'action_covid'

    def run(self, dispatcher, tracker, domain):
        country = tracker.get_slot('country')
        logger.info("Country read from slot ", country)
        print("Country read from slot ", country)
        if country == None:
            country_url =  "https://corona.lmao.ninja/v2/countries/india"
        else:
            country_url = "https://corona.lmao.ninja/v2/countries/"+country
        ##
        world_url = "https://corona.lmao.ninja/v2/all"
        world_content = requests.get(world_url)
        world_data = world_content.json()
        #
        country_content = requests.get(country_url)
        country_data = country_content.json()
        ###
        country_name = country_data['country']
        flag = country_data['countryInfo']['flag']
        totalCases = country_data['cases']
        recovered = country_data['recovered']
        deaths = country_data['deaths']
        todayDeaths = country_data['todayDeaths']
        todayRecovered = country_data['todayRecovered']
        active = country_data['active']
        critical = country_data['critical']
        casesPerOneMillion = country_data['casesPerOneMillion']
        deathsPerOneMillion = country_data['deathsPerOneMillion']
        tests = country_data['tests']
        testsPerOneMillion = country_data['testsPerOneMillion']
        population = country_data['population']
        continent = country_data['continent']
        tm = country_data['updated']/1000
        tm = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(tm))
        #
        population = _convert(population)
        ###
        response = """Country Name : {} \n Total Population :{} \n Total Reported Cases : {} \n Total Recovered : {} \n Total Deaths : {} \n Total Active : {} \n Last Updated : {}""".format(country_name, population, totalCases, recovered, deaths, active, tm)
        dispatcher.utter_message(image=flag, text=response)
        return []
