from time import sleep, ctime
import random


def action(code):
    for i in range(10):
        print("ID" + str(code) + ", " + str(i))
        sleep(random.randint(2, 5))


if __name__ == '__main__':
    print("Starting at: ", ctime())
    for i in range(5):
        action(i)
    print("Ending at: ", ctime())