import requests
from io import StringIO

import pandas as pd
url = "https://sky-scanner3.p.rapidapi.com/flights/search-one-way"

querystring = {"fromEntityId":"DEL","toEntityId":"BOM","departDate":"2024-06-16","currency":"INR","stops":"direct","cabinClass":"economy"}

headers = {
	"x-rapidapi-key": "401c261d13mshac33d6e1fcc7913p1b9a0cjsn30830ad2c7aa",
	"x-rapidapi-host": "sky-scanner3.p.rapidapi.com",
	"X-RapidAPI-Mock-Response": "212"
}

response = requests.get(url, headers=headers, params=querystring)
r = response.text
print(response.json())
result = pd.read_csv(StringIO(response.text))
print(result)



