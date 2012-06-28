#import <Cocoa/Cocoa.h>
#import "TextHolder.h"
#import "PyMainWindow.h"

@interface MainWindow : NSWindowController
{
    PyMainWindow *py;
    NSTextField *nameTextField;
    NSTextField *msgTextField;
    TextHolder *nameTextHolder;
    TextHolder *msgTextHolder;
}

@property (readwrite, retain) NSTextField *nameTextField;
@property (readwrite, retain) NSTextField *msgTextField;

- (id)init;
- (void)randomName;
- (void)sayHello;
@end