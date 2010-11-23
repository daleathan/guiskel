#import <Cocoa/Cocoa.h>
#import "TextHolder.h"
#import "PyInter.h"

@interface MainWindow : NSWindowController
{
    IBOutlet NSTextField *nameTextField;
    IBOutlet NSTextField *msgTextField;
    
    PyMainWindow *py;
    TextHolder *nameTextHolder;
    TextHolder *msgTextHolder;
}

- (IBAction)randomName:(id)sender;
- (IBAction)sayHello:(id)sender;
@end