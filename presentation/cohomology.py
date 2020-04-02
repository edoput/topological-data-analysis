class CoHomology:
    """Wrapper for the co-homology information returned by ripser.

    >>> c = CoHomology(data, barcodes, cocycles)
    <CoHomology groups: coH0, coH1>
    >>> c[1.5] # returns the representatives at time 1.5
    [ [array[...]], [array[...]]] # two representatives, one at dimension 0 and one at dimension 1
    """
    def __init__(self, points, barcodes, cocycles):
        self._points = points
        self._barcodes = barcodes
        self._cocycles = cocycles
        self._cocycles[0] = points # not sure about this, the order of barcodes and points might differ
        
    def __repr__(self):
        list_of_cohomology = ["coH-{}".format(i) for i in range(len(self._barcodes))]
        return "<CoHomology groups: {}>".format(", ".join(list_of_cohomology))

    def __getitem__(self, time):
        """Return the co-homology for our dataset at time t.
        
        This will return for every dimension n in our barcode
        the list of n-cocycles that are representative of a
        class in co-homology.
        """
        filtered_cohomology = []
        for (barcodes, representatives) in zip(self._barcodes, self._cocycles):
            merged = barcodes[:,1] < time
            filtered_cohomology.append(representatives[~merged])
            
        return filtered_cohomology
