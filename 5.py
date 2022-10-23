#input args outpot value with overwrite run
from threading import Thread
from time import sleep

class CustomThread(Thread):

    def run(self):
        sleep(1)
        print("message from run")
        self.value = 90

    def task(self,sleep_time,message):
        sleep(sleep_time)
        print(f"message frome task : {message}")

t = CustomThread()
t.start()
#vaghti input bgirim daghighan motevajeh mishim ke threaf run() baad az
#sleep 1s ejra mishe 
t.task(float(input("sleep_time: ")),input("message: "))
#main thread montazer mimoone ke input vared beshe 
print("message from main thread or out side of class ...")
#without join() t.value not work
#because it refer to main thread
t.join()
print(f"value is :{t.value}")