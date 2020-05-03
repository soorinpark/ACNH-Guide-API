## About
This repo parses the relevant pages from the Animal Crossing WiKi to a JSON object that is front-end friendly to parse and use. The end goal is to create a REST API for the data.

As the wiki updates, there is a high chance that the script will be incompatible with the newest wiki's structure. If the new wiki updates to break the script, the plan is to incorporate caching to use the last successful set of data that was converted as the data until the scripts can be updated.


### Dependencies & Services

- **[BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)**: parsing the AC:NH Wiki
- **[Flask](https://flask.palletsprojects.com/en/1.1.x/)**: web framework
- **[Heroku](https://devcenter.heroku.com/categories/reference)**: cloud platform service

### Current Parsed Pages
1. [Fish](https://animalcrossing.fandom.com/wiki/Fish_%28New_Horizons%29)
	- [JSON File](data/fish.json) 
	- [GET `/fish`](https://acnh-guide-api-prod.herokuapp.com/fish)
2. [Bugs](https://animalcrossing.fandom.com/wiki/Bugs_(New_Horizons)) 
	- [JSON File](data/bugs.json)
	- [GET `/bugs`](https://acnh-guide-api-prod.herokuapp.com/bugs)

### To be Parse Pages (In Priority Order)
1. [Fossils]([https://animalcrossing.fandom.com/wiki/Fossils_(New_Horizons)](https://animalcrossing.fandom.com/wiki/Fossils_(New_Horizons)))
2. [Villagers]([https://animalcrossing.fandom.com/wiki/Villager_list_(New_Horizons)](https://animalcrossing.fandom.com/wiki/Villager_list_(New_Horizons)))
3. [Events]([https://animalcrossing.fandom.com/wiki/Events_(New_Horizons)](https://animalcrossing.fandom.com/wiki/Events_(New_Horizons)))

## Usage
The parser is written in Python. There are a couple ways to access the data.

1. Downloading the static `json` files under the `data` directory manually. These files get updated when I push changes to the repo, so it might not be as up to date.
2. Through the API endpoints. These endpoints scrapes the latest Wiki at runtime therefore the informcation is as up to date as possible.
3. Running the heroku app locally and accessing the API endpoints via localhost. This method also scrapes the latest wiki at runtime so should also be up do date.

In the case that the Wiki has made structural/content changes to the page that the scraper is broken, it's set to return the static json files in the repo as backup. 

### To Run Locally:
1. `python3 -m venv env`
2. `source env/bin/activate`
3. `export APP_SETTINGS="config.DevelopmentConfig"`
4. `pip3 install -r requirements.txt`
5. `python3 app.py`
6. go to `http://localhost/{ENDPOINT}`

---
This is an in progress work, so feel free to reach out to me for any rooms for improvement, or feel free to open a PR to contribute!

Contact me @KirinSoo#9364 on Discord!