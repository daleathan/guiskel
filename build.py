import sys
import os
import os.path as op
import shutil

PROJNAMES = ['qt', 'cocoa', 'tk', 'gtk', 'xibless']

def build_cocoa_base(cocoa_path):
    import objp.o2p
    import objp.p2o
    sys.path.insert(0, cocoa_path)
    import pyplugin
    objp.o2p.generate_objc_code(pyplugin.PyMainWindow, op.join(cocoa_path, 'autogen'))
    objp.o2p.generate_objc_code(pyplugin.PyTextHolder, op.join(cocoa_path, 'autogen'))
    textholder_spec = objp.o2p.spec_from_python_class(pyplugin.TextHolderView)
    objp.p2o.generate_python_proxy_code_from_clsspec([textholder_spec], 'build/TextHolderView.m')
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
    shutil.copy(op.join(cocoa_path, 'pyplugin.py'), pydest)
    # For some strange reason, a "site.py" file is required at pydest.
    with open(op.join(pydest, 'site.py'), 'w'):
        pass
    from pluginbuilder import copy_embeddable_python_dylib, collect_dependencies
    copy_embeddable_python_dylib('build')
    collect_dependencies(op.join(cocoa_path, 'pyplugin.py'), pydest)

def build_cocoa():
    build_cocoa_base('cocoa')
    from pluginbuilder import get_python_header_folder
    if not op.exists('build/PythonHeaders'):
        os.symlink(get_python_header_folder(), 'build/PythonHeaders')
    os.chdir('cocoa')
    os.system('xcodebuild')
    os.chdir('..')

def build_xibless():
    build_cocoa_base('xibless')
    os.chdir('xibless')
    os.system('%s waf configure' % sys.executable)
    os.system('%s waf' % sys.executable)
    os.chdir('..')

def main(projname):
    if projname == 'cocoa':
        build_cocoa()
    elif projname == 'xibless':
        build_xibless()
    runtemplate_path = op.join(projname, 'runtemplate.py')
    shutil.copy(runtemplate_path, 'run.py')

if __name__ == '__main__':
    if len(sys.argv) != 2 or sys.argv[1] not in PROJNAMES:
        print("Usage: python build.py [project name]")
        print("Possible project names: {}".format(', '.join(PROJNAMES)))
        sys.exit()
    main(sys.argv[1])
