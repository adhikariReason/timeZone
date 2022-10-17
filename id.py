import requests

json_page = requests.get('https://legacyapi.recyclenation.com/materials?auth_code=8f194edfb445b5164dff2741098d1a1e')
# r = requests.get('https://recyclenation.com/find/?materials=5898252&zip=64468')  #request to site recyclenation.com
print(json_page.status_code)
import pickle
pickle.dump(json_page, open('test.pkl', 'wb'))
jd = pickle.load(open('./test.pkl', 'rb'))
json_data = (jd.json()['materials'])
json_dict = {obj['material_id']:obj['description'] for obj in json_data }
# print(json_dict)

def sums(a,b):
	c=a+b
	return c

print(sums(1,2))

