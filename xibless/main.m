#import <Cocoa/Cocoa.h>
#import <Python.h>
#import <wchar.h>
#import "MainMenu_UI.h"
#import "MainWindow.h"

int main(int argc, char *argv[])
{
    NSAutoreleasePool *pool = [[NSAutoreleasePool alloc] init];
    NSString *respath = [[NSBundle mainBundle] resourcePath];
    NSString *pypath = [respath stringByAppendingPathComponent:@"py"];
    NSString *mainpy = [pypath stringByAppendingPathComponent:@"pyplugin.py"];
    wchar_t wPythonPath[PATH_MAX+1];
    mbstowcs(wPythonPath, [pypath fileSystemRepresentation], PATH_MAX+1);
    Py_SetPath(wPythonPath);
    Py_Initialize();
    FILE* fp = fopen([mainpy UTF8String], "r");
    PyRun_SimpleFile(fp, "pyplugin.py");
    fclose(fp);
    [NSApplication sharedApplication];
    NSMenu *mainMenu = createMainMenu_UI(nil);
    [NSApp setMainMenu:mainMenu];
    MainWindow *mainWindow = [[MainWindow alloc] init];
    [mainWindow showWindow:nil];
    [NSApp run];
    Py_Finalize();
    [pool release];
    return 0;
}
