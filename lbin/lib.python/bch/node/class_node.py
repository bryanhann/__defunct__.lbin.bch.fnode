#!/usr/bin/env python3
from pathlib import Path

from bch.node.util import _isdir, mod4path

class Node:
    def gather(self):
        yield self
        for xx in self.more():
            yield xx
    def more(self):
        try: self.pymod.more
        except AttributeError: return None
        for path in self.pymod.more:
            yield Node(path)
            yield from (xx for xx in Node(path).more())
    def __init__(self,path):
        self._path = Path(path)
        self.base = None
    def __repr__(self):
        if self.base:
            path=self.path.relative_to(self.base)
            base='.../'
        else:
            path=self.path
            base=''
        path=str(path)
        name=self.__class__.__name__
        return f'<{name}:{base}{path}>'
        return f'<{self.__class__name}:{str(self.path())}>'

    @property
    def bch(self): return self.__class__(self.path/'.bch')

    @property
    def path(self): return self._path

    @property
    def base(self): return self._base

    @base.setter
    def base(self,val): self._base = val

    @property
    def dpath(self): return _isdir(self.path) and self.path   or None

    @property
    def fpath(self): return self.path.is_file() and self.path   or None

    @property
    def parent(self): return Node(self.path.parent)

    @property
    def parents(self):
        path=self.path
        acc=[]
        while not str(path)==str(path.parent):
            acc.append(path)
            path=path.parent
        acc.append(path)
        return [Node(x) for x in acc]

    @property
    def bpath (self): return self.bch.dpath

    def children(self):
        for child in self.path.glob('*'):
            yield Node(child)

    def descendants(self,depth=-1,test=lambda x:True):
        if test(self):
            yield self
            if not depth==0:
                for child in self.children():
                    yield from child.descendants(depth=depth-1, test=test)
    #def legacy(self,depth=-1,test=lambda x:True):
    #    yiel
    @property
    def pymod(self):
        path=self.path/'.bch'/'register.py'
        if not path.is_file():
            return None
        else:
            return mod4path(path)



