from time import sleep

import click
import requests


def check_url(url):
    try:
        response = requests.head(url)
    except requests.exceptions.ConnectionError:
        click.echo(f"ConnectionError: Can't reach {url} URL!")
        return -1
    return response.status_code


def colorize_status(url, status):
    colors = {
        2: "green",
        3: "yellow",
        4: "bright_red",
        5: "red",
    }
    click.secho(f"{url} -> {status}", fg=colors.get(status // 100, "magenta"))


@click.command()
@click.argument("urls", nargs=-1)
@click.option("--daemon", "-d", default=False, is_flag=True)
def check(urls, daemon):
    while True:
        for url in urls:
            status_code = check_url(url)
            colorize_status(url, status_code)
        if not daemon:
            break
        sleep(1)


if __name__ == '__main__':
    check()
