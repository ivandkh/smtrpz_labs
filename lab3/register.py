import cards
from cards import CardType
from uuid import UUID


class Register():

    def __init__(self, name: str=''):
        self.name = name
        self.cardsID = {}
        self.banned = {}

        self.log = []

        print("Register '%s' created." % name)

    def create_card(self, cardtype: CardType, *args, **kwargs):

        if cardtype is CardType.TimeLimit:
            newcard = cards.TimeLimitCard(*args, **kwargs)
        elif cardtype is CardType.NumLimit:
            newcard = cards.NumLimitCard(*args, **kwargs)
        elif cardtype is CardType.BalanceLimit:
            newcard = cards.BalanceLimitCard(*args, **kwargs)
        else:
            raise TypeError("Cardtype `%s` is not supported!" % cardtype.name)

        self.cardsID[newcard.id] = newcard
        return newcard

    def get_card_info(self, card_id: UUID) -> (bool, dict, str):

        try:
            if card_id in self.banned .keys():
                return False, {}, 'This card was banned.\n %s' % \
                                  getattr(self.banned[card_id], 'description')

            return True, self.cardsID[card_id].__dict__, ''
        except KeyError:
            return False, {}, 'Card not found.'

    def ban_card(self, card_id: UUID, description: str='') -> None:
        card = self.cardsID.pop(card_id)
        card.description = description
        self.banned[card_id] = card
