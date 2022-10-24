from threading import Thread

thread = Thread(name="myThrad",daemon=True)
print(thread.name,thread.daemon)