import threading
import time


def thread_function(msg):
    for i in range(5):
        time.sleep(2)
        print(msg)


thread1 = threading.Thread(target=thread_function, args=("Thread 1",))
thread2 = threading.Thread(target=thread_function, args=("Thread 2",))

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("Fim do programa")
