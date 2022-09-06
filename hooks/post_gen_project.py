import os
from pathlib import Path
from shutil import copyfile


source = Path(".")
dest = Path("..")

for f in source.iterdir():
    copyfile(f, dest.joinpath(f.name))
    f.unlink()

os.chdir(dest)
os.rmdir("{{cookiecutter.nombre_notebook}}")
