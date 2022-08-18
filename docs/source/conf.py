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

from os.path import join, abspath, dirname
import sys

sys.path.insert(
    0,
    abspath(
        join(
            dirname(__file__),
            '..',
            '..',
            'src',
        )
    )
)

import libertem_live  # noqa:E402

# -- Project information -----------------------------------------------------

project = 'LiberTEM-live'
copyright = 'LiberTEM-live Authors'
author = 'the LiberTEM team'

_version_bits = libertem_live.__version__.split('.')
# The short X.Y version
version = _version_bits[0] + '.' + _version_bits[1]
# The full version, including alpha/beta/rc tags

release = libertem_live.__version__


# -- General configuration ---------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.todo',
    'sphinx.ext.mathjax',
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages',
    'sphinx.ext.napoleon',
    'sphinx.ext.intersphinx',
    'sphinx.ext.doctest',
    'sphinxcontrib.bibtex',
    'nbsphinx',
    'nbsphinx_link',
    'IPython.sphinxext.ipython_console_highlighting',
    'sphinx_issues',
    'sphinx_rtd_theme',
]

bibtex_bibfiles = ['references-libertem_live.bib']

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
language = "en"

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path .
exclude_patterns = ['*/.ipynb_checkpoints/*', 'autogenerated/*.rst']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

html_logo = '_static/logo.png'

html_favicon = '../../corporatedesign/logo/favicon.ico'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
html_theme_options = {
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.
#
# html_sidebars = {}


# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'libertem_livedoc'


# -- Options for LaTeX output ------------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'LiberTEM-live.tex', 'LiberTEM-live Documentation',
     'Alexander Clausen, Dieter Weber', 'manual'),
]


# -- Options for manual page output ------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'libertem_live', 'LiberTEM-live Documentation',
     [author], 1)
]


# -- Options for Texinfo output ----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'LiberTEM-live', 'LiberTEM-live Documentation',
     author, 'LiberTEM-live', 'One line description of project.',
     'Miscellaneous'),
]


# -- Extension configuration -------------------------------------------------

# -- Options for sphinx_issues -----------------------------------------------
# GitHub repo
issues_github_path = "LiberTEM/LiberTEM-live"

# -- Options for doctest -----------------------------------------------------
# Disable standard doctest block testing since that would run it for
# docstrings in API reference, leading to failures because the test environment
# is not set up correctly
doctest_test_doctest_blocks = ''

# -- Options for todo extension ----------------------------------------------

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True

intersphinx_mapping = {
    'numpy': ('http://docs.scipy.org/doc/numpy/', None),
    'python': ('https://docs.python.org/3.10', None),
    'libertem': ('https://libertem.github.io/LiberTEM/', None),
}

# Sphinx' link checker.
linkcheck_ignore = [
    # Local URLs:
    r'^http://localhost.*',
    # Some kind of user agent filtering
    r'^https://pydata.org.*',
    # Freezes the link checker for unknown reasons within CI, hard to reproduce
    r'http://quantumdetectors.com/wp-content/uploads/2017/01/1532-Merlin-for-EM-Technical-Datasheet-v2.pdf',  # NOQA:E501
]

doctest_global_setup = '''
import os
def get_testdata_path():
    return os.environ.get(
        'TESTDATA_BASE_PATH',
        os.path.normpath(
            os.path.join(os.getcwd(), 'data')
        )
    )
DECTRIS_TESTDATA_PATH = os.path.join(
    get_testdata_path(),
    'dectris', 'zmqdump.dat.128x128-id34-exte-bslz4'
)
HAVE_DECTRIS_TESTDATA = os.path.exists(DECTRIS_TESTDATA_PATH)
'''
