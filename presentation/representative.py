import numpy as np

class Representative:
    """Representation of a representative co-cycle.

    A n-co-chain is modelled as an array with n+1 columns.
    
    Every row is a n-simplex and the first n columns are the
    unique identifiers of our vertices, the last column in
    the coefficent in the field we are doing naughty things in.
    """
    def __init__(self, rows, p=None):
        self._rows = rows
        self.p = p
        
    def __repr__(self):
        """
        We don't want to see an array of values. It's good enough
        that we can see the dimension we are chaining things in.
        """
        chain_elements = len(self._rows)
        simplex_dimension = len(self._rows[0]) - 2
        return "<Representative : {}-chain, free sum of {} elements>".format(simplex_dimension, chain_elements)
    
    def __str__(self):
        """
        The underlying row [a,b,c] is representing the
        chain c * <a|b>
        """
        r = [ "{}{}".format(row[-1], row[:-1]) for row in self._rows]
        return "+".join(r)
