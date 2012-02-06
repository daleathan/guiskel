#import "MainWindow.h"
#import "PyMainWindow.h"

@implementation MainWindow
- (void)awakeFromNib
{
    [self window];
    py = [[PyMainWindow alloc] init];
    nameTextHolder = [[TextHolder alloc] initWithTextField:nameTextField];
    msgTextHolder = [[TextHolder alloc] initWithTextField:msgTextField];
    [py setNameHolder:[[nameTextHolder py] pyRef] andMsgHolder:[[msgTextHolder py] pyRef]];
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