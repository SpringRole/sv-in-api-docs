# -*- coding: utf-8 -*-
#
# Ledger documentation build configuration file.

def setup(app):
    app.add_stylesheet('theme_overrides.css') # Override wide tables in RTD theme

# General Configuration
# =====================

extensions = []

source_suffix = ['.rst']

master_doc = 'index'

project = u'SpringVerify API Docs'
copyright = u'2020, SpringWorks'
author = u'SpringWorks'

version = u'2'
release = u'2'

pygments_style = 'sphinx'

# Options for HTML Output
# =======================

html_theme = 'groundwork'

html_static_path = ['_static']

# intersphinx
# ===========

extensions += ['sphinx.ext.intersphinx']