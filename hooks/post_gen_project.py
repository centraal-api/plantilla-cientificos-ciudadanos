import os
import stat
import shutil
import pathlib


def force_delete(func, path, _):
    """Error handler for `shutil.rmtree()` equivalent to `rm -rf`.
    Usage: `shutil.rmtree(path, onerror=force_delete)`
    From https://docs.python.org/3/library/shutil.html#rmtree-example
    """
    os.chmod(path, stat.S_IWRITE)
    func(path)


def rmtree(path):
    """Remove a directory and all its contents. Like rm -rf on Unix.
    :param path: A directory path.
    """
    shutil.rmtree(path, onerror=force_delete)


path = "{{cookiecutter.nombre_notebook}}"
os.chdir("..")
p = pathlib.Path("{{cookiecutter.nombre_notebook}}")
f = p.joinpath("{{cookiecutter.nombre_notebook}}.ipynb")
f.rename("./{{cookiecutter.nombre_notebook}}.ipynb")
del p
del f

rmtree(path)
