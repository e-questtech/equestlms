#!/home/madvirus/Documents/contrib/equestlms/env/bin/python

# $Id: rst2xml.py 8927 2022-01-03 23:50:05Z milde $
# Author: David Goodger <goodger@python.org>
# Copyright: This module has been placed in the public domain.

"""
A minimal front end to the Docutils Publisher, producing Docutils XML.
"""

try:
    import locale

    locale.setlocale(locale.LC_ALL, "")
except:
    pass

from docutils.core import default_description, publish_cmdline

description = (
    "Generates Docutils-native XML from standalone "
    "reStructuredText sources.  " + default_description
)

publish_cmdline(writer_name="xml", description=description)
