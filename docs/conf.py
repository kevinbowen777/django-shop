"""Sphinx configuration."""
project = "django-shop"
author = "Kevin Bowen"
copyright = f"2023, {author}"
#
html_theme = "furo"
html_logo = "django_24.png"
html_title = "django-shop"
extensions = [
    "sphinx.ext.duration",
]
