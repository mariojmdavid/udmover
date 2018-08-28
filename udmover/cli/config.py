# -*- coding: utf-8 -*-
"""
Configuration options
"""
import os
import sys
import configparser
from udmover.cli.msg import Msg


class Config(object):
    """Default configuration values for the whole application. Changes
    to these values should be made via a configuration file read via
    reside by default in ~/.udm.conf
    """

    def __init__(self):
        self.parser = configparser.ConfigParser()

    def get_conf(self, conf_file):
        """Get configuration options
        :returns dictionary with configuration options
        """
        self.parser.read(conf_file)
        cf = dict()
        cf['loglevel'] = self.parser.getint('DEFAULT', 'loglevel')
        # TODO: test if ssh key file exists and if dir exists and rw by the user
        if self.parser.has_option('DEFAULT', 'ssh_key'):
            cf['ssh_key'] = self.parser.get('DEFAULT', 'ssh_key')
        cf['local_dir'] = self.parser.get('local', 'local_dir')
        if self.parser.has_option('external', 'dav'):
            cf['dav'] = self.parser.getboolean('external', 'dav')
        if cf['dav']:
            cf['dav_endpoint'] = self.parser.get('external', 'dav_endpoint')
            cf['dav_user'] = self.parser.get('external', 'dav_user')
            cf['dav_pass'] = self.parser.get('external', 'dav_pass')
            if self.parser.has_option('external', 'dav_topdir'):
                cf['dav_topdir'] = self.parser.get('external', 'dav_topdir')
            cf['dav_insecure'] = self.parser.getboolean('external', 'dav_insecure')
            if not cf['dav_insecure']:
                if self.parser.has_option('external', 'dav_capath'):
                    cf['dav_capath'] = self.parser.get('external', 'dav_capath')
                else:
                    cf['dav_capath'] = '/etc/ssl/certs/ca-certificates.crt'
        return cf
