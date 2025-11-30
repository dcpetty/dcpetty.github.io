# [News](https://dcpetty.github.io/news/)

This tool was written with [PyScript](https://pyscript.net/) &mdash; a way of mixing [Python](https://docs.python.org/3/) with [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript) &mdash; for those of us comfortable with things [Pythonic](https://realpython.com/ref/glossary/pythonic/).

This tool creates a tracker-free, clickable, short [Google Search](https://www.google.com/search) link to search [Google News](https://www.google.com/news). The link updates as you enter your query.

## What I learned

- PyScript
  - I learned of PyScript ([https://pyscript.net/](https://pyscript.net/)) in an on-line post .
  - By including [`https://pyscript.net/releases/2025.11.2/core.js`](https://pyscript.net/releases/2025.11.2/core.js) (the latest version) and adding a `<script type="py"`&hellip; tag, you can embed [Python](https://docs.python.org/3/) with access to the [DOM](https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model).
  - [*Beginning PyScript*](https://docs.pyscript.net/2025.11.2/beginning-pyscript/) is a good primer.
  - The [`pyscript.when`](https://docs.pyscript.net/2025.11.2/api/#pyscriptwhen) decorator indicates that the decorated function should handle the specified events for elements with matching selectors.
  - The equivalent of [Python](https://docs.python.org/3/) [`print`](https://docs.python.org/3/library/functions.html#print) is [`pyscript.display`](https://docs.pyscript.net/2025.11.2/api/#pyscriptdisplay), which appends a `<div>` to the `target` ID.
- HTML / CSS / JavaScript
  - Because [PyScript](https://pyscript.net/) loads slowly, I made a `class="hide"` property for some elements so that &mdash; as the very last action of the [PyScript](https://pyscript.net/) &mdash; those elements initially loaded can be hidden (with `display: none;`) and other elements (`main,footer`) can be displayed (with `display: block;`).
  - I used the `@when("input", "#id")` decorator to update the '*tracker-free, clickable, short [Google Search](https://www.google.com/search) link*' as each character is entered.
  -  `news.css` is pretty standard formatting for a simple webpage. It includes one [flexbox](https://css-tricks.com/snippets/css/a-guide-to-flexbox/) for the `<label>` and `<input>`.
  -  There *is no [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)*, except what is accessed through [PyScript](https://pyscript.net/)!
- Python
  - Using [Python](https://docs.python.org/3/) in a webpage was refreshing. I could use the techniques from, *e.g.*, the [`re`](https://docs.python.org/3/library/re.html), [`sys`](https://docs.python.org/3/library/sys.html), and [`urllib.parse`](https://docs.python.org/3/library/urllib.parse.html) libraries, while also having access to [`document`](https://developer.mozilla.org/en-US/docs/Web/API/Document) and [`window`](https://developer.mozilla.org/en-US/docs/Web/API/Window) from the [DOM](https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model).
  - I refreshed my understanding of [`urlencode`](https://docs.python.org/3/library/urllib.parse.html#urllib.parse.urlencode), [`urlparse`](https://docs.python.org/3/library/urllib.parse.html#urllib.parse.urlparse), [`urlunparse`](https://docs.python.org/3/library/urllib.parse.html#urllib.parse.urlunparse) &amp; from [`urllib.parse`](https://docs.python.org/3/library/urllib.parse.html). The article [*How to encode URLs in Python*](https://www.urlencoder.io/python/) was helpful.