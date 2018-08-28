# -*- coding: utf-8 -*-
"""
Command line and options
"""
from udmover import __version__
from udmover.cli.msg import Msg
from udmover.storage.webdav.client import Client


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

    def do_list_files_ext(self, cf):
        """
        Get list of files from the external/public server
        """
        env = {'webdav_hostname': cf['dav_endpoint'],
               'webdav_login': cf['dav_user'],
               'webdav_password': cf['dav_pass'],
               'webdav_insecure': cf['dav_insecure']}
        if 'dav_topdir' in cf:
            env['webdav_root'] = cf['dav_topdir']
        if not cf['dav_insecure']:
            if 'dav_capath' in cf:
                env['webdav_capath'] = cf['dav_capath']
        Msg().out(env)


        client = Client(env)
        check = client.check()
        if check:
            Msg().out("success")
            list_files = client.list()
            Msg().out(list_files)
        else:
            Msg().out("not success")
