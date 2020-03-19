import abc
import random
import typing

from .reaction import Reaction

T = typing.TypeVar("T")


class AChem(typing.Generic[T], abc.ABC):
    """
    Abstract base class for an artificial chemistry.

    This includes the molecules and the rules governing their interactions
    """

    @abc.abstractmethod
    def react(self, molecules: typing.Iterable[T], rng: random.Random) -> Reaction[T]:
        """
        May be implemented by subclasses to enable simulation
        of reaction network.

        Elastic reactions return the reactants as the products.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def all_reactions(
        self, molecules: typing.Iterable[T]
    ) -> typing.Iterable[Reaction[T]]:
        """
        May be implemented by subclasses to enable enumeration
        of reaction network.
        """
        raise NotImplementedError
