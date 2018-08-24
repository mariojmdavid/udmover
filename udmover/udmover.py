#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
udmover Description
"""
from __future__ import division, print_function, absolute_import

import sys
import os
from udmover.cli.cmdparser import CmdParser
from udmover.cli.cmd import Cmd
from udmover.cli.msg import Msg
from udmover.cli.config import Config


__author__ = "Mario David"
__copyright__ = "LIP"
__license__ = "Licensed under the Apache License, Version 2.0"
__date__ = "2018"


def main():
    """Main entry point allowing external calls

    Args:
      args ([str]): command line parameter list
    """
    cmdp = CmdParser()
    cmd = Cmd()
    conf = Config()
    parseok = cmdp.parse(sys.argv)
    conf_file = os.path.expanduser('~') + os.sep + '.udm.conf'
    try:
        with open(conf_file, "r") as f:
            f.read()
    except (IOError, OSError):
        Msg.err("Error: config file: %s" % conf_file)
        sys.exit(1)

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
    if cmdp.get("", "CMD") == "lsext":
        cf = conf.get_conf(conf_file)
        cmd.do_list_files_ext(cf)
        sys.exit(0)
    if not parseok:
        Msg.err("Error: parsing command line, use: udmover help")
        sys.exit(1)


if __name__ == "__main__":
    main()
