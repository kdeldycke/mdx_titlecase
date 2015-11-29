# -*- coding: utf-8 -*-
#
# Copyright (C) 2015 Kevin Deldycke <kevin@deldycke.com>
#
# This program is Free Software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.

from __future__ import (
    division, print_function, absolute_import, unicode_literals
)

import re

from markdown import Extension
from markdown.treeprocessors import Treeprocessor
from markdown.util import etree
from titlecase import titlecase


class TitlecaseExtension(Extension):

    def __init__(self, *args, **kwargs):
        """ Merge user and default configuration. """
        # Default settings.
        self.config = {
            'metadata': [
                ['title'],
                'List of metadata keys to which apply titlecasing.'],
        }

        # Override defaults with user settings.
        for key, value in kwargs.items():
            self.setConfig(key, str(value))

        super(TitlecaseExtension, self).__init__(*args, **kwargs)

    def extendMarkdown(self, md, md_globals):
        md.registerExtension(self)
        self.processor = TitlecaseTreeprocessor()
        self.processor.md = md
        self.processor.config = self.getConfigs()
        md.treeprocessors.add('headerid', self.processor, '_end')


class TitlecaseTreeprocessor(Treeprocessor):

    def run(self, node):
        # Apply transformation to all <hx> tags.
        for child in node.getiterator():
            if child.tag in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
                child.text = titlecase(child.text)

        # Apply transformation to metadata.
        if hasattr(self.md, 'Meta'):
            for key in self.config['metadata']:
                if key in self.md.Meta:
                    self.md.Meta[key] = map(titlecase, self.md.Meta[key])

        return node
