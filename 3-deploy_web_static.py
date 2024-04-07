#!/usr/bin/python3
"""
Script to create and distribute an archive to the 
web servers
"""

from fabric.api import put, run, env, local
from os.path import exists, isdir
from datetime import datetime
env.hosts = ['35.153.33.193', '54.174.11.67']


def dopack():
    """generates an archive to my web servers"""

    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        if isdir("versions") is False:
            local("mkdir versions")
        file_n = "versions/web_static{}.tgz".format(date)
        local("tar -cvzf {} web_static".format(file_n))
        return file_n
    except:
        return None

def do_deploy(archive_path):
    """distributes an archive to my web servers"""


    if exists(archive_path) is False:
        return False
    try:
        file_name = archive_path.split("/")[-1]
        no_ext = file_name.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(path, no_ext))
        run('tar -xzf /tmp/{} -C {}{}/'.format(file_name, path, no_ext))
        run('rm /tmp/{}'.format(file_name))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, no_ext))
        run('rm -rf {}{}/web_static'.format(path, no_ext))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, no_ext))
        return True
    except:
        return False


def deploy():
    """creates and distributes an archive to the web servers"""

    archive_path = dopack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)