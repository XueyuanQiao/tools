# Importing the necessary module and function
from simple_image_download import simple_image_download as simp 
import sys

def download(k = ""):

    # Creating a response object
    response = simp.Downloader

    ## Keyword
    if not k:
        k = "Dog"

    # Downloading images
    try:
        response().download(k, 5)
        print("Images downloaded successfully.")
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    k = sys.argv[1]
    download(k)