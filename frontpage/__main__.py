from radicli import Radicli, Arg
from . import Frontpage

cli = Radicli()
fp = Frontpage.from_config_file("config.yml")


@cli.command("download")
def download():
    """Download new data."""
    fp.download()


@cli.command("preprocess")
def preprocess():
    """Preprocess downloaded data for annotation."""
    fp.preprocess()


@cli.command("annotate")
def annotate():
    """Annotate new examples."""
    fp.annotate()


if __name__ == "__main__":
    cli.run()
