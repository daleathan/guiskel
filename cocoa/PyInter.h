#import <Cocoa/Cocoa.h>

@interface PyMainWindow : NSObject {}
- (void)setNameHolder:(id)nameHolder andMsgHolder:(id)msgHolder;
- (void)selectRandomName;
- (void)sayHello;
@end

@interface PyTextHolder : NSObject {}
- (id)initWithView:(id)view;
- (NSString *)text;
- (void)setText:(NSString *)text;
@end