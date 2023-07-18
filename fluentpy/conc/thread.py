from concurrent.futures.thread import ThreadPoolExecutor
import threading
import requests
import time


thread_local = threading.local()


def get_session():
    if not hasattr(thread_local, 'session'):
        thread_local.session = requests.Session()

    return thread_local.session


def download_site(url):
    with thread_local.session.get(url) as response:
        print(f'Read {len(response.content)} from {url}')


def download_all_sites(sites):
    with ThreadPoolExecutor(max_workers=5) as executer:
        executer.map(download_site, sites)
