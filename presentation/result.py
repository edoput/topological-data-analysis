from .cocycle import Cocycles
from .cohomology import CoHomology
from .barcode import Barcode

class RipserResult(object):
    """Wrapped for the results returned by ripser.

    A python(ic) interface to the result returned by ripser.
    """
    _mappings = {
        'distances': 'dperm2all',
    }
    
    def __init__(self, points, result):
        self._points = points
        self._result = result

    @property
    def cohomology(self):
        """Access information about the cohomology computed.

        >>> result = ripser(X, ...)
        >>> r = RipserResult(X, result)
        >>> r.cohomology
        <<CoHomology groups: coH-0, co-H1> # two co-homology groups have been computed
        """
        return CoHomology(self._points, self._result['dgms'], self._result['cocycles'][:])
    
    @property
    def diagrams(self):
        """
        Access information about the barcode diagrams.

        >>> result = ripser(X, ...)
        >>> r = RipserResult(X, result)
        >>> r.diagrams
        """
        return Barcode(self._result['dgms'])
    
    @property
    def cocycles(self):
        """
        """
        return Cocycles(self._result['cocycles'], self._result['dgms'])
    
    def __getattr__(self, attribute_name):
        if attribute_name in self._mappings.keys():
            underlying = self._mappings[attribute_name]
            return self._result[underlying]
        if attribute_name in self._result.keys():
            return self._result[attribute_name]
        raise AttributeError("{} has no attribute '{}'".format(self.__class__.__name__, attribute_name))
        
        
    def __repr__(self):
        return "<{}>".format(self.__class__.__name__)
