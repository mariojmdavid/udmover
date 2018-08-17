# -*- coding: utf-8 -*-
"""
Command line and options
"""
try:
    from udmover import __version__
except ImportError:
    __version__ = '0.0.1.dev'
try:
    from udmover.cli.msg import Msg
except ImportError:
    from cli.msg import Msg


class Cmd(object):
    """Implements all commands and options for udmover
    """

    @staticmethod
    def do_version():
        Msg().out('Version: ', __version__)

    def do_help(self):
        """
        Syntax:
          udmover  <command>  [command_options]  <command_args>

          version  :Shows udmover version and exits
          help     :This help
        """
        Msg().out(self.do_help.__doc__)
