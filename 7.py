#configure thread attributs
#such as name and daemon
from threading import Thread

thread = Thread()
print(f"name={thread.name},daemon={thread.daemon}")
thread.name = "MyThread"
thread.daemon = True
print(f"name={thread.name},daemon={thread.daemon}")
