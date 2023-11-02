import click

from lib import *

entire_program = EntireProgram()

@click.group()
def cli():
    pass

@cli.command()
def get_sheets():
    global entire_program
    sheet_names = entire_program.get_sheets_name()
    click.echo("See the following sheet names for the excel file.")
    for sheet_name in sheet_names:
        click.echo(sheet_name)

if __name__ == "__main__":
    # Start the program
    get_sheets()