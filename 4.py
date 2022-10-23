#Example of Extending the Thread Class and Returning Values
from threading import Thread
from time import sleep

class customThread(Thread):
	#overwite run()
	def run(self):
		#block for moment
		sleep(1)
		#display from new thred not main thread
		print("this is coming from another thread")
		#store return value
		self.value = 99
#creat instance from 
thread = customThread()
# start() to call run()
thread.start()
#wait for thread to finish
print("out of thread waiting .....")
thread.join()
#get the value return from run
value = thread.value
print(f"got:{value}")
print(value)

