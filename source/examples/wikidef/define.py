#!/usr/bin/env python3

"""
Script to contact Wikipedia and get articles on a specified topic.
python define.py interesting_topic
"""

import sys
from definitions import Definitions
from html2text import html2text

title = len(sys.argv) == 2 and sys.argv[1] or ""

definition = Definitions.article(title)
txt = html2text(definition)
print(txt)
