import abc
import collections
import itertools
import random

from .reaction import ReactionEvent


class VesselBase:
    """
    Abstract base class for an reaction vessel.

    Given an artificial chemistry, how should the possible reactions be explored?

    This should be implemented by subclass as an iterator, with each yield being a ReactionEvent object.
    """

    achem = None

    def __init__(self, achem):
        self.achem = achem

    # required for iteration
    def __iter__(self):
        return self

    @abc.abstractmethod
    def __next__(self):
        raise NotImplementedError


class VesselZip(VesselBase):
    # TODO type hints
    contents = []
    contents_next = []  # TODO use queue?
    zipped = []
    rng = None
    time = 0.0

    def __init__(self, achem, contents, rng, timeout=100):
        super(VesselZip, self).__init__(achem)
        self.contents_next = list(contents)
        self.rng = rng
        self.time = 0.0
        self.timeout = timeout
        self.__next_timestep()

    def __next_timestep(self):
        self.contents = self.contents_next
        self.contents_next = []
        self.rng.shuffle(self.contents)
        self.zipped = zip(*[iter(self.contents)] * 2)
        self.time += 1.0

    def __next__(self):
        timout_test = 0.0
        while timout_test < self.timeout:
            pair = next(self.zipped, None)
            if not pair:
                self.__next_timestep()
                pair = next(self.zipped)
                timout_test += 1

            reaction = self.achem.react(pair, self.rng)
            if reaction:
                self.contents_next.extend(reaction.products)
                reaction_event = ReactionEvent(reaction, self.time)
                return reaction_event
            else:
                # elastic collision move to next time step
                self.contents_next.extend(pair)
                # TODO loop not recursion
            print(self.contents)
        raise StopIteration


class VesselCombinatoric(VesselBase):
    """
    Generates every possible reaction but has no sense of time or conservation
    of mass or energy.

    """

    seen = []  # TODO use set?
    pending = []  # TODO use queue?
    # TODO limit pending size?

    def __init__(self, achem, contents):
        super(VesselCombinatoric, self).__init__(achem)
        self.seen = list(contents)
        self.pending = list(itertools.combinations_with_replacement(contents, 2))

    def __next__(self):
        if len(self.pending) == 0:
            raise StopIteration

        reactants = self.pending.pop()
        for reaction in self.achem.all_reactions(reactants):
            # if it wasn't an elastic reaction
            if reaction is not None:
                yield ReactionEvent(reaction, 0.0)
                # add any potential new reactants
                for product in reaction.products:
                    if product not in self.seen:
                        self.seen.append(product)
                        # this will include self reaction
                        self.pending.extend(itertools.product([product], self.seen))


# TODO implement VesselSingle as a one-at-a-time random vessel


# TODO implement Gillespie / Gibson-Bruck vessel
