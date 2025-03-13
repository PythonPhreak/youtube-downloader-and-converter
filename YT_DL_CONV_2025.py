# -*- coding: utf-8 -*-
"""
Created on Thu Mar 13 13:33:14 2025

@author: user
"""

import time
import youtube_dl
from moviepy.editor import *
import os
import glob

def welcome_message():
    print("****** YOUTUBE DOWNLOADER AND CONVERTER ******")
    print("******** Created by Vaios Bakirtzoglou ********")
    time.sleep(1)
    print("\nWelcome to the YouTube downloader and MP3 converter!")
    time.sleep(1)

def download_video():
    try:
        link = input("\nPlease paste the YouTube video link: ")
        ydl_opts = {
            'format': 'best',
            'outtmpl': 'C:/music/%(title)s.%(ext)s',  # Save to C:/music folder
        }

        # Download video using youtube-dl
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            print(f"Downloading video: {link}")
            ydl.download([link])

        print("Download complete!")
        
        # Convert to MP3
        convert_to_mp3()

    except Exception as e:
        print(f"\nError downloading or converting: {str(e)}")

def convert_to_mp3():
    try:
        folder_path = r'C:/music/'
        file_type = r'\*mp4'
        files = glob.glob(folder_path + file_type)
        max_file = max(files, key=os.path.getctime)

        print(f"\nConverting {max_file} to MP3...")
        mp4_file = max_file
        mp3_file = mp4_file[:-4] + ".mp3"

        videoclip = VideoFileClip(mp4_file)
        audioclip = videoclip.audio
        audioclip.write_audiofile(mp3_file)

        audioclip.close()
        videoclip.close()

        print(f"Conversion completed: {mp3_file}")
    except Exception as e:
        print(f"\nError converting to MP3: {str(e)}")

# Main function
if __name__ == "__main__":
    welcome_message()
    download_video()
