from typing import Generic, TypeVar, List
from humans import Human, Policeman, Firefighter

T = TypeVar('T')
Z = TypeVar('Z')


class Vehicle(Generic[T]):

    _maxseats: int
    passengers: List[T]

    def __init__(self, maxseats: int):
        self._maxseats = maxseats
        self.passengers = []

    def maxseats(self) -> int:
        return self._maxseats

    def takenseats(self) -> int:
        return len(self.passengers)

    def add_passenger(self, passenger: T) -> None:
        print(self)
        print(self, )
        if self.takenseats() < self._maxseats:
            self.passengers.append(passenger)
        else:
            raise Exception('No free seats.')

    def drop_passenger(self, passenger: T) -> None:
        try:
            self.passengers.remove(passenger)
        except ValueError:
            raise ValueError("Passenger %s not in %s." % (passenger, self))


class Car(Vehicle[T]):
    pass


class Taxi(Car[Human]):
    pass


class PoliceCar(Car[Policeman]):
    pass


class FireTruck(Car[Firefighter]):
    pass


class Bus(Vehicle):

    def __init__(self, maxseats: int=30):
        super().__init__(maxseats)
