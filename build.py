import sys
import os
import os.path as op
import shutil

PROJNAMES = ['qt', 'cocoa', 'tk']

def build_cocoa():
    import objp.o2p
    import objp.p2o
    sys.path.insert(0, 'cocoa')
    import pyplugin
    objp.o2p.generate_objc_code(pyplugin.PyMainWindow, 'cocoa/autogen')
    objp.o2p.generate_objc_code(pyplugin.PyTextHolder, 'cocoa/autogen')
    objp.p2o.generate_python_proxy_code('cocoa/TextHolderView.h', 'build/TextHolderView.m')
    from setuptools import setup, Extension
    exts = [
        Extension("TextHolderView", ['build/TextHolderView.m', 'build/ObjP.m'],
            extra_link_args=["-framework", "Foundation"]),
    ]
    setup(
        script_args = ['build_ext', '--inplace'],
        ext_modules = exts,
    )
    pydest = 'build/py'
    if not op.exists(pydest):
        os.mkdir(pydest)
    shutil.copy('TextHolderView.so', pydest)
    shutil.copy('cocoa/pyplugin.py', pydest)
    # For some strange reason, a "site.py" file is required at pydest.
    with open(op.join(pydest, 'site.py'), 'w'):
        pass
    from pluginbuilder import copy_embeddable_python_dylib, get_python_header_folder, collect_dependencies
    copy_embeddable_python_dylib('build')
    if not op.exists('build/PythonHeaders'):
        os.symlink(get_python_header_folder(), 'build/PythonHeaders')
    collect_dependencies('cocoa/pyplugin.py', pydest)

def main(projname):
    if projname == 'cocoa':
        build_cocoa()
    runtemplate_path = op.join(projname, 'runtemplate.py')
    shutil.copy(runtemplate_path, 'run.py')

if __name__ == '__main__':
    if len(sys.argv) != 2 or sys.argv[1] not in PROJNAMES:
        print("Usage: python build.py [project name]")
        print("Possible project names: {}".format(', '.join(PROJNAMES)))
        sys.exit()
    main(sys.argv[1])
