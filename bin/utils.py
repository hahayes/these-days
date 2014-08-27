import json
import shutil
import os.path
import inspect

def lazypath(basedir, filename=''):
    curdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    return os.path.abspath(os.path.join(curdir, '..', basedir, filename))

def data_load(outfile):
    try:
        items = json.load(open(outfile))
    except (IOError, ValueError):
        items = []
    return items

def data_dump(item, outfile):
    items = data_load(outfile)
    items.append(item)
    json.dump(items, open(outfile, 'w'))

def copytree(src, dst, symlinks=False, ignore=None):
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            shutil.copytree(s, d, symlinks, ignore)
        else:
            shutil.copy2(s, d)

def init_browser(indir, outdir):
    copytree(indir, outdir)
