import vehicles as v
from humans import Human, Policeman, Firefighter

if __name__ == '__main__':

    car1 = v.Vehicle[Policeman](5)
    car2 = v.Car[Firefighter](5)
    bus = v.Bus()
    taxi = v.Taxi(8)
    pcar = v.PoliceCar(5)
    ftruck = v.FireTruck(6)

    p1 = Policeman('Jhon')
    f1 = Firefighter('James')
    h1 = Human('Jack')

    car1.add_passenger(p1)
    car1.add_passenger(f1)

    car2.add_passenger(p1)
    car2.add_passenger(f1)

    bus.add_passenger(p1)
    bus.add_passenger(f1)
    bus.add_passenger(h1)

    taxi.add_passenger(h1)
    taxi.add_passenger(p1)

    pcar.add_passenger(h1)
    pcar.add_passenger(f1)

    ftruck.add_passenger(h1)
    ftruck.add_passenger(f1)

    taxi.drop_passenger(h1)
    ftruck.drop_passenger(f1)
