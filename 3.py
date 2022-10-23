#custom thread class
from threading import Thread
from time import sleep

class customThread(Thread):
	#overwrite the run fuction
	def run(self):
		#block for moment
		sleep(1)
		#display
		print("this is coming from another thread")
#creat obj or instance
t = customThread()
#start the thread
t.start()
# wait for the thread to finish
print('Waiting for the thread to finish')
t.join()
