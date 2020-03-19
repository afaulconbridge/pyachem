import functools
import typing

T = typing.TypeVar("T")


@functools.total_ordering
class Reaction(typing.Generic[T]):
    # TODO use __new__ and weakref to prevent duplicates
    # see https://docs.python.org/3/reference/datamodel.html#object.__new__
    # see https://docs.python.org/3/library/weakref.html#weakref.WeakValueDictionary
    # TODO implement comparisons
    # TODO implement hash
    reactants = ()
    products = ()
    rate = 1.0

    def __init__(
        self,
        reactants: typing.Iterable[T],
        products: typing.Iterable[T],
        rate: float = 1.0,
    ):
        self.reactants = tuple(sorted(reactants))
        self.products = tuple(sorted(products))
        self.rate = rate

    def __repr__(self):
        return f"Reaction({self.reactants}, {self.products}, {self.rate})"

    def __eq__(self, other):
        if self is other:
            return True

        if self.reactants != other.reactants:
            return False
        if self.products != other.products:
            return False
        if self.rate != other.rate:
            return False

        # no problems, must be the same
        return True

    def __lt__(self, other):
        if self is other:
            return False

        if self.reactants < other.reactants:
            return True
        if self.products < other.products:
            return True
        if self.rate < other.rate:
            return True

        return False


@functools.total_ordering
class ReactionEvent(typing.Generic[T]):
    # TODO use __new__ and weakref to prevent duplicates
    # see https://docs.python.org/3/reference/datamodel.html#object.__new__
    # see https://docs.python.org/3/library/weakref.html#weakref.WeakValueDictionary
    # TODO implement comparisons
    # TODO implement hash
    reaction = None
    time = 0.0

    def __init__(self, reaction: Reaction[T], time: float):
        self.reaction = reaction
        self.time = time

    def __repr__(self):
        return f"ReactionEvent({self.reaction}, {self.time})"

    def __eq__(self, other):
        if self is other:
            return True

        if self.reaction != other.reaction:
            return False
        if self.time != other.time:
            return False

        # no problems, must be the same
        return True

    def __lt__(self, other):
        if self is other:
            return False

        if self.time < other.time:
            return True
        if self.reaction < other.reaction:
            return True

        return False
