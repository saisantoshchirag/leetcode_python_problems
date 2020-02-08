import requests

url = "https://devru-raaga-v1.p.rapidapi.com/json/browse.asp"

querystring = {"relYear":"2015","l":"T","search":"A"}

headers = {
    'x-rapidapi-host': "devru-raaga-v1.p.rapidapi.com",
    'x-rapidapi-key': "41cf5a2734mshe63eb2ead150e5ap14592ejsn5e3f8c3c6371"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
