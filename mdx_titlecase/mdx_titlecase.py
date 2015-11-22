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

import markdown
from markdown.util import etree
from titlecase import titlecase


class TitlecaseExtension(markdown.Extension):

    def __init__(self, **kwargs):
        """ Merge user and default configuration. """
        # Default settings.
        self.config = {
            'foo': ['fighter', 'Option description.'],
        }
        # Override defaults with user settings.
        for key, value in kwargs.items():
            self.setConfig(key, str(value))

    def extendMarkdown(self, md, md_globals):
        md.treeprocessors.add('titlecase', TitlecaseProcessor(), '_end')


class TitlecaseProcessor(markdown.treeprocessors.Treeprocessor):

    def run(self, node):
        expr = re.compile('h\d')
        for child in node.getiterator():
            match = expr.match(child.tag)
            if match:
                child.text = titlecase(child.text)
        return node
