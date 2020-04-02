from representative import Representative

class Cocycles:
    """Wrapper for co-cycles computed by ripser.
    
    Each cocycle is represented as a triple (start, end, value).
    
    The order of the cycles at level n+1 is reflected in the order of the
    barcodes at level n. To know when the k-th n+1-cycle has been
    introduced look at the end time of the k-th n-barcode.
    
    >>> c = Cocycles(cocycles, barcodes)
    <C-0, C-1> # there are co-cycles in dimension 0 and 1
    >>> c.C0
    [<Representative : 0-chain, free sum ...>, ...]
    >>> c.C1
    [<Representative : 1-chain, free sum ...>, ...]
    """
    def __init__(self, cocycles, barcodes):
        self._cocycles = cocycles
        self._barcodes = barcodes
    
    def __repr__(self):
        list_of_cocycles = ["C-{}".format(i) for i in range(len(self._cocycles))]
        return "<{}>".format(",".join(list_of_cocycles))
        
    def __len__(self):
        return len(self._cocycles)
    
    def __getattr__(self, name):
        if name.startswith('C'):
            n = int(name[1:], 10)
            return [Representative(r) for r in self._cocycles[n]]
        else:
            raise AttributeError("{} has no attribute '{}'".format(self.__class__name, attribute_name))
    
#    def __getitem__(self, key):
#        """
#        >>> c[n] #  get the co-cycles at dimension n
#        >>> c[n:t] # get the co-cycles at dimension n in the filtration F_t
#        """
#        # TODO : the semantics is not clear, I'm happy to have
#        #        the end time be the filtration time but I don't
#        #        see why I would want to filter also on the dimension
#        #        of a co-cycle
#        if isinstance(key, slice):
#            # given a slice we have a start and end
#            # value that represent the dimension we
#            # are interested in and the filtration time
#            dimension = key.start or len(self._cocycles)
#            # get all the barcodes up to `dimension` from the list
#            barcodes = np.concatenate(self._barcodes[:dimension])
#            # get all the co-cycles from dimension 1 to dimension+1
#            c = []
#            for level in self._cocycles[1:dimension+1]: # yes every level of our hierarchy has a list of co-cycles
#                for e in level:
#                    c.append(e)
#            cocycles = np.concatenate(c)
#            # just filter out all the barcodes that die after key.stop
#            wanted = barcodes[:,1] < key.stop
#            #print(barcodes, cocycles, wanted)
#            #print(barcodes.shape, cocycles.shape, wanted.shape)
#            return cocycles[wanted.T]
#        # with just one index `key` we are querying
#        # cocycles at leve `key`
#        return self._cocycles[key]
