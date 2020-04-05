from abc import ABC, abstractmethod
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


class CardBase(ABC):
    def __init__(self, isspecial: bool=False):
        self.id = uuid4()
        self.type_ = type(self)
        self.isspecial = isspecial

    def __repr__(self):
        return self.type_.name + " card\n"

    @abstractmethod
    def make_transaction(self, fare: int) -> (bool, str):
        pass


class TimeLimitCard(CardBase):
    def __init__(self, duration: TimeDuration, isspecial: bool=False):
        super().__init__(isspecial)

        self.expiration = datetime.datetime.now() + duration.value

    def make_transaction(self, fare: int) -> (bool, str):
        success = success = datetime.datetime.now() < self.expiration
        if success:
                msg = 'Active until %s' % self.expiration
        else:
            msg = 'Card has expired.'

        return success, msg


class NumLimitCard(CardBase):
    def __init__(self, numtravels: int, isspecial: bool=False):
        super().__init__(isspecial)

        self.numtravels = numtravels

    def make_transaction(self, fare: int) -> (bool, str):
        if self.numtravels > 0:
                self.numtravels -= 1
                success = True
                msg = '%d trevels left.' % self.numtravels
        else:
            msg = '0 trevels left.'
            success = False

        return success, msg


class BalanceLimitCard(CardBase):
    def __init__(self, balance: float):
        super().__init__(False)

        self.balance = balance

    def make_transaction(self, fare: int) -> (bool, str):

        if self.balance >= fare:
                self.balance -= fare
                success = True
                msg = '%.2f UAH left.' % self.balance
        else:
            msg = 'Not enough money on the balance:%.2f UAH.' % self.balance
            success = False

        return success, msg

cards_types_mapping = {
    CardType.TimeLimit: TimeLimitCard,
    CardType.NumLimit: NumLimitCard,
    CardType.BalanceLimit: BalanceLimitCard,
    }
