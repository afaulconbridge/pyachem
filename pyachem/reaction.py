import functools
import typing

T = typing.TypeVar("T")


@functools.total_ordering
class Reaction(typing.Generic[T]):
    # TODO use __new__ and weakref to prevent duplicates
    # see https://docs.python.org/3/reference/datamodel.html#object.__new__
    # see https://docs.python.org/3/library/weakref.html#weakref.WeakValueDictionary
    reactants = ()
    products = ()
    rate = 1.0
    __hash = None  # store hash once calculated
    __key = ()  # store common key used for equality, ordering, hashing

    def __init__(
        self,
        reactants: typing.Iterable[T],
        products: typing.Iterable[T],
        rate: float = 1.0,
    ):
        self.reactants = tuple(sorted(reactants))
        self.products = tuple(sorted(products))
        self.rate = rate

        self.__key = (self.reactants, self.products, self.rate)

    def __repr__(self):
        return f"Reaction({self.reactants}, {self.products}, {self.rate})"

    def __eq__(self, other):
        if self is other:
            return True

        return self.__key == other.__key

    def __lt__(self, other):
        if self is other:
            return False

        return self.__key < other.__key

    def __hash__(self):
        if not self.__hash:
            self.__hash = hash(self.__key)

        return self.__hash


@functools.total_ordering
class ReactionEvent(typing.Generic[T]):
    # TODO use __new__ and weakref to prevent duplicates
    # see https://docs.python.org/3/reference/datamodel.html#object.__new__
    # see https://docs.python.org/3/library/weakref.html#weakref.WeakValueDictionary
    reaction = None
    time = 0.0
    __hash = None  # store hash once calculated
    __key = ()  # store common key used for equality, ordering, hashing

    def __init__(self, reaction: Reaction[T], time: float):
        self.reaction = reaction
        self.time = time

        self.__key = (self.time, self.reaction)

    def __repr__(self):
        return f"ReactionEvent({self.reaction}, {self.time})"

    def __eq__(self, other):
        if self is other:
            return True

        return self.__key == other.__key

    def __lt__(self, other):
        if self is other:
            return False

        return self.__key < other.__key

    def __hash__(self):
        if not self.__hash:
            self.__hash = hash(self.__key)

        return self.__hash
