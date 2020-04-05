from cards import CardType, cards_types_mapping
from uuid import UUID


class Register():

    def __init__(self, name: str=''):
        self.name = name
        self.cardsID = {}
        self.banned = {}

        self.log = []

        print("Register '%s' created." % name)

    def create_card(self, cardtype: CardType, *args, **kwargs):
        try:
            newcard = cards_types_mapping[cardtype](*args, **kwargs)
        except KeyError:
            raise TypeError("Cardtype `%s` is not supported!" % cardtype.name)

        self.cardsID[newcard.id] = newcard
        return newcard

    def get_card_info(self, card_id: UUID) -> (bool,  str):

        try:
            if card_id in self.banned .keys():
                return False,  'This card was banned.\n %s' % \
                                  getattr(self.banned[card_id], 'description')

            return True,  ''
        except KeyError:
            return False, 'Card not found.'

    def ban_card(self, card_id: UUID, description: str='') -> None:
        card = self.cardsID.pop(card_id)
        card.description = description
        self.banned[card_id] = card
