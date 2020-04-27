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
	if " " in str:
		hours = str.split(' ')
		newHour = int(hours[0])
		if hours[1] == "PM":
			newHour = newHour + 12
		return newHour
	else:
		newHour = int(str[0])
		if "pm" in str.lower():
			newHour = newHour + 12
		return newHour

def convertTime(str):
	timesArr = []
	lowerTime = str.lower()
	if lowerTime == "all day":
		json = {}
		json['start'] = 0
		json['end'] = 24
		timesArr.append(json)
	elif "&" in lowerTime:
		times = str.split(' & ')
		for time in times:
			splitTimes = time.split(' - ')
			json = {}
			json['start'] = convertHours(splitTimes[0])
			json['end'] = convertHours(splitTimes[1])
			timesArr.append(json)
	else:
		times = str.split(' - ')
		json = {}
		json['start'] = convertHours(times[0])
		json['end'] = convertHours(times[1])
		timesArr.append(json)

	return timesArr

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
	div = soup.find_all('div', class_="tabbertab")

	northTable = div[0].find('table')
	southTable = div[1].find('table')
	northRows = northTable.find_all('tr')
	southRows = southTable.find_all('tr')

	southTime = [ele.text.strip() for ele in southRows[1:]]

	for i, row in enumerate(northRows):
		cols = row.find_all('td')
		southCols = southRows[i].find_all('td')

		if i == 0:
			cols = [ele.text.strip() for ele in row.find_all('th')]
			cols[6] = "Months"
			northRows[i] = cols
		else:
			for j, ele in enumerate(cols):
				if j > 6:
					break
				elif j == 5:
					northTime = ele.text.strip()
					northMonths = [ele.text.strip() for ele in cols[j+1:]]
					north = convertAvailability(northTime, northMonths)

					southTime = southCols[j].text.strip()
					southMonths = [ele.text.strip() for ele in southCols[j+1:]]
					south = convertAvailability(southTime, southMonths)

					cols[j] = { 'north': north, 'south': south }
				else:
					if j == 0 or ele.a == None:
						cols[j] = ele.text.strip()
					else:
						cols[j] = ele.a['href']

		northRows[i] = cols[:6]

	northRows.pop(1)
	jsonData = createJSONData(northRows)
	print(json.dumps(jsonData, ensure_ascii=False, indent=4))
	with open('fish.json', 'w', encoding='utf-8') as f:
		json.dump(jsonData, f, ensure_ascii=False, indent=4)

if __name__ == "__main__":
	main()