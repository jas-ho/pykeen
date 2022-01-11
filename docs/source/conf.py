# -*- coding: utf-8 -*-
#
# Configuration file for the Sphinx documentation builder.
#
# This file does only contain a selection of the most common options. For a
# full list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#

import os
import re
import sys
from datetime import date

sys.path.insert(0, os.path.abspath('../../src'))
# sys.path.insert(0, os.path.abspath('..'))

# -- Mockup PyTorch to exclude it while compiling the docs--------------------
# autodoc_mock_imports = ['torch', 'torchvision']

# from unittest.mock import Mock
# sys.modules['numpy'] = Mock()
# sys.modules['numpy.linalg'] = Mock()
# sys.modules['scipy'] = Mock()
# sys.modules['scipy.optimize'] = Mock()
# sys.modules['scipy.interpolate'] = Mock()
# sys.modules['scipy.sparse'] = Mock()
# sys.modules['scipy.ndimage'] = Mock()
# sys.modules['scipy.ndimage.filters'] = Mock()
# sys.modules['tensorflow'] = Mock()
# sys.modules['theano'] = Mock()
# sys.modules['theano.tensor'] = Mock()
# sys.modules['torch'] = Mock()
# sys.modules['torch.optim'] = Mock()
# sys.modules['torch.nn'] = Mock()
# sys.modules['torch.nn.init'] = Mock()
# sys.modules['torch.autograd'] = Mock()
# sys.modules['sklearn'] = Mock()
# sys.modules['sklearn.model_selection'] = Mock()
# sys.modules['sklearn.utils'] = Mock()

# -- Project information -----------------------------------------------------

project = 'pykeen'
copyright = f'2019-{date.today().year}, PyKEEN Project Team'
author = 'PyKEEN Project Team'

# The full version, including alpha/beta/rc tags.
release = '1.7.0-dev'

# The short X.Y version.
parsed_version = re.match(
    '(?P<major>\d+)\.(?P<minor>\d+)\.(?P<patch>\d+)(?:-(?P<release>[0-9A-Za-z-]+(?:\.[0-9A-Za-z-]+)*))?(?:\+(?P<build>[0-9A-Za-z-]+(?:\.[0-9A-Za-z-]+)*))?',
    release,
)
version = parsed_version.expand('\g<major>.\g<minor>.\g<patch>')

if parsed_version.group('release'):
    tags.add('prerelease')

# -- General configuration ---------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
add_module_names = False

# A list of prefixes that are ignored when creating the module index. (new in Sphinx 0.6)
modindex_common_prefix = ["pykeen."]

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autosummary',
    'sphinx.ext.autodoc',
    'sphinx.ext.coverage',
    'sphinx.ext.intersphinx',
    "sphinx.ext.todo",
    'sphinx.ext.mathjax',
    'sphinx.ext.viewcode',
    'sphinx_autodoc_typehints',
    'sphinx_click.ext',
    'sphinx_automodapi.automodapi',
    'texext',
]

# show todo's
todo_include_todos = True

# generate autosummary pages
autosummary_generate = True

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ['_static']

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.
#
# html_sidebars = {}

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
#
html_logo = 'logo.png'

# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'PyKEENdoc'

# -- Options for LaTeX output ------------------------------------------------

# latex_elements = {
#     The paper size ('letterpaper' or 'a4paper').
#
#     'papersize': 'letterpaper',
#
#     The font size ('10pt', '11pt' or '12pt').
#
#     'pointsize': '10pt',
#
#     Additional stuff for the LaTeX preamble.
#
#     'preamble': '',
#
#     Latex figure (float) alignment
#
#     'figure_align': 'htbp',
# }

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
# latex_documents = [
#     (
#         master_doc,
#         'pykeen.tex',
#         'PyKEEN Documentation',
#         author,
#         'manual',
#     ),
# ]

# -- Options for manual page output ------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (
        master_doc,
        'pykeen',
        'PyKEEN Documentation',
        [author],
        1,
    ),
]

# -- Options for Texinfo output ----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (
        master_doc,
        'pykeen',
        'PyKEEN Documentation',
        author,
        'PyKEEN Project Team',
        'Training and evaluatation knowledge graph embedding models.',
        'Miscellaneous',
    ),
]

# -- Options for Epub output -------------------------------------------------

# Bibliographic Dublin Core info.
# epub_title = project

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
#
# epub_identifier = ''

# A unique identification for the text.
#
# epub_uid = ''

# A list of files that should not be packed into the epub file.
# epub_exclude_files = ['search.html']

# -- Extension configuration -------------------------------------------------

# -- Options for intersphinx extension ---------------------------------------

# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {
    'https://docs.python.org/3/': None,
    'torch': ('https://pytorch.org/docs/stable', None),
    'torchvision': ('https://pytorch.org/vision/stable', None),
    'numpy': ('https://numpy.org/doc/stable', None),
    'optuna': ('https://optuna.readthedocs.io/en/latest', None),
    'pybel': ('https://pybel.readthedocs.io/en/latest/', None),
    'rexmex': ('https://rexmex.readthedocs.io/en/latest/', None),
    'bio2bel': ('https://bio2bel.readthedocs.io/en/latest/', None),
    'boto3': ('https://boto3.amazonaws.com/v1/documentation/api/latest/', None),
    'scipy': ('https://docs.scipy.org/doc/scipy/reference/', None),
}

autoclass_content = 'both'
# autodoc_member_order = 'bysource'
# autodoc_typehints = 'both' # TODO turn on after 4.1 release
# autodoc_preserve_defaults = True
