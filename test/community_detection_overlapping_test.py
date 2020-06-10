import networkx as nx

from karateclub.community_detection.overlapping import EgoNetSplitter, NNSED, DANMF, MNMF, BigClam, SymmNMF

def test_egonet_splitter():
    """
    Test the Ego Net splitter procedure.
    """
    graph = nx.newman_watts_strogatz_graph(100, 5, 0.3)

    model = EgoNetSplitter()

    model.fit(graph)
    memberships = model.get_memberships()
    
    indices = [k for k, v in memberships.items()].sort()
    nodes = [node for node in graph.nodes()].sort()

    assert graph.number_of_nodes() == len(memberships)
    assert indices == nodes


def test_nnsed():
    """
    Test the NNSED procedure.
    """
    graph = nx.newman_watts_strogatz_graph(100, 5, 0.3)

    model = NNSED()

    model.fit(graph)
    memberships = model.get_memberships()
    
    indices = [k for k, v in memberships.items()].sort()
    nodes = [node for node in graph.nodes()].sort()

    assert graph.number_of_nodes() == len(memberships)
    assert indices == nodes

    embedding = model.get_embedding()

    assert embedding.shape[0] == graph.number_of_nodes()
    assert embedding.shape[1] == model.dimensions
