import click


@click.group()
def main():
    """
    CLI Tool to manipulate signatures.json file from Cobbler.
    """
    pass


@main.command("import")
def importer():
    """
    Import
    """
    pass


@main.command("export")
def exporter():
    pass


if __name__ == "__main__":
    main()
