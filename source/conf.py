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

# from recommonmark.parser import CommonMarkParser

# -- Project information -----------------------------------------------------

project = 'NLP for French'
copyright = '2022, Xiaoou Wang'
author = 'Xiaoou Wang'

# html_theme_options = {
#     'navigation_depth': 4,
# }

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
# extensions = ['myst-parser']
# extensions = []
# extensions = ['sphinx_autorun',
extensions = ['sphinx.ext.mathjax', 'sphinx_autorun',
              'nbsphinx', 'sphinx_copybutton', "sphinx_inline_tabs", 'sphinx.ext.autosectionlabel', "myst_parser", 'sphinx_gallery.load_style']
# extensions = ['myst_parser']
# extensions = ['myst_parser',"nbsphinx"]
#   'numpydoc']


mathjax_config = {
    'TeX': {'equationNumbers': {'autoNumber': 'AMS', 'useLabelIds': True}},
}

nbsphinx_thumbnails = {
    'ml/01_classification_prenoms': 'static/a-local-file.png',
}

suppress_warnings = [
    "image.not_readable"
]

myst_update_mathjax = False

# Add any paths that contain templates here, relative to this directory.
# templates_path = ['templates']
templates_path = ['templates']
# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
# language = 'fr'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects htmlstatic_path and html_extra_path.

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
# n themes.
#
# html_theme = 'alabaster'
# html_theme = 'sphinx_rtd_theme'
# html_theme = 'asteroid_sphinx_theme'
html_theme = 'furo'
html_title = ""

nbsphinx_execute = 'auto'

html_js_files = [
    'custom.js',
]


GOOGlE = """
</script>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css" integrity="sha512-iBBXm8fW90+nuLcSKlbmrPcLa0OT92xO1BIsZ+ywDWZCvqsWgccV3gFoRBv0z+8dLJgyAHIhR35VZc2oM/gI1w==" crossorigin="anonymous" />
<!-- Global site tag (gtag.js) - Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-58WGY2PHYB"></script>
<script src='https://kit.fontawesome.com/a076d05399.js' crossorigin='anonymous'></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'G-58WGY2PHYB');
</script>
<!-- Default Statcounter code for nlpinfrench
http://nlpinfrench.fr -->
<script type="text/javascript">
var sc_project=12500373;
var sc_invisible=1;
var sc_security="def60251";
</script>
<script type="text/javascript"
src="https://www.statcounter.com/counter/counter.js"
async></script>
<noscript><div class="statcounter"><a title="Web Analytics
Made Easy - StatCounter" href="https://statcounter.com/"
target="_blank"><img class="statcounter"
src="https://c.statcounter.com/12500373/0/def60251/1/"
alt="Web Analytics Made Easy -
StatCounter"></a></div></noscript>
<!-- End of Statcounter Code -->
<script src="https://cdn.jsdelivr.net/gh/cferdinandi/gumshoe@4.0/dist/gumshoe.polyfills.min.js"></script>
"""


def setup(app):
    # 3. Tell Sphinx to add your JS code. Sphinx will insert
    #    the `body` into the html inside a <script> tag:
    app.add_js_file(None, body=GOOGlE)


html_css_files = [
    'custom.css',
]


# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
htmlstatic_path = ['static']
html_logo = "nlp_Logo.png"

html_theme_options = {
    "light_logo": "nlp_Logo.png",
    "dark_logo": "nlp_Logo.png",
}
# exclude_patterns = [r'*/image.md',r'better_programmer/*','ml/index.md','transformers/index.md']
#
