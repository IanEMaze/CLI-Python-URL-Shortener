# CLI-Python-URL-Shortener

This script uses the Cutt.ly API to shorten links

-Side note: Need to sign up to cutt.ly to get your api key to use in your .env file.

## Setup
Install Pip if not already installed

Download:
```bash
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
```
Install:
```bash
python get-pip.py
```

Install Poetry
```bash
pip install poetry
```

## Installation

After cloning the repo, run the following command to install dependencies
```bash
poetry install
```
And to activate the environment 
```bash
poetry shell
```


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
