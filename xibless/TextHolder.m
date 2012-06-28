#import "TextHolder.h"
#import "ObjP.h"

@implementation TextHolder
- (id)initWithTextField:(NSTextField *)aTextField
{
    self = [super init];
    PyObject *pView = ObjP_classInstanceWithRef(@"TextHolderView", @"TextHolderView", self);
    py = [[PyTextHolder alloc] initWithView:pView];
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