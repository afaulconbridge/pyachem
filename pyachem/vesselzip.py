import abc
import random

from .reaction import ReactionEvent


class VesselBase(abc.ABC):
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
    def __init__(self, achem, contents, rng):
        super(VesselZip, self).__init__(achem)
        self.contents = list(contents)
        self.rng = rng
        self.time = 0.0
        self.__next_timestep()

    def __next_timestep(self):
        self.rng.shuffle(self.contents)
        self.contents_next = []
        self.zipped = zip(*[iter(self.contents)] * 2)
        self.time += 1.0

    def __next__(self):
        pair = next(self.zipped, None)
        if not pair:
            self.__next_timestep()
            pair = next(self.zipped)

        reaction = self.achem.react(pair, self.rng)
        if reaction:
            self.contents_next.extend(reaction.products)
            reaction_event = ReactionEvent(reaction, self.time)
            return reaction_event
        else:
            # elastic collision move to next time step
            self.contents_next.extend(pair)
            # TODO loop not recursion
            return self.__next__()


# TODO implement VesselSingle as a one-at-a-time random vessel

# TODO implement Gillespie / Gibson-Bruck vessel
