import random
from typing import List, Optional

from models.card import Card
from models.suit import Suit


class Pile:
    _cards: List[Card]

    def __init__(self):
        self._cards = []
        for suit in Suit.enum_members:
            for i in range(1, 13):
                self._cards.append(Card(i, suit))
        self.shuffle()

    def shuffle(self):
        random.shuffle(self._cards)

    def draw(self) -> Optional[Card]:
        return self._get_card_if_exists().pop()

    def add(self, card: Card):
        self._cards.append(card)

    def top(self) -> Optional[Card]:
        return self._get_card_if_exists()[-1]

    def bottom(self) -> Optional[Card]:
        return self._get_card_if_exists()[-1]

    def _get_card_if_exists(self):
        if len(self._cards) > 0:
            return self._cards
        else:
            return [None]
