import os
import psutil

def listRoots() -> []:
    disks = psutil.disk_partitions()
    return [ disk.mountpoint for disk in disks ]


def listChildren(path: str) -> []:
    return os.listdir(path)


def pathExists(path: str) -> bool:
    return os.path.exists(path)


def pathIsFile(path: str) -> bool:
    return os.path.isfile(path)


def pathIsDirectory(path: str) -> bool:
    return os.path.isdir(path)


def pathIsLink(path: str) -> bool:
    return os.path.islink(path)

