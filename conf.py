#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# CDMI specification documentation build configuration file, created by
# sphinx-quickstart on Wed Nov  8 13:25:30 2017.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))
import codecs
from string import Template

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.autodoc',
    'sphinx.ext.todo',
    'sphinx.ext.coverage']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = ['.rst', '.md', '.txt']

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'CDMI V2.0.0a Specification'
copyright = '2018, SNIA'
author = 'SNIA'

licensetext = codecs.open('license.md', encoding='utf-8').read()

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = '2.0.0a'
# The full version, including alpha/beta/rc tags.
release = '2.0.0a'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'en'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = [ 'README.md', 'license.md', '**/scratch.txt' ]

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True


# Enable the use of numfig
numfig = True


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'classic'

html_logo = 'images/SNIA_R_logo.png'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# This is required for the alabaster theme
# refs: http://alabaster.readthedocs.io/en/latest/installation.html#sidebars
html_sidebars = {
    '**': [
        'relations.html',  # needs 'show_related': True theme option to display
        'searchbox.html',
    ]
}


# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'CDMI_v2.0.0_doc'


# -- Options for LaTeX output ---------------------------------------------
latex_engine = 'xelatex'

latex_contents = r'''
    \maketitle
    \licensepage
    \tableofcontents
    \clearpage
    \listoffigures
    \clearpage
    \listoftables
    \clearpage
    \pagenumbering{arabic}
'''

latex_defns = Template(r'''
    \def\licensepage{
        \pagestyle{normal}
        ${licensetext}
        \clearpage
    }
''')


latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    'fncychap': '',

    # The font size ('10pt', '11pt' or '12pt').
    #
    'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    'inputenc': '',
    'utf8extra': '',

    'preamble': r'''

    % Set fonts
    \usepackage{fontspec}
    \setsansfont{Arial}
    \setmainfont{Arial}
    \setmonofont{Courier New}

    % Adjust font size
    \usepackage{scrextend}
    \changefontsizes[10pt]{9pt}

    % Make table headers lightgray
    \usepackage{colortbl}
    \protected\def\sphinxstyletheadfamily {\cellcolor{lightgray}\sffamily}

    % Change Latex's Part/Chapter/Appendix to ISO's Section/Clause/Annex
    \addto\captionsenglish{\renewcommand{\partname}{Section}}
    \addto\captionsenglish{\renewcommand{\chaptername}{Clause}}
    \addto\captionsenglish{\renewcommand{\appendixname}{Annex}}
    \usepackage{chngcntr}
    \counterwithout{figure}{chapter}
    \counterwithout{table}{chapter}

    % Clear pages before new section
    \usepackage{titlesec}
    \newcommand{\sectionbreak}{\clearpage}

    % Change the page headers
    \makeatletter
    \fancypagestyle{normal}{
        \fancyhf{}
        \fancyhead[LE,LO]{{\py@HeaderFamily Cloud Data Management Interface \version}}
        \fancyfoot[LE,LO]{{\py@HeaderFamily \copyright \  SNIA 2018 - All rights reserved}}
        \fancyfoot[CE,CO]{{\py@HeaderFamily SNIA Working Draft}}
        \fancyfoot[RE,RO]{{\py@HeaderFamily\thepage}}
        }
    \makeatother

    % Create linenumers
    \usepackage{lineno} 
    \linenumbers
''' + latex_defns.substitute(licensetext=licensetext),   

    'tableofcontents': latex_contents,
    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
    
    'sphinxsetup': 'verbatimhintsturnover=true',
    'extraclassoptions': 'openany',
    'releasename': 'Version',
    
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'CDMI_v2.0.0.tex', 'Cloud Data Management Interface (CDMI)',
     'SNIA Working Draft', 'manual'),
]

latex_logo = 'images/SNIA_R_logo.png'

latex_toplevel_sectioning = 'part'

# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'CDMI_v2.0.0_spec', 'Cloud Data Management Interface (CDMI)',
     [author], 1)
]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'CDMI_v2.0.0', 'CDMI specification Documentation',
     author, 'CDMI_v2.0.0', 'CDMI Specification.',
     'Miscellaneous'),
]



# -- Options for Epub output ----------------------------------------------

# Bibliographic Dublin Core info.
epub_title = project
epub_author = author
epub_publisher = author
epub_copyright = copyright

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
#
# epub_identifier = ''

# A unique identification for the text.
#
# epub_uid = ''

# A list of files that should not be packed into the epub file.
epub_exclude_files = ['search.html']


# -- Todo options
# If this is True, todo and todolist produce output, else they produce nothing. The default is False.
todo_include_todos = True
# If this is True, todo emits a warning for each TODO entries. The default is False.
todo_emit_warnings = False
# If this is True, todolist produce output without file path and line, The default is False.
todo_link_only =False
