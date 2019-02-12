import threading


def job1():
    global A, lock
    lock.acquire()
    for i in range(10):
        A += 1
        print('job1 A=', A)
    lock.release()


def job2():
    global A, lock
    lock.acquire()
    for i in range(10):
        A += 10
        print('job2 A=', A)
    lock.release()


if __name__ == '__main__':
    lock = threading.Lock()
    A = 0
    t1 = threading.Thread(target=job1)
    t2 = threading.Thread(target=job2)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
"""
job1 A= 1
job1 A= 2
job1 A= 3
job1 A= 4
job1 A= 5
job1 A= 6
job1 A= 7
job1 A= 8
job1 A= 9
job1 A= 10
job2 A= 20
job2 A= 30
job2 A= 40
job2 A= 50
job2 A= 60
job2 A= 70
job2 A= 80
job2 A= 90
job2 A= 100
job2 A= 110
"""