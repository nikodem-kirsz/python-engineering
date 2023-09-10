"""
Event Handling: Implement event-driven systems where multiple components need to respond
to events (e.g., user interface elements reacting to user interactions).

Stock Market: Notify multiple subscribers (investors) about changes in stock prices 
when they occur.
"""
from abc import ABC, abstractmethod

# Observer interface
class Observer(ABC):
    @abstractmethod
    def update(self, news):
        pass

# Concrete observer classes (subscribers)
class Subscriber(Observer):
    def __init__(self, name):
        self.name = name

    def update(self, news):
        print(f"{self.name} received news: {news}")

# Subject (publisher) class
class NewsAgency:
    def __init__(self):
        self._observers = []

    def add_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

    def notify_observers(self, news):
        for observer in self._observers:
            observer.update(news)

    def publish_news(self, news):
        print(f"News Agency publishes: {news}")
        self.notify_observers(news)

# Client code
news_agency = NewsAgency()

subscriber1 = Subscriber("Subscriber 1")
subscriber2 = Subscriber("Subscriber 2")
subscriber3 = Subscriber("Subscriber 3")

news_agency.add_observer(subscriber1)
news_agency.add_observer(subscriber2)
news_agency.add_observer(subscriber3)

news_agency.publish_news("Breaking news: COVID-19 vaccine rollout begins")
