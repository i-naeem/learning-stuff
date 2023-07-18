import multiprocessing
import requests

session: requests.Session = None


def set_global_session():
    global session
    if not session:
        session = requests.Session()


def download_site(url):
    with session.get(url) as response:
        pn = multiprocessing.current_process().name
        print(f'{pn}: Read {len(response.content)} from {url}')


def download_all_sites(sites):
    with multiprocessing.Pool(initializer=set_global_session) as pool:
        pool.map(download_site, sites)
