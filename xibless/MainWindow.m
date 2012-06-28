#import "MainWindow.h"
#import "MainWindow_UI.h"
#import "PyMainWindow.h"

@implementation MainWindow

@synthesize nameTextField;
@synthesize msgTextField;

- (id)init
{
    self = [super initWithWindow:nil];
    NSWindow *window = createMainWindow_UI(self);
    [self setWindow:window];
    py = [[PyMainWindow alloc] init];
    nameTextHolder = [[TextHolder alloc] initWithTextField:nameTextField];
    msgTextHolder = [[TextHolder alloc] initWithTextField:msgTextField];
    [py setNameHolder:[[nameTextHolder py] pyRef] andMsgHolder:[[msgTextHolder py] pyRef]];
    return self;
}

- (void)dealloc
{
    [nameTextHolder release];
    [nameTextHolder release];
    [py release];
    [super dealloc];
}
- (void)randomName
{
    [py selectRandomName];
}

- (void)sayHello
{
    [py sayHello];
}
@end