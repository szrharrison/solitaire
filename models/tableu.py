from typing import List

from models.stack import Stack


class Tableu:
    stacks: List[Stack]

    def __init__(self, *stacks: Stack):
        self.stacks = list(stacks)
