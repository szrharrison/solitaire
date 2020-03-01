from typing import Optional

from models.suit import Suit


class Card:
    suit: Optional[Suit]
    number: int
    face_up: bool

    def __init__(self, number: int, suit: Suit = None):
        self.number = number
        self.suit = suit
        self.face_up = False

    def flip(self):
        self.face_up = not self.face_up

    def __eq__(self, other) -> bool:
        if isinstance(other, Card):
            if other.number == self.number and other.suit == self.suit:
                return True
            else:
                return False
        else:
            return False
