import itertools

import igraph

from .reaction import Reaction
from .vessel import VesselCombinatoric


class ReactionGraph:
    def __init__(self, achem, initial):
        self.achem = achem
        self.vessel = VesselCombinatoric(achem, initial)
        self.graph = igraph.Graph(
            directed=True,
            vertex_attrs={"mol": [], "is_reaction": [], "is_molecule": [],},
            edge_attrs={"count": []},
        )

        for reaction in self.vessel:
            # create a new node for this reaction
            reaction_vertex = self.graph.add_vertex(is_reaction=True, is_molecule=False)
            # find or create nodes for reactant
            for reactant in reaction.reactants:
                reactant_vertexes = self.graph.vs.select(lambda v: reactant == v["mol"])
                if len(reactant_vertexes) == 0:
                    reactant_vertexes = [
                        self.graph.add_vertex(
                            is_reaction=False, is_molecule=True, mol=reactant
                        )
                    ]
                reactant_vertex = reactant_vertexes[0]

                # find or create edges from reactant to reaction
                reactant_edges = self.graph.es.select(
                    _from=reactant_vertex, _to=reaction_vertex
                )
                if len(reactant_edges) == 0:
                    reactant_edges = [
                        self.graph.add_edge(reactant_vertex, reaction_vertex, count=0)
                    ]
                reactant_edge = reactant_edges[0]
                reactant_edge["count"] += 1

            # find or create nodes for product
            for product in reaction.products:
                product_vertexes = self.graph.vs.select(lambda v: product == v["mol"])
                if len(product_vertexes) == 0:
                    product_vertexes = [
                        self.graph.add_vertex(
                            is_reaction=False, is_molecule=True, mol=product
                        )
                    ]
                product_vertex = product_vertexes[0]

                # find or create edges from product to reaction
                product_edges = self.graph.es.select(
                    _from=reaction_vertex, _to=product_vertex
                )
                if len(product_edges) == 0:
                    product_edges = [
                        self.graph.add_edge(reaction_vertex, product_vertex, count=0)
                    ]
                product_edge = product_edges[0]
                product_edge["count"] += 1
