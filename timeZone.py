import json
import requests
from bs4 import BeautifulSoup
url = 'https://www.timeanddate.com/worldclock/full.html'
page = requests.get(url)
print(page.status_code)
page_soup = BeautifulSoup(page.text, 'html5lib')
table_content = page_soup .find('tbody')
all_rows = table_content.find_all('tr')
# print(all_rows[37].find_all('td')[1].text)
json_dict = {}
col_count =0
while(col_count<5):
	for row in all_rows:
		place = row.find_all('td')[col_count].text
		time = row.find_all('td')[col_count+1].text
		json_dict[place] = time
		# print(place + "	"+ time +"\n")
	col_count +=2
	
# print(len(json_dict))
with open("data.json", "w") as wf:
    json.dump(json_dict, wf)