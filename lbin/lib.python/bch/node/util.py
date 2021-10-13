#!/usr/bin/env python3

import sys
import os
from pathlib import Path
from pprint import pprint
import importlib.util



def _isdir(path):
    try:
        return path.is_dir()
    except PermissionError:
        return False

def mod4path(path):
    name='anonymoose'
    path=str(path)
    spec = importlib.util.spec_from_file_location(name, path)
    foo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(foo)
    return foo


