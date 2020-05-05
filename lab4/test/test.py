import pytest
from vehicles import Vehicle
from humans import Human


def test_maxseats():
    assert Vehicle[Human](10).maxseats() == 10


def test_takenseats():
    v1 = Vehicle[Human](10)
    for i in range(10):
        v1.add_passenger(Human('Name%d' % i))
    assert v1.takenseats() == 10


def test_add_passenger():
    v1 = Vehicle[Human](10)
    for i in range(10):
        v1.add_passenger(Human('Name%d' % i))

    with pytest.raises(Exception):
        v1.add_passenger(Human('Jhon'))


def test_drop_passenger():
    v1 = Vehicle[Human](10)
    h = [Human('Name%d' % i) for i in range(11)]
    map(lambda x: v1.add_passenger(x), h)
    map(lambda x: v1.drop_passenger(x), h)

    with pytest.raises(ValueError):
        v1.drop_passenger(Human('Jhon'))
