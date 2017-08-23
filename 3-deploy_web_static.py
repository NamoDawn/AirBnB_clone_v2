#!/usr/bin/python3
from fabric.api import *
from datetime import datetime
from os import path

''' script that creates and distributes an archive to your web servers '''


env.hosts = ["66.70.184.34",
             "184.73.87.120"]


def deploy():
    ''' script that creates and distributes an archive '''
    path = do_pack()
    return(do_deploy(path))


def do_pack():
    ''' generates a .tgz archive '''
    format = "%Y%m%d%H%M%S"
    time = datetime.utcnow().strftime(format)
    local("mkdir -p ./versions")
    arch_path = local('tar -zcvf versions/web_static_{}.tgz web_static'.format
                      (time))
    if arch_path.failed:
        return(None)
    return("versions/web_static_{}.tgz".format(time))


def do_deploy(archive_path):
    ''' distributes an archive '''

    if not path.isfile(archive_path):
        return False

    try:
        put(archive_path, "/tmp")

        release_archive = archive_path.split("/")[1]
        release_folder = release_archive.split(".")[0]

        run("tar zxvf /tmp/{} && rm /tmp/{}".format
            (release_archive, release_archive))
        run("mv web_static /data/web_static/releases/{}".format
            (release_folder))
        run("rm -rf /data/web_static/current")
        run("ln -sf /data/web_static/releases/{} /data/web_static/current".
            format(release_folder))

        return True
    except:
        return False
