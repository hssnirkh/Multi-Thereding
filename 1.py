#first example
#a custom function that blocked for a moment
from time import sleep
from threading import Thread

def task():
	#block for moment
	sleep(1)
	#display
	print("this is first thread")

#creating a thread
thread = Thread(target=task)
#run the threaf
thread.start()
# wait for the thread to finish
print('Waiting for the thread...')
thread.join()
