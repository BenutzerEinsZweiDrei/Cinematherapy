# this found the streaming available
# pip install simple-justwatch-python-api

import json
from simplejustwatchapi.justwatch import search

def load_file(name):
	     #open and read the file
	     # ressources to X
	f = open(name, "r")
	temp = f.read()
	j = json.loads(temp)
	# return
	return j

def save_json(d, file):
	
	# open file to overwrite content
	f = open(file, "w")
	txt = json.dumps(d)
	f.write(txt)
	f.close()

movies = load_file("movies2.json")


for item in movies:
    title = item["Title of"]
    # Search for the movie on JustWatch

    # Extract the video ID of the first result
    results = search(title, "DE", "en", 1, True)
    # Print the YouTube URL for the trailer
    if results[0].title == title:
    	list = ""
    	for item2 in results[0].offers:
    		if item2.monetization_type=="FLATRATE":
    			list = list + item2.name + " ,"
    	# add to json
    	item["Stream free On"] = list
    	print(title+" Stream:" + list)
    			
save_json(movies, "movies5.json")