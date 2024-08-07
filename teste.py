import requests

url = "https://linkedin-data-api.p.rapidapi.com/search-jobs"

querystring = {"keywords":"golang","locationId":"92000000","datePosted":"anyTime","sort":"mostRelevant"}

headers = {
	"x-rapidapi-key": "90371450f9mshea3a6b1bd9728cep11af93jsn53f8aa0ce60d",
	"x-rapidapi-host": "linkedin-data-api.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())
