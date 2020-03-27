import random
import typing

from .achembase import AChem
from .reaction import Reaction


class AChemPrime(AChem):
    """Example artificial chemistry based on prime numbers"""

    def _react(self, a, b):
        if b == a or b % a:
            # same, or has a remainder, elastic reaction
            return None
        else:
            return b // a

    def react(
        self, molecules: typing.Iterable[int], rng: random.Random
    ) -> Reaction[int]:
        a, b = molecules
        # 50/50 chance to flip
        if rng.random() < 0.5:
            a, b = b, a

        c = self._react(a, b)
        if not c:
            return None
        else:
            return Reaction((a, b), (a, c))

    def all_reactions(
        self, molecules: typing.Iterable[int]
    ) -> typing.Iterable[Reaction[int]]:
        a, b = molecules
        reactants_all = [(a, b), (b, a)]
        reactions = []
        for reactants in reactants_all:
            a, b = reactants
            c = self._react(a, b)
            if c:
                reactions.append(Reaction((a, b), (a, c)))
        return reactions
