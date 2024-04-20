import os
import json
import googleapiclient.discovery
from google.oauth2 import service_account

credentials_file_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")

# Load credentials from JSON file
with open(credentials_file_path) as f:
    credentials = json.load(f)


creds = service_account.Credentials.from_service_account_info(credentials)
youtube = googleapiclient.discovery.build("youtube", "v3", credentials=creds)

def search_youtube_videos(query:str, num_of_results:int):
    request = youtube.search().list(
        part="snippet",
        q=query,
        type="video",
        maxResults=num_of_results 
    )
    response = request.execute()

    video_links = []
    for item in response['items']:
        video_id = item['id']['videoId']
        video_link = f"https://www.youtube.com/watch?v={video_id}"
        video_links.append(video_link)
    
    return video_links
