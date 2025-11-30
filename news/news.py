#!/usr/bin/env python3
#
# news.py
# 
from pyscript import display, document, when, window
from re import sub
from sys import version
from urllib.parse import urlencode, urlparse, urlunparse

"""
This PyScript loaded from index.html creates a tracker-free, 
clickable, short Google Search link to search Google News. 
The link updates as you enter your query.
"""

# Initialize static HTML.
title = document.querySelector('title')
title.innerText = window.location.href
header = document.querySelector('#h1-id')
header.href = window.location.href

# disp appends NBSP to s before display (for display: inline-block)
disp = lambda s, x='\u00A0': display(f"{s}{x}", target='footer')

def put_query(value):
    """
    Put URI with value query into #query anchor. Parse base URI, 
    unparse base URI including query value (if any), set that URI
    as #query anchor href and wrappable version (ZERO WIDTH SPACEs) 
    as #query anchor text. (See: https://www.urlencoder.io/python/)
    """
    base = 'https://google.com/search'
    sch, loc, pth, _, _, _ = urlparse(base)
    params = {'tbm': 'nws', 'q': value, } if value else dict()
    query = urlencode(params)
    parts = (sch, loc, pth, '', query, '', )
    uri = urlunparse(parts)
    anchor = document.querySelector('#query a')
    anchor.href = uri
    anchor.text = sub(r'([/+])', r'\1' + '\u200B', uri)

put_query('') # initially empty query

# Fires on every change (typing, paste, delete)
# Alternative: only after each key press (ignores mouse paste)
# @when("keyup", "#inp")
@when("input", "#inp")
def on_input(evt):
    value = document.querySelector("#inp").value
    put_query(value)

# Update footer with display information.
disp(f"DEBUG:")
disp(f"VERSION:{version}")
disp(f"LOCATION:{window.location.href}")
disp(f"LOCATION KEYS:{window.location.object_keys()}")
disp(f"LOCATION VALUES:{window.location.object_values()}")

# Set '.hide' display: none; and 'main,footer' display: block;,
# then set focus on textbox as last PyScript actions.
for el in document.querySelectorAll('.hide'):
    el.style.display = 'none'
for el in document.querySelectorAll('main,footer'):
    el.style.display = 'block'
document.querySelector('input#inp').focus()
