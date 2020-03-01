from typing import Iterable, Set, Union

from models.card import Card


class CardSet:
    _cards = Set[Card]

    def __init__(self, *cards: Card):
        if len(cards) > 0:
            self._cards = {*cards}
        else:
            self._cards = set()

    def __add__(self, other: Union[Card, Iterable[Card], 'CardSet']) -> 'CardSet':
        try:
            iter(other)
        except TypeError:
            if isinstance(other, Card):
                self._cards.add(other)
            elif isinstance(other, CardSet):
                self._cards.union(other._cards)
            else:
                raise NotImplemented
        else:
            self._cards.union(other)

        return self

    def __radd__(self, other: Union[Card, Iterable[Card], 'CardSet']) -> 'CardSet':
        return self.__add__(other)

    def has(self, card: Card) -> bool:
        return card in self._cards
