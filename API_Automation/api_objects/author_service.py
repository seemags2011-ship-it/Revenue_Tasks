import requests

BASE_URL = "https://openlibrary.org/authors/"

def get_author_details(author_id="OL1A"):
    """
    Fetch author details from OpenLibrary API.
    Returns a Response object.
    """
    url = f"{BASE_URL}{author_id}.json"
    response = requests.get(url, timeout=10)
    print(f"🔗 API called: {url} -> Status: {response.status_code}")
    return response
