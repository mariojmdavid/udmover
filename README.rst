===============
User Data Mover
===============

Data mover between storage resources.

Description
===========

User level client tool to move or transfer files and directories between storage resources.

Instalation
===========

Installation through virtualenv::

    mkdir udmenv
    virtualenv -p python3 udmenv
    source udmenv/bin/activate


Configuration
=============

By default the udmover tool takes it's configuration from
the file ~/.udm.conf.

Copy the sample configuration file can be found in
to your home directory::

    cp udmenv/etc/udmover/udmover.conf.sample ~/.udm.conf

Modify the configuration file accordingly

Acknowledgments
===============

* udocker tool: https://github.com/indigo-dc/udocker/
