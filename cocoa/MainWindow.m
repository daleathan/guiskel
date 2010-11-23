#import "MainWindow.h"

@implementation MainWindow
- (void)awakeFromNib
{
    [self window];
    NSString *pluginPath = [[NSBundle mainBundle] pathForResource:@"pyplugin" ofType:@"plugin"];
    NSBundle *pluginBundle = [NSBundle bundleWithPath:pluginPath];
    [pluginBundle load];
    Class PyMainWindow = [pluginBundle classNamed:@"PyMainWindow"];
    py = [[PyMainWindow alloc] init];
    nameTextHolder = [[TextHolder alloc] initWithTextField:nameTextField];
    msgTextHolder = [[TextHolder alloc] initWithTextField:msgTextField];
    [py setNameHolder:[nameTextHolder py] andMsgHolder:[msgTextHolder py]];
}

- (void)dealloc
{
    [nameTextHolder release];
    [nameTextHolder release];
    [py release];
    [super dealloc];
}
- (IBAction)randomName:(id)sender
{
    [py selectRandomName];
}
- (IBAction)sayHello:(id)sender
{
    [py sayHello];
}
@end