# this found the trailers for each movie
# pip install google-api-python-client

import json
from googleapiclient.discovery import build

# Set your API key
api_key = "<your api key>"

# Create a YouTube API service
youtube = build("youtube", "v3", developerKey=api_key)


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

movies = load_file("movies.json")



# List of movie titles

for item in movies:
    title = item["Title of"]
    # Search for the movie trailer on YouTube
    search_response = youtube.search().list(
        q=f"{title} trailer",
        part="id",
        type="video",
        maxResults=1
    ).execute()

    # Extract the video ID of the first result
    video_id = search_response["items"][0]["id"]["videoId"]

    # Print the YouTube URL for the trailer
    print(f"{title} Trailer: https://www.youtube.com/watch?v={video_id}")
    # add to table
    item["trailer"] = f"https://www.youtube.com/watch?v={video_id}"
    save_json(movies, "movies2.json")