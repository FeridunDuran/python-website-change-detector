import hashlib
from urllib.parse import urlparse
import requests
from bs4 import BeautifulSoup
import os

def get_data(url):
    """
    This function takes a URL as input, sends a GET request to the URL using the requests 
    library, and extracts the text content of the HTML response using BeautifulSoup. It 
    returns the extracted text as a string.

    :param url: A string representing the URL to be scraped.
    :return: A string containing the text content of the HTML response.
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # extract the data you're interested in
    data = soup.get_text()
    return data

def compute_hash(data):
    """
    Computes the MD5 hash of the given data.

    :param data: A string representing the data to be hashed.
    :type data: str
    :return: A string representing the hexadecimal digest of the MD5 hash.
    :rtype: str
    """
    return hashlib.md5(data.encode('utf-8')).hexdigest()

def get_old_hash(url):
    """
    Given a URL, this function computes the MD5 hash of the URL and looks for a file with the name of the hash.
    If the file exists, it reads the contents of the file and returns them.
    If the file does not exist, it returns None.
    
    Args:
    - url (str): The URL to compute the MD5 hash of.
    
    Returns:
    - str or None: The contents of the file with the name of the MD5 hash of the URL, or None if the file does not exist.
    """
    hash_file = hashlib.md5(url.encode('utf-8')).hexdigest() + ".txt"
    if os.path.exists(hash_file):
        with open(hash_file, 'r') as file:
            old_hash = file.read()
        return old_hash
    else:
        return None

def store_new_hash(url, new_hash):
    """
    Stores a new hash in a text file with the name generated from the md5 hash of the given url.
    
    :param url: The url to hash and use as part of the filename.
    :type url: str
    
    :param new_hash: The hash to store in the text file.
    :type new_hash: str
    
    :return: None
    """
    hash_file = hashlib.md5(url.encode('utf-8')).hexdigest() + ".txt"
    with open(hash_file, 'w') as file:
        file.write(new_hash)

def notify(url):
    """Prints a message indicating that the specified website URL has changed."""
    print(f'Website {url} has CHANGED')

def main(url):
    old_hash = get_old_hash(url)
    new_data = get_data(url)
    new_hash = compute_hash(new_data)

    if old_hash is not None and old_hash != new_hash:
        notify(url)
    
    if old_hash is not None and old_hash == new_hash:
        """Prints a message indicating that the specified website URL has NOT changed."""
        print(f'{urlparse(url).netloc} has NOT CHANGED')

    store_new_hash(url, new_hash)

if __name__ == "__main__":
    urls = ["https://www.example.com", "https://www.example2.com"]  # replace with your URLs
    for url in urls:
        main(url)
