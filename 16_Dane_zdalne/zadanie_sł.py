import requests
from pprint import pprint

url = "https://restcountries.com/v3.1/name/germany?fullText=true"
response = requests.request(method="GET", url=url)
#a = int (input("wpisz cyfre"))
data = response.json()[0]
pprint(data.keys())
print(f'Ludnosc:\t\t{data["population"]}')
print(f'Powierzchnia:\t{data["area"]}')
print(f'Waluta:\t\t\t{list(data["currencies"].keys())[0]}')
print(f'Stolica:\t\t{data["capital"][0]}')