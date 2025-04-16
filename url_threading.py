import threading
import requests
from concurrent.futures import ThreadPoolExecutor

def get_urls():
    with open("urls.txt") as file:
        urls = [line.strip() for line in file.readlines() if line.strip() ]
        return urls

def hit_url(url):
    try:
        response = requests.get(url)
        print(response)
    except requests.exceptions.RequestException as e:
        print(f"url--{url}---Error{e}")
def execute(urls):
    threads = []
    for url in urls:
        threads.append(threading.Thread(target=hit_url, args = (url,)))
    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

def execute_with_thread_pool(urls, max_thread=5):
    with ThreadPoolExecutor(max_workers=max_thread) as exector:
        exector.map(hit_url, urls)



if __name__  == "__main__":
    urls = get_urls()
    #execute(urls)
    execute_with_thread_pool(urls)