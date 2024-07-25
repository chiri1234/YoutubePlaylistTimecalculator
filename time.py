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
# total_duration += timedelta(seconds=int(duration))

## Print the total duration

# print(f"cumulative time : {total_duration}")
# import re
# import requests
# from bs4 import BeautifulSoup
# from datetime import timedelta

# # Define the Youtube Playlist URL
# playlist_url = "https://www.youtube.com/playlist?list=PL9gnSGHSqcnr_DxHsP7AW9ftq0AtAyYqJ"

# # Fetch the HTML content of the playlist page
# response = requests.get(playlist_url)
# html_content = response.text

# # Parse the HTML content using BeautifulSoup
# soup = BeautifulSoup(html_content, 'html.parser')

# # Find all the video durations in the playlist
# duration_regex = re.compile(r'"lengthSeconds":"(\d+)"')
# video_durations = re.findall(duration_regex, str(soup))

# # Calculate the total duration of all videos in seconds
# total_duration_seconds = sum(int(duration) for duration in video_durations)

# # Convert total duration to hours
# total_hours = total_duration_seconds // 3600
# total_minutes = (total_duration_seconds % 3600) // 60
# total_seconds = total_duration_seconds % 60

# # Print the total duration in hours
# print(f"Cumulative time: {total_hours} hours, {total_minutes} minutes, and {total_seconds} seconds")


from flask import Flask, request, jsonify
import requests
import re
from datetime import timedelta
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow cross-origin requests

@app.route('/calculate_duration', methods=['POST'])
def calculate_duration():
    data = request.json
    playlist_url = data.get('playlistUrl')

    if not playlist_url:
        return jsonify({'error': 'Playlist URL is required'}), 400

    try:
        # Fetch HTML content
        response = requests.get(playlist_url)
        response.raise_for_status()
        html_content = response.text

        # Extract video durations
        duration_regex = re.compile(r'"lengthSeconds":"(\d+)"')
        video_durations = re.findall(duration_regex, html_content)

        if not video_durations:
            return jsonify({'error': 'No video durations found in the playlist'}), 404

        # Calculate total duration
        total_duration = timedelta()
        for duration in video_durations:
            total_duration += timedelta(seconds=int(duration))

        # Convert total duration to days, hours, minutes, and seconds
        total_seconds = total_duration.total_seconds()
        days = total_seconds // 86400
        hours = (total_seconds % 86400) // 3600
        minutes = (total_seconds % 3600) // 60
        seconds = total_seconds % 60

        return jsonify({
            'days': int(days),
            'hours': int(hours),
            'minutes': int(minutes),
            'seconds': int(seconds)
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
