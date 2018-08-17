#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
udmover Description
"""
from __future__ import division, print_function, absolute_import

import sys
#import logging

try:
    from udmover.cli.cmdparser import CmdParser
except ImportError:
    from cli.cmdparser import CmdParser
try:
    from udmover.cli.cmd import Cmd
except ImportError:
    from cli.cmd import Cmd

__author__ = "Mario David"
__copyright__ = "LIP"
__license__ = "Licensed under the Apache License, Version 2.0"
__date__ = "2018"

#_logger = logging.getLogger(__name__)


#def setup_logging(loglevel):
#    """Setup basic logging

#    Args:
#      loglevel (int): minimum loglevel for emitting messages
#    """
#    logformat = "[%(asctime)s] %(levelname)s:%(name)s:%(message)s"
#    logging.basicConfig(level=loglevel, stream=sys.stdout,
#                        format=logformat, datefmt="%Y-%m-%d %H:%M:%S")


def main():
    """Main entry point allowing external calls

    Args:
      args ([str]): command line parameter list
    """
    cmdp = CmdParser()
    cmd = Cmd()
    parseok = cmdp.parse(sys.argv)

    if (cmdp.get("", "CMD") == "version") or \
            cmdp.get("--version", "GEN_OPT") or \
            cmdp.get("-V", "GEN_OPT"):
        cmd.do_version()
        sys.exit(0)
    if (cmdp.get("", "CMD") == "help") or \
            cmdp.get("--help", "GEN_OPT") or \
            cmdp.get("-h", "GEN_OPT"):
        cmd.do_help()
        sys.exit(0)
    if not parseok:
        #_logger.error("Error: parsing command line, use: udmover help")
        sys.exit(1)


if __name__ == "__main__":
    main()
