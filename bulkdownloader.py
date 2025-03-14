import os
import requests

downloads_folder = os.path.expanduser("./juzwise/")

# Ensure the Downloads folder exists
if not os.path.exists(downloads_folder):
    os.makedirs(downloads_folder)

base_url = "https://www.imamhussainresearch.com/audio/Quran/para_number_"


# Loop through i = 01 to 30
for i in range(1, 31):
    file_name = f"{i:02}.mp3"  # Format as 01, 02, ..., 30
    file_url = f"{base_url}{file_name}"

    file_path = os.path.join(downloads_folder, file_name)
    
    print(file_url)
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