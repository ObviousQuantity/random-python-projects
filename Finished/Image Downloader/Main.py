import requests
import validators

def download_files(url):
    local_filename = url.split("/")[-1]
    with requests.get(url,stream=True) as r:
        print("Downloading...")
        with open("C:/Users/Admin/OneDrive/Desktop/"+local_filename,"wb") as f:
            print("Writing data to file")
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    f.close()
    print("Download complete")
    print("File saved as "+local_filename)

while 1:
    print("Welcome to image downloader")
    image_url = input(str("Image url: "))
    valid = validators.url(image_url)
    if valid == True:
        download_files(image_url)
    else:
        print("Invalid url")
    print("")