#import <Cocoa/Cocoa.h>
#import "PyTextHolder.h"

@interface TextHolder : NSObject
{
    NSTextField *textField;
    PyTextHolder *py;
}
- (id)initWithTextField:(NSTextField *)aTextField;
- (PyTextHolder *)py;
@end