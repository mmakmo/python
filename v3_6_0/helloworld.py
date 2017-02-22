#!/usr/bin/env python

import sys

# -*- coding: utf-8 -*-


def greet(name):
    print('Hello, {0}!'.format(name))


if len(sys.argv) > 1:
    name = sys.argv[1]
    greet(name)
else:
    greet('world')
