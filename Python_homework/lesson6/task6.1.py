from time import sleep
from termcolor import colored

class Trafficlight:
    __color = ['красный', 'желтый', 'зеленый', 'желтый']

    def running(self):
        i = 0
        while i <= 3:
            a = Trafficlight.__color[i]
            print(f'Светофор переключается : ', end=' ')
            if i == 0:
                print(colored(a, 'red'))
                sleep(7)
            elif i == 1:
                print(colored(a, 'yellow'))
                sleep(2)
            elif i == 2:
                print(colored(a, 'green'))
                sleep(7)
            elif i == 3:
                print(colored(a, 'yellow'))
                sleep(2)
            i += 1


traffic = Trafficlight()
traffic.running()
