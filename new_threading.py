import time
import concurrent.futures


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
    return f'Done Sleeping...{seconds}'


with concurrent.futures.ThreadPoolExecutor() as executor:
    secs = [5, 4, 3, 2, 1]
    results = [executor.submit(do_something, sec) for sec in secs]

    for f in concurrent.futures.as_completed(results):
        print(f.result())


# Stoping the timmer
finish = time.perf_counter()

# Printing out the results of the timmmer
print(f'Finished in {round(finish-start,2)} second(s)')
