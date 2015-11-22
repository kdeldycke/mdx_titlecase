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

import textwrap
import unittest

import markdown

from mdx_titlecase import TitlecaseExtension


class MDXTitlecase(unittest.TestCase):

    def test_load_extension_as_string(self):
        markdown.markdown('', extensions=['titlecase'])

    def test_load_extension_as_object(self):
        markdown.markdown('', extensions=[TitlecaseExtension()])

    def test_configs_parameter(self):
        md = markdown.Markdown()
        md.registerExtension(TitlecaseExtension(foo='bar'))
        ext = md.registeredExtensions[0]
        self.assertEqual(ext.config['foo'][0], 'bar')

    def test_title_casing(self):
        text = textwrap.dedent("""
            un-cased article title of the year
            ==================================

            This is a stupid sentence.

            sub-title of the day
            --------------------

            Lorem ipsum.
            """).encode('utf-8')
        html = textwrap.dedent("""\
            <h1>Un-Cased Article Title of the Year</h1>
            <p>This is a stupid sentence.</p>
            <h2>Sub-Title of the Day</h2>
            <p>Lorem ipsum.</p>""")
        output = markdown.markdown(text, extensions=[TitlecaseExtension()])
        self.assertEqual(output, html)
