# Configuration file for the Sphinx documentation builder.

# -- Project information -----------------------------------------------------

project = 'AWS' # Your project name
copyright = '2021, Graziella' # Your copyright
author = 'Graziella' # Your name

release = '0.1'
version = '0.1.0'

# -- General configuration ---------------------------------------------------

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output -------------------------------------------------

html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files.
# This path is relative to the directory containing conf.py (docs/source/)
html_static_path = ['static'] # Corrected based on your folder name

# The logo shown in the side bar.
# Place your logo file inside the static directory (docs/source/static/)
# The path here is relative to the directory containing conf.py (docs/source/)
html_logo = 'static/aws_logo.png' # Corrected based on your folder name


# Add any CSS files you want to include
# These paths are relative to the directories in html_static_path
html_css_files = [
    'logo_resize.css', # Include the new CSS file for logo resizing
]


# -- Options for EPUB output -------------------------------------------------
epub_show_urls = 'footnote'
