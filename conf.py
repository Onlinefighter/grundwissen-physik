# import sys, os

extensions = [
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.imgmath',
    ]

templates_path = ['_templates']
source_suffix  = '.rst'
master_doc     = 'index'

project   = 'Grundwissen Physik'
copyright = '2011-2017, Bernhard Grotz'

version = '0.4.3e'
release = '0.4.3e'

pygments_style = 'sphinx'
trim_footnote_reference_space = True
todo_include_todos = False
language = 'de'

html_theme = 'sphinxdoc'
html_static_path = ['_static']
html_additional_pages = {'home': 'home.html'}
htmlhelp_basename = 'Grundwissen Physik'
html_title        = 'Grundwissen Physik'
html_short_title  = 'Grundwissen Physik'
html_show_sourcelink = True
html_show_copyright  = False
html_show_sphinx     = False
html_last_updated_fmt = '%d.%m.%Y'
today_fmt = '%d.%m.%Y'

html_favicon = 'favicon.ico'
html_logo    = 'logo.png'
latex_logo   = 'logo_print.png'

html_search_language = 'en'
html_search_options = {'type': 'default'}

exclude_patterns = [
    'notes.rst', 
    '*/notes.rst', 
    '**/notes.rst',
    'todos.rst',
    'README.rst'
    ]

latex_preamble = r'''
\usepackage[T1]{fontenc}
\usepackage[version=3]{mhchem}
\usepackage{shadow}
\usepackage{amsmath, units, cancel}
\usepackage{amsfonts, amssymb,color}
\usepackage{multicol,pifont,mdframed,lscape}
\usepackage{nicefrac,marvosym,wasysym, textcomp, gensymb}
\usepackage[style=english]{csquotes}
\setlength{\headheight}{15pt}
\setcounter{secnumdepth}{-1}
\setcounter{tocdepth}{2}
\clubpenalty  = 10000 % Disable single lines at the start of a page ("Schusterjungen")
\widowpenalty = 10000 % Disable single lines at the end   of a page ("Hurenkinder")
\displaywidowpenalty = 10000
\usepackage{hyperref,url}
\hypersetup{
pdftitle={Grundwissen Physik},
pdfsubject={Ein Lehrbuch über grundlegende physikalische Zusammenhänge},
pdfauthor={Bernhard Grotz},
pdfkeywords={Physik} {Lehrbuch} {Schule} {Unterricht} {Übungsaufgaben} {Aufgaben} {Lösungen},
}
'''

latex_show_pagerefs = False
imgmath_image_format='png'
imgmath_latex_preamble = latex_preamble

latex_elements = {
    'preamble': latex_preamble,
    'classoptions': 'oneside,openany',
    'papersize': 'a4paper,',
    'pointsize': '12pt,',
    'fontpkg': '',
    'babel':    '\\usepackage[ngerman]{babel}',
    'geometry': '\\usepackage[left=2.5cm, right=2.5cm, top=2.5cm, bottom=2.5cm]{geometry}',
    'fncychap': '',
    }

latex_documents = [
    ('index', 'grundwissen-physik.tex', 'Grundwissen Physik', 'Bernhard Grotz',
     'manual'),
    ]

texinfo_documents = [
    ('index', 'Physik', 'Grundwissen Physik', 'Bernhard Grotz', 'Physik',
     'Grundwissen Physik', ''),
    ]

intersphinx_mapping = {
    'gw':('http://grund-wissen.de/', None),
    'gwc':('http://grund-wissen.de/chemie/', None),
    'gwe':('http://grund-wissen.de/elektronik/', None),
    'gwm':('http://grund-wissen.de/mathematik/', None),
    'gwl': ('http://grund-wissen.de/linux/', None),
    'gwv': ('http://grund-wissen.de/vegan/', None),
    'gwic': ('http://grund-wissen.de/informatik/c', None),
    'gwil': ('http://grund-wissen.de/informatik/latex', None),
    'gwip': ('http://grund-wissen.de/informatik/python', None),
    }

