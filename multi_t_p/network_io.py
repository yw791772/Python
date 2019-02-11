import threading
from queue import queue
import requests
import bs4
import time

lock = threading.Lock()
def get(url):
	with lock:
		print("Starting thread {}".format(threading.current_thread().name))
	res = requests.get(url)
	res.raise_for_status()

	page = b4.BeautifulSoup(res.text, "html.parser")
	title = page.select("title")[0].getText()

	with lock:
		print("{}".format(threading.current_thread().name))
		print("{}: {}".format(url, title))
		print("Finished fetching: {}".format(url))

def process():
	while True:
		url = url_q.get()
		if url is None:
			break
		get(url)
		url_q.task_done()

url_q = Queue()
urls = ["https://www.google.com", "https://www.yahoo.com", "https://baidu.com", "https://bing.com"]
num_of_workers = 4
threads = []

for _ in range(num_of_workers):
	t = threading.Thread(target=process)
	t.start()
	threads.append(t)

start = time.time()

for url in urls:
	url_q.put(url)

url_q.join()

print("Execution time = {0:.5f}".format(time.time() - start))

for _ in range(num_worker_threads):
	file_q.put(None)
for t in threads:
	t.join()