## About
This repo parses the relevant pages from the Animal Crossing WiKi to a JSON object that is front-end friendly to parse and use. The end goal is to create a REST API for the data.

As the wiki updates, there is a high chance that the script will be incompatible with the newest wiki's structure. If the new wiki updates to break the script, the plan is to incorporate caching to use the last successful set of data that was converted as the data until the scripts can be updated.

### Current Parsed Pages
1. [Fish](https://animalcrossing.fandom.com/wiki/Fish_%28New_Horizons%29) - [JSON Data](fish.json)

### To be Parse Pages (In Priority Order)
1. [Bugs]([https://animalcrossing.fandom.com/wiki/Bugs_(New_Horizons)](https://animalcrossing.fandom.com/wiki/Bugs_(New_Horizons)))
2. [Fossils]([https://animalcrossing.fandom.com/wiki/Fossils_(New_Horizons)](https://animalcrossing.fandom.com/wiki/Fossils_(New_Horizons)))
3. [Villagers]([https://animalcrossing.fandom.com/wiki/Villager_list_(New_Horizons)](https://animalcrossing.fandom.com/wiki/Villager_list_(New_Horizons)))
4. [Events]([https://animalcrossing.fandom.com/wiki/Events_(New_Horizons)](https://animalcrossing.fandom.com/wiki/Events_(New_Horizons)))

## Usage
The parser is written in Python. To run, you can either manually install the dependencies or rely on the virtual environment as well as the requirements file to manage it for you more efficiently. 

#### To Run:
1. `python3 -m venv env`
2. `pip3 install -r requirements.txt`
3. `source env/bin/activate`
4. `python3 parse_fish.py`

---
This is an in progress work, so feel free to reach out to me for any rooms for improvement, or feel free to open a PR to contribute!

Contact me @KirinSoo#9364 on Discord!