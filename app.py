
"""Set up a YouTube Data API key:

Go to the Google Cloud Console.
Create a new project or select an existing one.
Enable the YouTube Data API v3.
Create an API key."""

# pip install streamlit google-auth google-auth-oauthlib google-api-python-client youtube_transcript_api markdown
import openai
import streamlit as st
import re
from googleapiclient.discovery import build
from youtube_transcript_api import YouTubeTranscriptApi
import markdown


"""Set up Google API credentials:

Go to the Google Cloud Console.
Create a new project or select an existing one.
Enable the YouTube Data API v3.
Create an OAuth 2.0 client ID and download the client secret JSON file. Place the file in the same directory as your Python script.


function to authenticate the user using the Google API:"""

openai.api_key = "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"

API_KEY = "AIzaSyAbh_P33tDXuxs4fL_Z4JKgqJO1WtBJDnY"


#function to extract video ID from the YouTube URL:


def extract_video_id(url):
    video_id = re.search(r"(?<=v=)[\w-]+", url)
    if video_id:
        return video_id.group()
    return None


# function to get the video transcript:

def get_transcript(video_id):
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        return transcript
    except Exception as e:
        st.error(f"Error: {e}")
        return None



#function to convert the transcript into Markdown format


def transcript_to_markdown(transcript):
    md_text = ""
    line_counter = 1
    for entry in transcript:
        md_text += f"{entry['text']} "
        if line_counter % 3 == 0:
            md_text += "  \n\n"
        line_counter += 1
    return md_text







#Create the Streamlit app:

def main():
    st.title("YouTube Video Transcript Extractor by Polymath Solutions")

    url = st.text_input("Enter a YouTube video URL:")

    if url:
        video_id = extract_video_id(url)
        if not video_id:
            st.error("Invalid URL. Please enter a valid YouTube video URL.")
        else:
            transcript = get_transcript(video_id)
            if transcript:
                md_text = transcript_to_markdown(transcript)
                st.markdown(md_text)
            else:
                st.warning("No transcript found for the video.")

if __name__ == "__main__":
    main()





