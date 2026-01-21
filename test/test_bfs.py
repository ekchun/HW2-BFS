# write tests for bfs
import pytest
from search import graph

def test_bfs_traversal():
    """
    TODO: Write your unit test for a breadth-first
    traversal here. Create an instance of your Graph class 
    using the 'tiny_network.adjlist' file and assert 
    that all nodes are being traversed (ie. returns 
    the right number of nodes, in the right order, etc.)
    """

    g = graph.Graph("data/tiny_network.adjlist")
    start = g.bfs("31806696")

    bfs_5 = [
        "31806696",
        "Luke Gilbert",
        "33483487",
        "31626775",
        "31540829"
    ]
    assert start[:5] == bfs_5 # check first 5 nodes in bfs traversal

    with pytest.raises(ValueError):
        g.bfs("fake_node123") # test for non-existent start; edge case 1 + use ValueError

def test_bfs():
    """
    TODO: Write your unit test for your breadth-first 
    search here. You should generate an instance of a Graph
    class using the 'citation_network.adjlist' file 
    and assert that nodes that are connected return 
    a (shortest) path between them.
    
    Include an additional test for nodes that are not connected 
    which should return None. 
    """
    g = graph.Graph("data/citation_network.adjlist")

    # (shortest) path between connected nodes
    path = g.bfs("34413319", "34968246")
    assert path[0] == "34413319"
    assert path[-1] == "34968246"
    assert len(path) >= 2
    assert path == ["34413319", "Nadav Ahituv", "34968246"]  # expected shortest path

    # no path between nodes, edge case 2
    neighbors = g.bfs("Charles Chiu")
    unreachable = None
    for node in g.graph.nodes:
        if node not in neighbors:
            unreachable = node
            break

    assert unreachable is not None
    assert g.bfs("Charles Chiu", unreachable) is None

    # test for non-existent end; edge case 3
    end = "fake_node123"
    assert end not in g.graph
    assert g.bfs("34413319", end) is None