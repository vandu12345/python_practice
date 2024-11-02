import threading
import time


def abc(test_value):
    a = test_value
    print(f"Hello: {a}")
    time.sleep(2)    

start_time = time.time()
# Create a thread
t1 = threading.Thread(target=abc, args=(2,), name="Thread1")
t2 = threading.Thread(target=abc, args=(3,), name="Thread2")
t3 = threading.Thread(target=abc, args=(4,), name="Thread3")



# Start the thread
t1.start()
t2.start()
t3.start()

# Main thread continues executing in parallel
print("Main thread continues running...")

# Wait for thread to finish
t1.join()
t2.join()
t3.join()

end_time = time.time()

print(f"Total time taken : {end_time - start_time} seconds")

