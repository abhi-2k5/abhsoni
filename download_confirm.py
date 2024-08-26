import requests
import os
import hashlib

file_id = '1D4yxUdJQfOWDZqhEwQEykRAjUT9iKcz8'
confirm = 't'
download_url = f"https://drive.google.com/uc?id={file_id}&confirm={confirm}"

# Ensure the directory exists
directory=r"C:\Users\abhsoni\PycharmProjects\Selenium"
if not os.path.exists(directory):
    os.makedirs(directory)
output_path = os.path.join(directory, 'star.png')


# Download the file from Google drive
def download_file_from_google_drive(download_url, output_path):

 try:
    response = requests.get(download_url, stream=True, allow_redirects=True)
    response.raise_for_status()

    # Write the file to disk
    with open(output_path, 'wb') as file:
        for chunk in response.iter_content(chunk_size=8192):
            file.write(chunk)

    print(f"File downloaded to {output_path}")
    return True

 except requests.exceptions.RequestException as e:
    print(f"Error downloading file: {e}")
    return False

#Verify the MD5Sum of file
def md5sum(filename):
    hash_md5 = hashlib.md5()
    with open(filename, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

if __name__ == "__main__":
        #download_file_from_google_drive(download_url, output_path)
        md5sum("star.png")