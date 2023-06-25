# Website Change Detector

This Python script checks if the content of specified websites has changed since its last run. It sends GET requests to URLs, computes an MD5 hash of the webpage's content, and compares it with a previous hash if available. If the hashes differ, it prints a notification stating the URL of the changed website.

## Requirements

Before you run this script, you need to install the following Python packages:

- `requests`
- `beautifulsoup4`
- `hashlib`

You can install them using pip:

```sh
pip install requests beautifulsoup4
```

Please note that `hashlib` is part of the Python Standard Library, so it doesn't need to be installed separately.

## Usage

The script expects a list of URLs to be checked. These URLs should be inserted in the `urls` list within the `if __name__ == "__main__":` section at the end of the script:

```python
if __name__ == "__main__":
    urls = ["https://www.example.com", "https://www.example2.com"]  # replace with your URLs
    for url in urls:
        main(url)
```

After updating the `urls` list, you can run the script with:

```sh
python script_name.py
```

Replace `script_name.py` with the name of the Python script.

## Functions

The script contains the following functions:

- `get_data(url: str) -> str`: Fetches the HTML content from the provided URL and returns it as a string.
- `compute_hash(data: str) -> str`: Computes an MD5 hash of the given data string.
- `get_old_hash(url: str) -> str or None`: Returns the previously computed hash for the given URL, if it exists. Otherwise, returns None.
- `store_new_hash(url: str, new_hash: str) -> None`: Stores the new computed hash for the given URL.
- `notify(url: str) -> None`: Prints a notification that the content of the specified URL has changed.
- `main(url: str) -> None`: Orchestrates the process for a single URL.

## Limitations

This script does not handle cases where the GET request to a URL fails. Also, it only considers changes in the textual content of the webpages. Changes in images, videos, scripts, or other non-textual content will not trigger a notification.

Moreover, this script will detect changes even if the changes are due to dynamic content or advertisements that are different on every page load.