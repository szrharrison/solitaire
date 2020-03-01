from typing import List, Iterable, Union

from models.card import Card
from models.card_set import CardSet


class Stack:
    _cards: List[Card]
    _accepts: CardSet

    def __init__(self):
        self._cards = []
        self._accepts = CardSet()

    @property
    def accepts(self) -> CardSet:
        return self._accepts

    @accepts.setter
    def accepts(self, value: Union[Card, Iterable[Card], CardSet]):
        try:
            iter(value)
        except TypeError:
            if isinstance(value, Card):
                self._accepts = CardSet(value)
            elif isinstance(value, CardSet):
                self._accepts = value
            else:
                raise NotImplemented
        else:
            self._accepts = CardSet(*value)

    def add(self, card: Card):
        if self.accepts.has(card):
            self._cards.append(card)
        else:
            raise ValueError(f"Stack does not accept card: {card}")
