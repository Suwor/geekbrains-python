from time import sleep
from itertools import cycle


class TrafficLight:
    setting = {'красный': 7, 'желтый': 2, 'зеленый': 5}

    def __init__(self):
        self.color = None  # бесполезный атрирбут и сама задача сформулированна очень криво

    def cycle_generator(self):
        for item in cycle(TrafficLight.setting):
            yield item

    def running(self):
        for el in self.cycle_generator():
            print(el)
            sleep(TrafficLight.setting[el])


traffic_light = TrafficLight()
traffic_light.running()
