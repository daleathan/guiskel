using Gtk;

public class MainWindow : Window {
    private DMainWindow model;
    private LabelController helloLabel;
    private EntryController nameEntry;
    
    public MainWindow(string proxy_path) {
        this.model = Bus.get_proxy_sync(BusType.SESSION, DBUS_PROGID, proxy_path);
        this.title = "guiskel";
        this.border_width = 10;
        this.window_position = WindowPosition.CENTER;
        this.set_default_size (350, 100);
        this.destroy.connect (Gtk.main_quit);

        var box = new Box(Orientation.VERTICAL, 5);
        this.add(box);
        var nameEntryView = new Entry();
        box.pack_start(nameEntryView, false, false, 0);
        var helloLabelView = new Label("");
        box.pack_start(helloLabelView, false, false, 0);
        var buttonBox = new Box(Orientation.HORIZONTAL, 5);
        var randomNameButton = new Button.with_label("Random Name");
        var sayHelloButton = new Button.with_label("Say Hello");
        buttonBox.pack_end(sayHelloButton, false, false, 0);
        buttonBox.pack_end(randomNameButton, false, false, 0);
        box.pack_start(buttonBox, false, false, 0);

        this.helloLabel = new LabelController(this.model.hellolabel_path(), helloLabelView);
        this.nameEntry = new EntryController(this.model.namebox_path(), nameEntryView);
        randomNameButton.clicked.connect(() => {this.model.select_random_name();});
        sayHelloButton.clicked.connect(() => {this.model.say_hello();});
    }
}