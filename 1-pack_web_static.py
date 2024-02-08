#!/usr/bin/python3
# Fabric script to generate .tgz archive from web_static dir

from fabric.api import *
from datetime import datetime


def do_pack():
    """generate a .tgz archive"""

    timestamp = datetime.utcnow().strftime('%Y%m%d%H%M%S')
    local('mkdir -p versions')

    # create archive name
    archive_name = 'web_static_{}.tgz'.format(timestamp)
    archive_path = 'versions/{}'.format('archive_name')

    result = local('tar -cvzf {} web_static'.format(archive_path))

    # check and return archive path if succesful
    if result:
        return archive_path
    return None


if __name__ == "__main__":
    do_pack()
