#import <Cocoa/Cocoa.h>
#import <Python.h>

int main(int argc, char *argv[])
{
    NSAutoreleasePool *pool = [[NSAutoreleasePool alloc] init];
    NSString *respath = [[NSBundle mainBundle] resourcePath];
    NSString *pypath = [respath stringByAppendingPathComponent:@"py"];
    NSString *mainpy = [pypath stringByAppendingPathComponent:@"pyplugin.py"];
    Py_Initialize();
    FILE* fp = fopen([mainpy UTF8String], "r");
    PyRun_SimpleFile(fp, "pyplugin.py");
    fclose(fp);
    int result = NSApplicationMain(argc,  (const char **) argv);
    Py_Finalize();
    [pool release];
    return result;
}
