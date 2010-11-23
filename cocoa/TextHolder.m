#import "TextHolder.h"

@implementation TextHolder
- (id)initWithTextField:(NSTextField *)aTextField
{
    self = [super init];
    NSString *pluginPath = [[NSBundle mainBundle] pathForResource:@"pyplugin" ofType:@"plugin"];
    NSBundle *pluginBundle = [NSBundle bundleWithPath:pluginPath];
    Class PyTextHolder = [pluginBundle classNamed:@"PyTextHolder"];
    py = [[PyTextHolder alloc] initWithView:self];
    textField = [aTextField retain];
    [[NSNotificationCenter defaultCenter] addObserver:self selector:@selector(textDidChange:)
        name:NSControlTextDidChangeNotification object:nil];
    return self;
}

- (void)dealloc
{
    [py release];
    [textField release];
    [super dealloc];
}

- (PyTextHolder *)py
{
    return py;
}

- (void)textDidChange:(NSNotification *)aNotification
{
    [py setText:[textField stringValue]];
}

// model --> view
- (void)updateText
{
    [textField setStringValue:[py text]];
}
@end