import random
import typing

from .achembase import AChem
from .reaction import Reaction


class AChemPrime(AChem):
    """Example artificial chemistry based on prime numbers"""

    def react(
        self, molecules: typing.Iterable[int], rng: random.Random
    ) -> Reaction[int]:
        a, b = molecules
        # 50/50 chance to flip
        if rng.random() < 0.5:
            a, b = b, a

        if b == a or b % a:
            # same, or has a remainder, elastic reaction
            return None
        else:
            c = b // a
            return Reaction((a, b), (a, c))

    def all_reactions(
        self, molecules: typing.Iterable[int]
    ) -> typing.Iterable[Reaction[int]]:
        return super(AChemPrime, self).all_reactions(molecules)
