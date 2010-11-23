#import <Cocoa/Cocoa.h>
#import "PyInter.h"

@interface TextHolder : NSObject
{
    NSTextField *textField;
    PyTextHolder *py;
}
- (id)initWithTextField:(NSTextField *)aTextField;
- (PyTextHolder *)py;
@end