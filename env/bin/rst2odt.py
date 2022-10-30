#!/home/madvirus/Documents/contrib/equestlms/env/bin/python

# $Id: rst2odt.py 8994 2022-01-29 16:28:17Z milde $
# Author: Dave Kuhlman <dkuhlman@rexx.com>
# Copyright: This module has been placed in the public domain.

"""
A front end to the Docutils Publisher, producing OpenOffice documents.
"""

try:
    import locale

    locale.setlocale(locale.LC_ALL, "")
except:
    pass

from docutils.core import default_description, publish_cmdline_to_binary
from docutils.writers.odf_odt import Reader, Writer

description = (
    "Generates OpenDocument/OpenOffice/ODF documents from "
    "standalone reStructuredText sources.  " + default_description
)


writer = Writer()
reader = Reader()
output = publish_cmdline_to_binary(
    reader=reader, writer=writer, description=description
)
