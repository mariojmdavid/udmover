# -*- coding: utf-8 -*-
"""
Configuration options
"""
import os
import sys
try:
    from udmover.cli.msg import Msg
except ImportError:
    from cli.msg import Msg
try:
    from udmover.cli.util import FileUtil
except ImportError:
    from cli.util import FileUtil


class Config(object):
    """Default configuration values for the whole application. Changes
    to these values should be made via a configuration file read via
    self.user_init() and that can reside in ~/.udmover/udmover.conf
    """

    try:
        verbose_level = int(os.getenv("UDMOVER_LOGLEVEL", ""))
    except ValueError:
        verbose_level = 3

    homedir = os.path.expanduser("~") + "/.udmover"

    topdir = homedir

    config = "udmover.conf"

    # for tmp files only
    tmpdir = "/tmp"

    # defaults for container execution
    cmd = ["/bin/bash", "-i"]  # Comand to execute

    # default path for executables
    root_path = "/usr/sbin:/sbin:/usr/bin:/bin"
    user_path = "/usr/local/bin:/usr/bin:/bin"

    # Pass host env variables
    valid_host_env = ("TERM", "PATH", )
    invalid_host_env = ("VTE_VERSION", )

    # Curl settings
    http_proxy = ""    # ex. socks5://user:pass@127.0.0.1:1080
    timeout = 12       # default timeout (secs)
    download_timeout = 30 * 60    # file download timeout (secs)
    ctimeout = 6       # default TCP connect timeout (secs)
    http_agent = ""
    http_insecure = False

    def _verify_config(self):
        """Config verification"""
        if not Config.topdir:
            Msg().err("Error: UDMOVER directory not found")
            sys.exit(1)

    def _override_config(self):
        """Override config with environment"""
        Config.topdir = os.getenv("UDMOVER_DIR", Config.topdir)

    def _read_config(self, config_file):
        """Interpret config file content"""
        cfile = FileUtil(config_file)
        if cfile.size() == -1:
            return False
        data = cfile.getdata()
        for line in data.split("\n"):
            if not line.strip() or "=" not in line or line.startswith("#"):
                continue
            (key, val) = line.strip().split("=", 1)
            key = key.strip()
            Msg().err(config_file, ":", key, "=", val, l=Msg.DBG)
            try:
                exec('Config.%s=%s' % (key, val))
            except(NameError, AttributeError, TypeError, IndexError,
                   SyntaxError):
                raise ValueError("config file: %s at: %s" %
                                 (config_file, line.strip()))
            if key == "verbose_level":
                Msg().setlevel(Config.verbose_level)
        return True

    def user_init(self, config_file):
        """
        Try to load default values from config file
        Defaults should be in the form x = y
        """
        try:
            self._read_config("/etc/" + Config.config)
            if self._read_config(config_file):
                return True
            self._read_config(Config.topdir + "/" + Config.config)
            if self.topdir != self.homedir:
                self._read_config(Config.homedir + "/" + Config.config)
        except ValueError as error:
            Msg().err("Error:", error)
            sys.exit(1)
        self._override_config()
        self._verify_config()

    def username(self):
        """Get username"""
        try:
            return pwd.getpwuid(Config.uid).pw_name
        except KeyError:
            return ""

    def arch(self):
        """Get the host system architecture"""
        arch = ""
        try:
            machine = platform.machine()
            bits = platform.architecture()[0]
            if machine == "x86_64":
                if bits == "32bit":
                    arch = "i386"
                else:
                    arch = "amd64"
            elif machine in ("i386", "i486", "i586", "i686"):
                arch = "i386"
            elif machine.startswith("arm"):
                if bits == "32bit":
                    arch = "arm"
                else:
                    arch = "arm64"
        except (NameError, AttributeError):
            pass
        return arch

    def osversion(self):
        """Get operating system"""
        try:
            return platform.system().lower()
        except (NameError, AttributeError):
            return ""

    def osdistribution(self):
        """Get operating system distribution"""
        (distribution, version, dummy) = platform.linux_distribution()
        return (distribution.split(" ")[0], version.split(".")[0])

    def oskernel(self):
        """Get operating system"""
        try:
            return platform.release()
        except (NameError, AttributeError):
            return "3.2.1"

    def oskernel_isgreater(self, ref_version):
        """Compare kernel version is greater or equal than ref_version"""
        os_release = self.oskernel().split("-")[0]
        os_version = [int(x) for x in os_release.split(".")]
        for idx in (0, 1, 2):
            if os_version[idx] > ref_version[idx]:
                return True
            elif os_version[idx] < ref_version[idx]:
                return False
        return True

