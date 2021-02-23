import time

class TrafficLight:
    _TrafficLight = 'Color'
    def running(self):
        print('red')
        time.sleep(7)
        print('yellow')
        time.sleep(2)
        print('green')
        time.sleep(7)

value_1 = TrafficLight()
print(value_1._TrafficLight)
value_1.running()