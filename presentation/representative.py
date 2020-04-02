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
    
    def project(self, distance, t):
        """Project the representative co-cycle on the filtration at time t.

        :param distance: distance function for two vertices
        :type distance: callable

        :param t: distance threshold
        :type t: float

        :return: projected co-cycle at time t
        :rettype: Representative

        Given a distance between our simplexes points
        and a threshold t we can can ask if the underlying row(s)
        describes a simplex that belongs to the
        filtration at time t.
        
        This can be done because we just ask if all the
        points in our simplex are distant less than t.
        
        Once we know if a simplex belongs to the filtration
        we can filter it out of the representative.
        """
        
        def close_enough(vertices, t=np.infty):
            """
            Returns true if the distance in the set of
            vertices is always less than t

            :param vertices: vertices in our n-cycle
            :type vertices: sequence

            :param t: threshold distance
            :type t: float
            """
            for i, vertex in enumerate(vertices):
                for other in vertices[i+1:]:
                    if not distance(vertex, other) <= t:
                        return False
            return True
                    
        (r,_) = self._rows.shape
        mask =  np.full(r, False, dtype=bool)
        for i, simplex in enumerate(self._rows):
            if close_enough(simplex[:-1], t):
                mask[i] = True
        if not any(mask):
            raise ValueError("The feature does not exist for time {}".format(t))
        # here we are copying the underlying values
        return Representative(self._rows[mask])
        
    def __str__(self):
        """
        The underlying row [a,b,c] is representing the
        chain c * <a|b>
        """
        r = [ "{}{}".format(row[-1], row[:-1]) for row in self._rows]
        return "+".join(r)
