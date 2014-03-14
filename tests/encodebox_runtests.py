#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Transcoding watchfolder called EncodeBox
# Retrieved from git clone https://bitbucket.org/cloudncode/encodebox.git
u"""
    Run the unit tests of EncodeBox.

    :author: David Fischer <david.fischer.ch@gmail.com>
    :copyright: (c) 2014 <TODO Company> Inc. All rights reserved.
"""

from pytoolbox.encoding import configure_unicode
from pytoolbox.unittest import runtests


def main():
    configure_unicode()
    return runtests(__file__, cover_packages=[u'encodebox'], packages=[u'encodebox', u'tests'])

if __name__ == u'__main__':
    main()