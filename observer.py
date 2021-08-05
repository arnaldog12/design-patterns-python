from abc import abstractmethod
from time import sleep


# Publisher (Subject)
class WeatherData:
    def __init__(self, list_subscribers):
        self.list_subscribers = list_subscribers
        self.temperature = None
        self.humidity = None

    def notify(self):
        for subscriber in self.list_subscribers:
            subscriber.update(self)
        print()

    def new_data(self, temperature, humidity):
        self.temperature = temperature
        self.humidity = humidity
        self.notify()


# Observer Pattern
class Observer:
    @abstractmethod
    def update(self, weather_data):
        pass


# Observers
class DisplayObserver(Observer):
    def update(self, weather_data):
        print(f"Current Temperature: {weather_data.temperature}")
        print(f"   Current Humidity: {weather_data.humidity}")


class StatisticsObserver(Observer):
    def __init__(self):
        self.list_temperatures = []

    def update(self, weather_data):
        self.list_temperatures.append(weather_data.temperature)
        if len(self.list_temperatures) >= 3:
            avg_temp = sum(self.list_temperatures) / len(self.list_temperatures)
            print(f"Average Temperature: {avg_temp}")


list_observers = [DisplayObserver(), StatisticsObserver()]

data = WeatherData(list_observers)
sleep(2)
data.new_data(30, 60)

sleep(2)
data.new_data(33, 70)

sleep(2)
data.new_data(40, 20)

sleep(2)
data.list_subscribers.pop(0)
data.new_data(35, 80)
