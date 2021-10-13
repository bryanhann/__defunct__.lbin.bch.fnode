import pytest
from pathlib import Path
from bch.node.class_node  import Node
import time
import tempfile

class Namespace: pass

pytest_plugins = "pytester"

TREE="""
    A/fruit/apple/.bch
    A/fruit/apple/.bch
    A/fruit/banana/
    A/animal/.bch/reg.py
    A/animal/.bch/index
    A/animal/insect/ant/
    A/animal/insect/bee/
    A/animal/mammal/ape/
    A/animal/mammal/bear/
    A/mythical/unicorn/.bch/reg.py
    A/mythical/unicorn/.bch/index
    B/
    """.split()

@pytest.fixture
def ROOT(tree):
    return Node(tree)

@pytest.fixture(scope="module")
def _tmpdir():
    name=str(time.time())
    return Path(tempfile.mkdtemp())/name

@pytest.fixture(scope="module")
def tree(_tmpdir):
    root=_tmpdir/'ROOT'
    for path in TREE:
        if path.endswith('/'):
            (root/path).mkdir(parents=True,exist_ok=True)
        else:
            (root/path).parent.mkdir(parents=True,exist_ok=True)
            (root/path).write_text('')
    return root

@pytest.fixture
def NODES(ROOT):
    return list( xx for xx in ROOT.descendants() )

@pytest.fixture
def DICT(NODES):
    acc={}
    for node in NODES:
        name = node.path.name
        #name = node.path().name
        if not name in acc:
            acc[name] = []
        acc[name].append(node)
    return acc

@pytest.fixture
def PLATTER(NODES):
    it=Namespace()
    for node in NODES:
        #name = node.path().name
        name = node.path.name
        if node.fpath: continue
        if name in '.bch'.split(): continue
        setattr( it, name, node )
    return it
