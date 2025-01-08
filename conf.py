# Configuration file for the Sphinx documentation builder.

# -- Path setup --------------------------------------------------------------

import os
import sys
sys.path.insert(0, os.path.abspath("./_ext"))


# -- Project information -----------------------------------------------------

project = "multiphenicsx"
copyright = "2016-2025, the multiphenicsx authors"
author = "Francesco Ballarin"


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here.
extensions = [
    "sphinxcontrib.bibtex",
    "ext"
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# List of bib files
bibtex_bibfiles = ["_static/bib/publications.bib"]

# Suppress config.cache warnings
# https://github.com/sphinx-doc/sphinx/issues/12300#issuecomment-2062238457
suppress_warnings = ["config.cache"]


# -- Options for HTML output -------------------------------------------------
html_title = "multiphenicsx"

# The theme to use for HTML and HTML Help pages.
# From https://github.com/bashtage/sphinx-material
html_theme = "sphinx_material"

# Material theme options
html_theme_options = {
    # Set the name of the project to appear in the navigation.
    "nav_title": "multiphenicsx",

    # Set you GA account ID to enable tracking
    "google_analytics_account": "G-TY8PDHZR0G",

    # Specify a base_url used to generate sitemap.xml. If not
    # specified, then no sitemap will be built.
    "base_url": "https://multiphenics.github.io/",

    # Set the color and the accent color
    "theme_color": "#00325c",
    "color_primary": "unicatt",
    "color_accent": "unicatt",

    # Set the repo location to get a badge with stats
    "repo_url": "https://github.com/multiphenics/multiphenicsx/",
    "repo_name": "multiphenicsx",

    # Visible levels of the global TOC; -1 means unlimited
    "globaltoc_depth": 1,
    # If False, expand all TOC entries
    "globaltoc_collapse": True,
    # If True, show hidden TOC entries
    "globaltoc_includehidden": False,

    # Path to a touch icon, should be 152x152 or larger.
    "touch_icon": "images/multiphenicsx-logo.png",
    "logo_icon": "&#xe069",

    # Main menu links
    "nav_links": [
        {
            "href": "tutorials",
            "internal": True,
            "title": "Tutorials",
        },
        {
            "href": "installing",
            "internal": True,
            "title": "Installation",
        },
        {
            "href": "contributing",
            "internal": True,
            "title": "How to contribute",
        },
        {
            "href": "citing",
            "internal": True,
            "title": "How to cite",
        },
        {
            "href": "publications",
            "internal": True,
            "title": "Publications",
        }
    ],

    # Disable version dropbown
    "version_dropdown": False,
}
html_sidebars = {
    "**": ["logo-text.html", "globaltoc.html", "localtoc.html", "searchbox.html"]
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

# Custom CSS files
html_css_files = [
    "https://cdnjs.cloudflare.com/ajax/libs/jquery-dropdown/2.0.3/jquery.dropdown.min.css",
    "https://fonts.googleapis.com/css?family=Pangolin",
    "css/custom.css",
]

# Custom javascript files
html_js_files = [
    "https://cdnjs.cloudflare.com/ajax/libs/jquery/3.3.1/jquery.min.js",
    "https://cdnjs.cloudflare.com/ajax/libs/jquery-dropdown/2.0.3/jquery.dropdown.min.js",
    "js/external_links.js"
]
