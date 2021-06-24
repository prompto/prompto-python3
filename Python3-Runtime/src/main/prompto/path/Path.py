import os
import psutil
import gzip
import shutil
import tempfile

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


def compressToTempPath(path: str) -> str:
    with open(path, 'rb') as inflated:
        compressedFile = tempfile.NamedTemporaryFile("r+b", prefix="deflate", suffix=".gz", delete=False)
        with gzip.open(compressedFile, 'wb') as deflated:
            shutil.copyfileobj(inflated, deflated)
            return compressedFile.name


def decompressToTempPath(path: str) -> str:
    with gzip.open(path, 'rb') as deflated:
        rawFile = tempfile.NamedTemporaryFile("w+b", prefix="inflate", suffix=".raw", delete=False)
        with open(rawFile, 'rb') as inflated:
            shutil.copyfileobj(deflated, inflated)
            return rawFile.name