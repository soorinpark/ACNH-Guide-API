from parse_fish import *
from parse_bugs import *
from flask import Flask
import os

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
print(os.environ['APP_SETTINGS'])

@app.route('/fish')
def parseFish():
	try:
		return fishMain()
	except:
		with open('data/fish.json', 'r') as f:
		    return f.read()

@app.route('/bugs')
def parseBugs():
	try:
		return bugsMain()
	except:
		with open('data/bugs.json', 'r') as f:
		    return f.read()

if __name__ == '__main__':
    app.run()