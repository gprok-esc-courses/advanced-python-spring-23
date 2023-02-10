from time import sleep, ctime
import random
import threading


def action(code):
    for i in range(10):
        print("ID" + str(code) + ", " + str(i))
        sleep(random.randint(2, 5))


if __name__ == '__main__':
    threads = []
    print("Starting at: ", ctime())
    for i in range(5):
        th = threading.Thread(target=action, args=(i,))
        threads.append(th)
        th.start()
    for th in threads:
        th.join()
    print("Ending at: ", ctime())