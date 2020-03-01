from typing import List

from models.stack import Stack


class Foundation:
    stacks: List[Stack]

    def __init__(self, deck_count: int):
        i = 0
        self.piles = []
        while i < deck_count * 4:
            self.stacks[i] = Stack()
