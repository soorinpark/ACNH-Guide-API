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
		json['start'] = 0
		json['end'] = 24
	else:
		times = str.split(' - ')
		json['start'] = convertHours(times[0])
		json['end'] = convertHours(times[1])
	return json

def convertAvailability(time, monthsArr):
	isAllDay = time.lower() == "all day"
	hours = convertTime(time)
	months = convertMonths(monthsArr)
	isAllYear = len(months) == 12
	dict = { 
		'hours': hours, 
	 	'months': months,
	 	'isAllDay': isAllDay,
	 	'isAllYear': isAllYear 
	}
	return dict


def createJSON(keyArr, valArr):
	json = {}
	for i in range(len(keyArr)):
		if i == 2:
			json[keyArr[i]] = int(valArr[i])
		else:
			json[keyArr[i]] = valArr[i]
	return json

def createJSONData(arr):
	keys = [key.lower().replace(" ", "_") for key in arr[0]]
	keys[-1] = "availability"
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
				elif j == 5:
					time = ele.text.strip()

					months = [ele.text.strip() for ele in cols[j+1:]]
					availability = convertAvailability(time, months)
					cols[j] = availability
				else:
					if j == 0 or ele.a == None:
						cols[j] = ele.text.strip()
					else:
						cols[j] = ele.a['href']

		rows[i] = cols[:6]

	jsonData = createJSONData(rows)
	print(json.dumps(jsonData, ensure_ascii=False, indent=4))
	with open('fish.json', 'w', encoding='utf-8') as f:
		json.dump(jsonData, f, ensure_ascii=False, indent=4)

if __name__ == "__main__":
	main()