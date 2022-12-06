import requests
import json
import pprint
def get_en_ru(text_user,langvitch_in,laungvich_from):
	url = "https://microsoft-translator-text.p.rapidapi.com/translate"
	querystring = {"to":langvitch_in,"api-version":"3.0","from":laungvich_from,"profanityAction":"NoAction","textType":"plain"}
	payload = [{"Text":text_user}]
	headers = {
	"content-type": "application/json",
	"X-RapidAPI-Key": "c4e8847f51msh109ad93ffc9fcfap1aef96jsn8f8ca40f8b49",
	"X-RapidAPI-Host": "microsoft-translator-text.p.rapidapi.com"
	}
	response = requests.request("POST", url, json=payload, headers=headers, params=querystring)
	response1 = response.json()[0]
	#response1 = response1[0]
	response1 = response1['translations']
	response1 = response1[0]
	response1 = response1['text']
	return response1
#print(response.text)
print(get_en_ru("I would really like to drive your car around the block a few times.",'ru','en'))


url = "https://microsoft-translator-text.p.rapidapi.com/Detect"

querystring = {"api-version":"3.0"}

payload = [{"Text": "Ich würde wirklich gern Ihr Auto um den Block fahren ein paar Mal."}]
headers = {
	"content-type": "application/json",
	"X-RapidAPI-Key": "c4e8847f51msh109ad93ffc9fcfap1aef96jsn8f8ca40f8b49",
	"X-RapidAPI-Host": "microsoft-translator-text.p.rapidapi.com"
}

#response = requests.request("POST", url, json=payload, headers=headers, params=querystring)
#response1 = response.json()[0]

#print(response1['language'])
