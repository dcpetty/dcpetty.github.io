#!/usr/bin/env python3
#
# links.py
# 
from pyscript import display, document, when, window
from re import sub
from sys import version
from urllib.parse import urlencode, urlparse, urlunparse

"""
This PyScript loaded from index.html creates tracker-free, clickable, 
short Google Search links to search Google News, Google Maps, & Google 
Images. The links update as you enter your query.
"""

# Initialize static HTML.
title = document.querySelector('title')
title.innerText = window.location.href
header = document.querySelector('#h1-href')
header.innerHTML = window.location.href.replace('/', '/\u200B')

# disp appends NBSP to s before display (for display: inline-block)
disp = lambda s, x='\u00A0': display(f"{s}{x}", target='footer')

data = (
    # selector, URI location, URI params, query key
    ( '#queryn', 'search', {'tbm': 'nws', }, 'q', ),
    ( '#querym', 'maps/search/', {'api': '1', }, 'query', ),
    ( '#queryi', 'search', {'tbm': 'isch', }, 'q', ),
)
def put_query(selector, path = '', params = dict()):
    """
    Put URI with urlencoded params and appended path into selector.
    Parse base URI appended with path, unparse base URI including 
    query value (if any), set that URI as selector anchor href
    and wrappable version (ZERO WIDTH SPACEs) as selector anchor text. 
    (See: https://www.urlencoder.io/python/)
    """
    #from js import console
    #console.log(f"{selector} {path} {params}")

    base = 'https://google.com/' + (path if path else '')
    sch, loc, pth, _, _, _ = urlparse(base)
    query = urlencode(params)
    parts = (sch, loc, pth, '', query, '', )
    uri = urlunparse(parts)
    anchor = document.querySelector(f'{selector} a')
    anchor.href = uri
    anchor.text = sub(r'([/+])', r'\1' + '\u200B', uri)

for sel, pth, _, _, in data:
    put_query(sel, pth) # initially empty queries

# Fires on every change (typing, paste, delete)
# Alternative: only after each key press (ignores mouse paste)
# @when("keyup", "#inp")
@when("input", "#inp")
def on_input(evt):
    value = document.querySelector("#inp").value
    for sel, pth, par, key, in data:
        put_query(sel, pth, par | { key: value, } )


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
