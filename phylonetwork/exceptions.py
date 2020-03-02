class MalformedNewickException(Exception):
    """
    Raised when creating a new network from a malformed eNewick string.
    """
    pass

class TaxaException(Exception):
    """
    Raised when trying to compare to networks with incompatible Taxa.
    """
    pass


class NotAPhylogeneticNetwork(Exception):
    """
    Raised when the graph is not a Phylogenetic Network
    """
    pass
