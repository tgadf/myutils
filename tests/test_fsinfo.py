from myutils import FileInfo
from myutils import DirInfo
from os import getcwd
from os.path import abspath
import typing


def test_fileinfo_hash():
    path = abspath(__file__)
    finfo = FileInfo(path)
    assert isinstance(finfo, typing.Hashable), f"FileInfo [{finfo}] is not hashable"
    

def test_dirinfo_hash():
    path = getcwd()
    dinfo = DirInfo(path)
    assert isinstance(dinfo, typing.Hashable), f"DirInfo [{dinfo}] is not hashable"
    

def test_fileinfo():
    path = getcwd()
    dinfo = DirInfo(path)
    finfo = dinfo.join("dummy.x")

    finfo2 = FileInfo("dummy.x")
    assert finfo.name == finfo2.name, "FileInfo names are not equal!"

    finfo.touch(debug=False)
    assert finfo.exists(), f"Could not create [{finfo}]"
    finfo.rmFile(debug=False)


def test_dirinfo():
    path = getcwd()
    dinfo = DirInfo(path)
    
    path2 = getcwd()
    dinfo2 = DirInfo(path2)
    assert dinfo == dinfo2, f"DirInfo __eq__ is not working correctly: {dinfo} vs {dinfo2}"

    newdinfo = dinfo.join("test_dirinfo")
    newdinfo.mkDir(debug=False)
    assert newdinfo.exists(), f"Could not create [{newdinfo}]"
    newdinfo.rmDir(debug=False)
