import requests
import time
import json
import discord
from settings import *
from discord import Webhook, RequestsWebhookAdapter
url = 'https://api.promaptools.com/service/us/zip-lat-lng/get/?zip='+ (zip) + '&key=17o8dysaCDrgv1c'
headers = {
    'authority': 'api.promaptools.com',
    'method': 'GET',
    'path': '/service/us/zip-lat-lng/get/?zip=90210&key=17o8dysaCDrgv1c',
    'scheme': 'https',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36'
}
req = requests.get(url, headers=headers).json()
data = req
for station in data["output"]:
    lat = (f"{station['latitude']}")
    longit = (f"{station['longitude']}")
vaccineurl = 'https://api.us.castlighthealth.com/vaccine-finder/v1/provider-locations/search?medicationGuids=a84fb9ed-deb4-461c-b785-e17c782ef88b&lat=' + (lat) + '&long=' + (longit) + '&radius=' + (radius) + '&appointments=true'
headers2 = {
'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'accept-language': 'en-US,en;q=0.9',
'cache-control': 'max-age=0',
'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
'sec-ch-ua-mobile': '?1',
'sec-ch-ua-platform': '\"Android\"',
'sec-fetch-dest': 'document',
'sec-fetch-mode': 'navigate',
'sec-fetch-site': 'none',
'sec-fetch-user': '?1',
'upgrade-insecure-requests': '1',
'Accept-Encoding': 'gzip, deflate, br',
'Connection': 'keep-alive',
'Host': 'api.us.castlighthealth.com',
'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36'
}
req2 = requests.get(vaccineurl, headers=headers2) 
data2 = req2.json()
for station in data2["providers"]:
        locations = (f"{station['name']} Their phone is {station['phone']}")
        print(locations)
length = len(locations)
webhook = Webhook.from_url(webhook, adapter=RequestsWebhookAdapter())
webhook.send( str(length) + ' locations had available appointments within the set ' + str(radius) +' mile radius' )