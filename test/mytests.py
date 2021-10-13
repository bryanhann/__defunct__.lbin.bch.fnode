import pytest
from bch.node.class_node import Node

def test_children(ROOT):
    assert len(list(ROOT.children())) == 2

def test_descendants(ROOT):
    assert len(list(ROOT.descendants(depth=0))) == 1
    assert len(list(ROOT.descendants(depth=1))) == 3
    assert len(list(ROOT.descendants(depth=2))) == 6
    assert len(list(ROOT.descendants(depth=3))) == 12

def test_nodes(NODES, tree):
    return
    for xx in NODES:
        print(xx.rel(tree))


def rel(path, rel):
    if path is None: return None
    else: return path.relative_to(rel)
def test_DICT(DICT,tree,ROOT):
    #return
    for key in DICT:
        for node in DICT[key]:
            bch = node.bch
            _dpath=rel(node.dpath, tree)
            _fpath=rel(node.fpath, tree)
            _bpath=rel(node.bpath, tree)
            #_fpath=rel(node.fpath(), tree)
            #_bpath=rel(node.bpath(), tree)
            #fpath = node.fpath(rel=tree)
            #dpath = node.dpath(rel=tree)
            #bpath = node.bpath(rel=tree)
            #old=[ key, fpath, dpath, bpath]
            new=[ key, _fpath, _dpath, _bpath]
            #print(old)
            print(new)
            node.base=ROOT.path
            print(node)
            ##print(old==new)
            #old=f"{key}: fpath={fpath}, dpath={dpath}, bpath={bpath}"
            #new=f"{key}: fpath={fpath}, _dpath={dpath}, _path={bpath}" )

            #print( f"{key}:  fpath={_fpath}, dpath={_dpath}, bpath={_bpath}" )
            #print( f"{key}: _fpath={fpath}, _dpath={dpath}, _path={bpath}" )

def test_PLATTER_is_correct(PLATTER,ROOT):
    def same(node,name):
        root_path = ROOT.path
        node_path = node.path
        #root_path = ROOT.path()
        #node_path = node.path()
        rel_path = node_path.relative_to(root_path)
        assert str(rel_path) == name
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

