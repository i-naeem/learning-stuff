import requests
import time


def download_url(url, session):
    with session.get(url) as response:
        print(f'Read {len(response.content)} from {url}')


def download_all_sites(sites):
    with requests.Session() as session:
        for site in sites:
            download_url(site, session)


if __name__ == "__main__":
    sites = [
        "https://www.jython.org",
        "http://olympus.realpython.org/dice",
    ] * 10
    start_time = time.time()
    download_all_sites(sites)
    duration = time.time() - start_time
    print(f"Downloaded {len(sites)} in {duration} seconds")
