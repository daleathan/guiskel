import sys
import os
import os.path as op
import shutil

PROJNAMES = ['qt', 'cocoa']

def main(projname):
    if projname == 'cocoa':
        from setuptools import setup
        setup(
            script_args = ['py2app'],
            plugin = ['cocoa/pyplugin.py'],
            setup_requires = ['py2app'],
        )
        pluginpath = 'cocoa/pyplugin.plugin'
        if op.exists(pluginpath):
            shutil.rmtree(pluginpath)
        shutil.move('dist/pyplugin.plugin', pluginpath)
        os.chdir('cocoa')
        os.system('xcodebuild')
        os.chdir('..')
    runtemplate_path = op.join(projname, 'runtemplate.py')
    shutil.copy(runtemplate_path, 'run.py')

if __name__ == '__main__':
    if len(sys.argv) != 2 or sys.argv[1] not in PROJNAMES:
        print("Usage: python build.py [project name]")
        print("Possible project names: {}".format(', '.join(PROJNAMES)))
        sys.exit()
    main(sys.argv[1])
