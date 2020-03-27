import itertools
import random

import pytest
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
    vessel = VesselZip(AChemPrime(), [2, 4], random.Random(42))
    reaction = next(vessel)
    assert reaction == ReactionEvent(Reaction((2, 4), (2, 2), 1.0), 1.0)


def test_vesselzip_terminate():
    vessel = VesselZip(AChemPrime(), [2, 2], random.Random(42))
    with pytest.raises(StopIteration):
        reaction = next(vessel)
