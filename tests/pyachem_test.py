import itertools
import random

from pyachem import Reaction, ReactionEvent, VesselZip
from pyachem.achemprime import AChemPrime


def test_reactions():
    achem = AChemPrime()
    reaction = achem.react((2, 4), random.Random(42))
    print(reaction.products)
    assert reaction.products == (2, 2)
    assert reaction.reactants == (2, 4)
    assert reaction.rate == 1.0


def test_vesselzip():
    achem = AChemPrime()
    vessel = VesselZip(achem, range(2, 5 + 1), random.Random(42))
    reaction = next(vessel)
    assert reaction == ReactionEvent(Reaction((3, 4), (3, 4), 1.0), 1.0)
