# import re
# import requests
# from bs4 import BeautifulSoup
# from datetime import timedelta

# # define the Youtube Playlist URL

# playlist_url = "https://www.youtube.com/playlist?list=PL9gnSGHSqcnr_DxHsP7AW9ftq0AtAyYqJ"
# # Fetch the html content of the playlist page
# response = requests.get(playlist_url)
# html_content = response.text

# # Parse the html content using BeautifulSoup
# soup = BeautifulSoup(html_content, 'html.parser')

# # Find all the video ids in the playlist
# duration_regex = re.compile(r'"lengthseconds" : "(\d+)"')
# vides_durations = re.findall(duration_regex, str(soup))

# # Calculate the total duration of all videos
# total_duration = timedelta()
# for duration in vides_durations:
#     total_duration += timedelta(seconds=int(duration))

# # Print the total duration

# print(f"cumulative time : {total_duration}")
import re
import requests
from bs4 import BeautifulSoup
from datetime import timedelta

# Define the Youtube Playlist URL
playlist_url = "https://www.youtube.com/playlist?list=PL9gnSGHSqcnr_DxHsP7AW9ftq0AtAyYqJ"

# Fetch the html content of the playlist page
response = requests.get(playlist_url)
html_content = response.text

# Parse the html content using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Find all the video durations in the playlist
duration_regex = re.compile(r'"lengthSeconds":"(\d+)"')
video_durations = re.findall(duration_regex, str(soup))

# Calculate the total duration of all videos
total_duration = timedelta()
for duration in video_durations:
    total_duration += timedelta(seconds=int(duration))

# Print the total duration
print(f"Cumulative time: {total_duration}")
