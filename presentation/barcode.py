class Barcode:
    """Access barcode diagram information.
    
    Each barcode in the family encodes information
    about the liveness of an element of the co-homology group
    as [start, end].
    
    Every end time in a barcode at level n means that
    we have introduced a feature at level n+1 that
    links two features at level n.
    
    >>> b = Barcode(barcodes)
    <B-0, B-1> # two barcodes diagram are present
    >>> b.B0 # same as r.barcode[0]
    >>> b.B1 # same as r.barcode[1]
    >>> for diagram in b:
           ...
    """
    def __init__(self, barcodes):
        self._barcodes = barcodes
        
    def __repr__(self):
        list_of_barcodes = ["B-{}".format(i) for i in range(len(self._barcodes))]
        return "<{}>".format(",".join(list_of_barcodes))
    
    def __len__(self):
        return len(self._barcodes)
    
    def __getattr__(self, name):
        if not name.startswith('B'):
            raise AttributeError("Barcode names always starts with 'B'")
        n = int(name[1:], 10)
        return self._barcodes[n]
    
    def __getitem__(self, key):
        if type(key) != int:
            raise TypeError("Slices are not allowed when querying barcodes")
        return self._barcodes[key]
