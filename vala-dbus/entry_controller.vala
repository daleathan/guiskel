using Gtk;

public class EntryController {
    
    private Entry entryView;
    private DTextHolder model;
    
    public EntryController(string proxy_path, Entry entryView) {
        this.entryView = entryView;
        this.model = Bus.get_proxy_sync(BusType.SESSION, DBUS_PROGID, proxy_path);
        this.entryView.changed.connect(() => {
            this.model.set_text(this.entryView.text);
        });
        this.model.update_text.connect(() => {
            this.entryView.set_text(this.model.text());
        });
    }
}
