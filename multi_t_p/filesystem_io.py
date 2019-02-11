import threading
from queue import Queue
import time
import shutil

lock = threading.Lock()
def copy(data):
	with lock:
		print("Starting thread: {}".format(threading.current_thread().name))

	local_data = threading.local()
	local_data.ip, local_data.op = next(iter(data.items()))

	shutil.copy(local_data.ip, local_data.op)

	with lock:
		print("Finished thread: {}".format(threading.current_thread().name))

def process():
	while True:
		file_data = file_q.get()
		if file_data is None:
			break
		copy(file_data)
		file_q.task_done()

file_q = Queue()
num_worker_threads = 2
files = [{'example1.mp4': 'example11.mp4'},{'example2.mp4': 'example22.mp4'}]
threads = []

for _ in range(num_worker_threads):
	t = threading.Thread(target=process)
	t.start()
	threads.append(t)

start = time.time()

for file_data in files:
	file_q.put(file_data)

file_q.join()

print("Execution time = {0:.5f}".format(time.time() - start))

for _ in range(num_worker_threads):
	file_q.put(None)
for t in threads:
	t.join()
