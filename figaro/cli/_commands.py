"""Command line interface for Jobrunner"""

import time
import click

from figaro.cli import figaro
from figaro import lib


@figaro.command("map-files")
def map_files():
    """
    \b
    Write boxmap from cloud storage
    """

    config = lib.load_config()
    client = lib.validate_credentials(config)

    boxmap = lib.boxmap_from_root(client, config)
    lib.write_boxmap(config, boxmap)


@figaro.command("upload-files")
@click.argument("sourcelist", nargs=-1)
def upload_files(sourcelist):
    """
    \b
    Upload files to a box cloud storage
    """

    config = lib.load_config()
    boxmap = lib.load_boxmap(config)
    client = lib.validate_credentials(config)

    lib.fileupload_from_list(client, config, boxmap, sourcelist)
