import threading


def job1():
    global A
    for i in range(10):
        A += 1
        print('job1 A=', A)


def job2():
    global A
    for i in range(10):
        A += 10
        print('job2 A=', A)


if __name__ == '__main__':
    A = 0
    t1 = threading.Thread(target=job1)
    t2 = threading.Thread(target=job2)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
"""
job1 A= 1
job2 A= 11
job2 A= 21
job2 A= 31
job2 A= 41
job1 A= 42
job1 A= 43
job1 A= 44
job1 A= 45
job1 A= 46
job1 A= 47
job1 A= 48
job1 A= 49
job1 A= 50
job2 A= 60
job2 A= 70
job2 A= 80
job2 A= 90
job2 A= 100
job2 A= 110
"""