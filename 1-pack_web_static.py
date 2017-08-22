#!/usr/bin/python3
from fabric.api import *
from datetime import datetime
''' script to generate .tgz archive from contents of web_static folder'''


def do_pack():
    ''' generates a .tgz archive '''
    format = "%Y%m%d%H%M%S"
    time = datetime.utcnow().strftime(format)
    local("mkdir -p ./versions")
    arch_path = local('tar -zcvf versions/web_static_{}.tgz web_static'.format
                      (time))
    if arch_path.failed:
        return(None)
    return("versions/web_static_{}.tgz web_static.format(time)")
