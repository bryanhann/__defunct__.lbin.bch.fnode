import pytest
from bch_node_lib.node import Node

def test_children(ROOT):
    assert len(list(ROOT.children())) == 2

def test_descendants(ROOT):
    assert len(list(ROOT.descendants(depth=0))) == 0
    assert len(list(ROOT.descendants(depth=1))) == 2
    assert len(list(ROOT.descendants(depth=2))) == 5
    assert len(list(ROOT.descendants(depth=3))) == 11

def test_nodes(NODES, tree):
    return
    for xx in NODES:
        print(xx.rel(tree))

def test_DICT(DICT,tree):
    #return
    for key in DICT:
        for node in DICT[key]:
            bch = node.bch()
            fpath = node.fpath(rel=tree)
            dpath = node.dpath(rel=tree)
            bpath = node.bpath(rel=tree)
            print( f"{key}: fpath={fpath}, dpath={dpath}, bpath={bpath}" )

def test_PLATTER_is_correct(PLATTER,ROOT):
    def same(node,name): assert str(node.path(rel=ROOT.path())) == name
    P=PLATTER
    same( P.A       , "A"                   )
    same( P.B       , "B"                   )
    same( P.fruit   , "A/fruit"             )
    same( P.apple   , "A/fruit/apple"       )
    same( P.banana  , "A/fruit/banana"      )
    same( P.animal  , "A/animal"            )
    same( P.insect  , "A/animal/insect"     )
    same( P.ant     , "A/animal/insect/ant" )
    same( P.bee     , "A/animal/insect/bee" )
    same( P.mammal  , "A/animal/mammal"     )
    same( P.ape     , "A/animal/mammal/ape" )
    same( P.bear    , "A/animal/mammal/bear")
    same( P.mythical, "A/mythical"          )
    same( P.unicorn , "A/mythical/unicorn"  )

