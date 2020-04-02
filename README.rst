=====================================
Topological data analysis assignments
=====================================

This repo contains two things, the first is a python package
to interface with the results provided by ripser.

Installing the package will make some things easier to see
as the bindings to ripser are good but they are not easy
to play with. Wrapping the result in some presentation classes
is a common exercise in P vs NP.

You can install the package using::

        python setup.py install

Then the package will be available for use in your environment.

>>> from presentation.result import RipserResult
>>> result = ripser(X, ...)
>>> r = RipserResult(X, result)

From there there are some attributes you can explore

>>> r.diagrams # recover the list of diagrams
<B-0, B-1> # we have two diagrams!
>>> r.cohomology # and two co-homology groups
<CoHomology groups: coH0, coH1>

and a sane way to recover data

>>> r.diagrams.B0 # alternatively r.diagrams[0]
array[[start,end], ...]
>>> r.diagrams.B1 # alternatively r.diagrams[1]
array[[start,end], ...]

>>> r.cocycles.C0 # alternatively r.cocycles[0]
[<Representative : 0-chain, free sum of n elements>, ...]
>>> r.cocycles.C1 # alternatively r.cocycles[1]
[<Representative : 1-chain, free sum of m elements>, ...]

And if you really care about a representative element before plotting it
you can always print out the algebraic representation with `str`

>>> c = r.cocycles.C1[0]
>>> c
<Representative : 1-chain, free sum of 2 elements>
>>> str(c)
"1[18 17] + 1[9 10]"
