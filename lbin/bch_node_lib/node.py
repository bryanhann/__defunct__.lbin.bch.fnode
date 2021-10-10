#!/usr/bin/env python3

import sys
import os
from pathlib import Path
from pprint import pprint

class Node:
    def __init__(self,path,base=None):
        self._path = path
    def bch   (self):           return self.__class__(self.path()/'.bch')
    def rel   (self, other):    return self.path().relative_to(other)
    def path  (self, rel=None): return rel and self._path.relative_to(rel) or self._path
    def dpath (self, rel=None): return self.path().is_dir()  and self.path(rel=rel)         or None
    def fpath (self, rel=None): return self.path().is_file() and self.path(rel=rel)         or None
    def bpath (self, rel=None): return self.bch().dpath()    and self.bch().dpath(rel=rel)  or None
    def __repr__(self):         return f'<{self.__class__name}:{str(self.path())}>'

    def children(self):
        for child in self.path().glob('*'):
            yield Node(child)
    def descendants(self,depth=-1,skip=lambda x:False):
        if depth==0 or skip(self):
            return
        for child in self.children():
            yield child
            yield from child.descendants(depth-1)


