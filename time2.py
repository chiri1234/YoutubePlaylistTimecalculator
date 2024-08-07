import re
import requests
from bs4 import BeautifulSoup
from datetime import timedelta

# Define the Youtube Playlist URL
playlist_url = "https://www.youtube.com/playlist?list=PLu0W_9lII9agq5TrH9XLIKQvv0iaF2X3w"

# Fetch the HTML content of the playlist page
response = requests.get(playlist_url)
html_content = response.text

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Find all the video durations in the playlist
duration_regex = re.compile(r'"lengthSeconds":"(\d+)"')
video_durations = re.findall(duration_regex, str(soup))

# Calculate the total duration of all videos in seconds
total_duration_seconds = sum(int(duration) for duration in video_durations)

# Convert total duration to hours
total_hours = total_duration_seconds // 3600
total_minutes = (total_duration_seconds % 3600) // 60
total_seconds = total_duration_seconds % 60

# Print the total duration in hours
print(f"Cumulative time: {total_hours} hours, {total_minutes} minutes, and {total_seconds} seconds")
