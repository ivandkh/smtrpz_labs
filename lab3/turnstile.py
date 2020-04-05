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

        active, msg = self.reg.get_card_info(card_id)

        if active:
            card = self.reg.cardsID[card_id]
            isspecial = card.isspecial
            success, msg = card.make_transaction(self.fare)

        if not active or not success:
            self.forbid_passage(msg)
            self.reg.log.append((card_id, datetime.datetime.now(),
                                'Forbidded at turnstile #%d' % self.id_))
        else:
            if isspecial: self.special_passage_warn()
            self.allow_passage(msg)
            self.reg.log.append((card_id, datetime.datetime.now(),
                                'Allowed at turnstile #%d' % self.id_))

    def special_passage_warn(self) -> None:
        print('Special passage!')

    def allow_passage(self, msg: str) -> None:
        print('Passage allowed.\n' + msg)

    def forbid_passage(self, msg: str) -> None:
        print('Passage forbidden.\n' + msg)
