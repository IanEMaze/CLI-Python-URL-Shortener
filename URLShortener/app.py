import requests, os, typer, webbrowser
from dotenv import load_dotenv
from rich import print as rprint

def shortLink(url):
    # this will load variables from .env.
    load_dotenv()  

    api_key = os.getenv("api_key")

    # preferred name in the URL
    api_url = f"https://cutt.ly/api/api.php?key={api_key}&short={url}"
    # make the request
    data = requests.get(api_url).json()["url"]
    if data["status"] == 7:
        # OK, get shortened URL
        shortened_url = data["shortLink"]
        rprint(f"\n[green]URL: {url} | Shortened URL:", shortened_url)
    else:
        print("[!] Error Shortening URL:", data)

app = typer.Typer(
    add_completion=False,
    no_args_is_help=True,
    help="--------------- Python URL Shortener ---------------"
    )

@app.command()
def api_docs():
    """
    cutt.ly api documenation
    """
    webbrowser.open('https://cutt.ly/cuttly-api')

@app.command()
def short_input():
    """
    Shorten URL by manual input
    """
    url = input("\nEnter URL: ")
    shortLink(url)

if __name__ == "__main__":
    app()