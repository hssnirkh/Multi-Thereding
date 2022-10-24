#mainThread
from threading import Thread,current_thread,main_thread
thread = current_thread()
print(thread.name,thread.daemon,thread.ident)
t = main_thread()
print(t.name,t.daemon,t.ident)