from bs4 import BeautifulSoup
import requests
import code
import json

def convertMonths(arr):
	months = []
	for i, value in enumerate(arr):
		if value == '✓':
			months.append(i + 1)
	return months

def convertHours(str):
	hours = str.split(' ')
	newHour = int(hours[0])
	if hours[1] == "PM":
		newHour = newHour + 12

	return newHour

def convertTime(str):
	json = {}
	lowerTime = str.lower()
	if lowerTime == "all day":
		json = None
	else:
		times = str.split(' - ')
		json['start'] = convertHours(times[0])
		json['end'] = convertHours(times[1])

	return json

def createJSON(keyArr, valArr):
	json = {}
	for i in range(len(keyArr)):
		json[keyArr[i]] = valArr[i]
	return json

def createJSONData(arr):
	keys = [key.lower().replace(" ", "_") for key in arr[0]]
	values = arr[1:]

	data = { 'data': [] }
	for i, vals in enumerate(values):
		data['data'].append(createJSON(keys, vals))
	
	return data

def main():
	link = "https://animalcrossing.fandom.com/wiki/Fish_(New_Horizons)"
	f = requests.get(link)
	soup = BeautifulSoup(f.text, 'html.parser')

	table = soup.find('table', class_='sortable')
	rows = table.find_all('tr')

	for i, row in enumerate(rows):
		cols = row.find_all('td')
		if i == 0:
			cols = [ele.text.strip() for ele in row.find_all('th')]
			cols[6] = "Months"
		else:
			for j, ele in enumerate(cols):
				if j > 6:
					break
				elif j == 6:
					strippedCols = [ele.text.strip() for ele in cols[j:]]
					months = convertMonths(strippedCols)
					cols[j] = months
				else:
					if j == 0 or ele.a == None:
						cols[j] = ele.text.strip()
						if j == 5:
							cols[j] = convertTime(cols[j])
					else:
						cols[j] = ele.a['href']

		rows[i] = cols[:7]

	jsonData = createJSONData(rows)
	print(json.dumps(jsonData, ensure_ascii=False, indent=4))
	with open('fish.json', 'w', encoding='utf-8') as f:
		json.dump(jsonData, f, ensure_ascii=False, indent=4)

if __name__ == "__main__":
	main()