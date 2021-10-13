#!/usr/bin/env python3

import os

HOME=os.environ['HOME']
MOUNTS=[]
MOUNTS.append( '/Volumes' )
MOUNTS.append( '/mount' )
MOUNTS.append( '/mnt' )
MOUNTS.append( '/media/%s' % HOME )
MOUNTS.append( HOME )

