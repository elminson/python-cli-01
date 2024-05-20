import click
from checkdir.util import list_files

@click.command()
@click.option('--verbose', '-v', is_flag=True)
@click.option('--file_filter', '-f', default='*', type=str)
@click.argument('path')
def main(path, file_filter, verbose):
    print(f"Verbose: {verbose}")
    print(f"{list_files(path, file_filter)}")
