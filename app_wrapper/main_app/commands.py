import click
from flask.cli import with_appcontext
from .extensions import db

@click.command("initdb")
@with_appcontext
def initdb():
    """
    drop and recreate all collections
    """
    click.echo("Init db")
    db.drop_all()
    db.create_all()
