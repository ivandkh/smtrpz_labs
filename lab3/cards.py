from enum import Enum, auto
from uuid import uuid4
import datetime


class CardType(Enum):
    TimeLimit = auto()
    NumLimit = auto()
    BalanceLimit = auto()


class TimeDuration(Enum):
    OneDay = datetime.timedelta(days=1)
    OneWeek = datetime.timedelta(weeks=1)
    OneMonth = datetime.timedelta(days=30)


class CardBase():
    def __init__(self, type_: CardType, isspecial: bool=False):
        self.id = uuid4()
        self.type_ = type_
        self.isspecial = isspecial

    def __repr__(self):
        return self.type_.name + " card\n"


class TimeLimitCard(CardBase):
    def __init__(self, duration: TimeDuration, isspecial: bool=False):
        super().__init__(CardType.TimeLimit, isspecial)

        self.expiration = datetime.datetime.now() + duration.value


class NumLimitCard(CardBase):
    def __init__(self, numtravels: int, isspecial: bool=False):
        super().__init__(CardType.NumLimit, isspecial)

        self.numtravels = numtravels


class BalanceLimitCard(CardBase):
    def __init__(self, balance: float):
        super().__init__(CardType.BalanceLimit, False)

        self.balance = balance
