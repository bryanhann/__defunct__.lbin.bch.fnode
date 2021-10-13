#!/usr/bin/env python3

from bch.node.constants import HOME, MOUNTS
from bch.node.class_node import Node


def mounted():
     for mount in MOUNTS:
         yield from (xx for xx in Node(mount).children() if xx.bpath)

def gather_all():
    for root in mounted():
        for node in root.gather():
            yield node


