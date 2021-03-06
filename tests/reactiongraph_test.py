import itertools

import igraph
from pyachem.achemprime import AChemPrime
from pyachem.reactiongraph import ReactionGraph


def test_reactiongraph():
    reactiongraph = ReactionGraph(AChemPrime(), [2, 3, 4, 5, 6])

    reactions = frozenset(reactiongraph)
    assert len(reactions) == 3

    # layout = reactiongraph.graph.layout_kamada_kawai()
    # igraph.plot(reactiongraph.graph, layout = layout)
