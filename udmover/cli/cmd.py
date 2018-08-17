#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Command line and options
"""

import udmover


class Cmd(object):
    """Implements all commands and options for udmover
    """

    def do_version(self):
        return udmover.__version__

    def do_help(self):
        h = 'This is the User Data Mover'
        return h
