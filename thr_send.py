import time
import math
import threading


def do_something(num, returns, ret_idx):
    print(f'[Thread {num}]')
    time.sleep(5)
    result = num**2
    returns[ret_idx] = result


def main():
    num_of_thread = 2
    task = [i for i in range(5)]
    batch_of_thread = math.ceil(len(task)/num_of_thread)
    
    print(f'Task : {task}')

    for batch in range(batch_of_thread):
        print(f'[Batch {batch+1}/{batch_of_thread}]')

        threads = []
        returns = [None] * num_of_thread
        idx_start, idx_end = batch*num_of_thread, (batch+1)*num_of_thread
        if idx_end > len(task):
            idx_end = len(task)



        for thread_idx, idx in enumerate(range(idx_start, idx_end)):
            print(f'Current thread {idx}')
            threads.append(threading.Thread(target=do_something, args=(idx,returns,thread_idx)))
            threads[thread_idx].start()
            time.sleep(1)
            


        for t in threads:
            res = t.join()
        print(returns)

if __name__ == '__main__':
    main()