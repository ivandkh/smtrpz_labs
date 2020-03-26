from cards import CardType
from register import Register
from uuid import UUID
import datetime

FARE = 8.0


class Turnstile():

    def __init__(self, reg: Register, id_: int, fare: int=FARE):
        self.reg = reg
        self.fare = fare
        self.id_ = id_

    def __call__(self, card_id: UUID) -> None:

        active, data, msg = self.reg.get_card_info(card_id)

        if active:
            isspecial = data['isspecial']
            success, msg = self.make_transaction(data)

        if not active or not success:
            self.forbid_passage(msg)
            self.reg.log.append((card_id, datetime.datetime.now(),
                                'Forbidded at turnstile #%d' % self.id_))
        else:
            if isspecial: self.special_passage_warn()
            self.allow_passage(msg)
            self.reg.log.append((card_id, datetime.datetime.now(),
                                'Allowed at turnstile #%d' % self.id_))

    def make_transaction(self, card: dict) -> (bool, str):
        success = False
        fare = self.fare
        if card['isspecial']:
            fare /= 2.0

        cardtype = card['type_']

        if cardtype == CardType.TimeLimit:
            success = datetime.datetime.now() < card['expiration']
            if success:
                msg = 'Active until %s' % card['expiration']
            else:
                msg = 'Card has expired.'

        elif cardtype == CardType.NumLimit:
            if card['numtravels'] > 0:
                card['numtravels'] -= 1
                success = True
                msg = '%d trevels left.' % card['numtravels']
            else:
                msg = '0 trevels left.'

        elif cardtype == CardType.BalanceLimit:
            if card['balance'] >= fare:
                card['balance'] -= fare
                success = True
                msg = '%.2f UAH left.' % card['balance']

            else:
                msg = 'Not enough money on the balance:%.2f UAH.' % card['balance']

        else:
            msg = "Cardtype `%s` is not supported!" % cardtype.name

        return success, msg

    def special_passage_warn(self) -> None:
        print('Special passage!')

    def allow_passage(self, msg: str) -> None:
        print('Passage allowed.\n' + msg)

    def forbid_passage(self, msg: str) -> None:
        print('Passage forbidden.\n' + msg)
