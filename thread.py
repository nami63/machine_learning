import threading
import os

def printt():
    thread_name=threading.current_thread().name
    process_id=os.getpid()
    print(f"{thread_name},{process_id}")

def worker():
    printt()

threads=[]
for i in range(5):
    t=threading.Thread(target=worker,name=f"Thread-{i}")
    threads.append(t)
    t.start()
    t.join()

