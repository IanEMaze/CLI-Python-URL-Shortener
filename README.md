# CLI-Python-URL-Shortener

This script uses the Cutt.ly API to shorten links

## Setup
* Sign up to cutt.ly to generate your own api key
* set up .env file
* Install Typer

## Run Code
```bash
py app.py
```

```bash
 --------------- Python URL Shortener ---------------

╭─ Options ────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ --help          Show this message and exit.                                                                          │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Commands ───────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ api-docs                            cutt.ly api documenation                                                         │
│ short-input                         Shorten URL by manual input                                                      │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
```

# short-input Command
```bash
py app.py short-input

Enter URL: https://www.pythoncheatsheet.org/cheatsheet/functions

URL: https://www.pythoncheatsheet.org/cheatsheet/functions | Shortened URL: https://cutt.ly/V9XY5qL
```
