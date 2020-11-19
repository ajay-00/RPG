import time
import threading


'''
This is used to track how long it takes
for the program to run
'''
start = time.perf_counter()

'''
This is a function that is just used to
illstrate a process taking place. In
this case the function is just waiting
for one second to pass by
*f strings are used to pass in variables
'''
def do_something(seconds):
    print(f'sleeping {seconds}  second(s)...')
    time.sleep(seconds)
    print('Done Sleeping...')

# This list is used to store the results of the threads
threads = []

'''
This for loop starts 10 different threads
and stores them in a list so they can be joined later.
*the underline is used in the for loop because it represents
a dummy variable which we do not use and is simply there
for the purpose of running the loop 10 times
'''
for _ in range(10):
    t = threading.Thread(target=do_something, args=[1.5])
    t.start()
    threads.append(t)
'''
In this for loop the threads are joined.
joining is the process of waiting for the threads
to end before they move onto the next process.
If we do not join the threads the completion time
will be wrong as the instructions will pass to the
stop clock before the threads are finsihed processing
'''
for thread in threads:
    thread.join()

# Stoping the timmer
finish = time.perf_counter()

# Printing out the results of the timmmer
print(f'Finished in {round(finish-start,2)} second(s)')
