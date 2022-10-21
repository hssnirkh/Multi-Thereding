#function with arguments
#a custom function that blockes for moment

from threading import Thread
from time import sleep
#custom function that block and has argument
def task(sleep_time,message):
	#block a moment
	sleep(sleep_time)
	#display a message
	print(message)
#creat thred with args
t=Thread(target=task, args=(1.5,"new message from another thread"))
#start thread
t.start()
# wait for the thread to finish
print('Waiting for the thread...')
t.join()
