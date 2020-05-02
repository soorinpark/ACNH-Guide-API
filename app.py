from parse_fish import *
from parse_bugs import *
from flask import Flask
import os

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
print(os.environ['APP_SETTINGS'])

@app.route('/fish')
def parseFish():
	return fishMain()

@app.route('/bugs')
def parseBugs():
	return bugsMain()

if __name__ == '__main__':
    app.run()