import os

import requests

# Get the Downloads folder path
downloads_folder = os.path.expanduser("./basit/")

# Ensure the Downloads folder exists
if not os.path.exists(downloads_folder):
    os.makedirs(downloads_folder)

# Base URL
base_url = "https://server7.mp3quran.net/basit/"

# Loop through i = 001 to 114
for i in range(1, 115):
    file_name = f"{i:03}.mp3"  # Format as 001, 002, ..., 114
    file_url = f"{base_url}{file_name}"
    file_path = os.path.join(downloads_folder, file_name)
    
    print(f"Downloading {file_name}...")
    response = requests.get(file_url, stream=True)
    
    if response.status_code == 200:
        with open(file_path, "wb") as file:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    file.write(chunk)
        print(f"Saved: {file_path}")
    else:
        print(f"Failed to download: {file_url}")

print("Download completed!")
