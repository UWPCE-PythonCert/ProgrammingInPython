# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'Programming in Python'

# the one with the text too
html_logo = "_static/UWPCE_logo_full.png"

source_suffix = '.rst'
# The master toctree document.
master_doc = 'index'

# copyright = '2020, Christopher Barker'
# author = 'Christopher Barker'
author_list = ["Natasha Aleksandrova",
               "Christopher Barker",
               "Brian Dorsey",
               "Cris Ewing",
               "Christy Heaton",
               "Jon Jacky",
               "Maria McKinley",
               "Andy Miles",
               "Rick Riehle",
               "Joseph Schilz",
               "Joseph Sheedy",
               "Hosung Song"
               ]

author = ", ".join(sorted(author_list, key=lambda n: n.split()[-1]))

copyright = ("2020, University of Washington, {}. "
             "Creative Commons Attribution-ShareAlike 4.0 license".format(author)
             ).format(author)

# The full version, including alpha/beta/rc tags
release = '7.0'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ["sphinx.ext.githubpages",
              'IPython.sphinxext.ipython_console_highlighting',
              'IPython.sphinxext.ipython_directive',
              ]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
# html_theme = 'alabaster'
html_theme = "sphinx_rtd_theme"

html_theme_options = {
    # 'canonical_url': '',
    # 'analytics_id': 'UA-XXXXXXX-1',  #  Provided by Google in your dashboard
    # 'github_url': 'https://github.com/UWPCE-PythonCert/ProgrammingInPython',
    'logo_only': True,
    'display_version': False,
    'prev_next_buttons_location': 'both',
    'style_external_links': True,
    # 'vcs_pageview_mode': '',
    'style_nav_header_background': '#4b2e83',
    # # Toc options
    # 'collapse_navigation': True,
    # 'sticky_navigation': True,
    'navigation_depth': 2,
    # 'includehidden': True,
    'titles_only': True
}

github_url = 'https://github.com/UWPCE-PythonCert/ProgrammingInPython'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']