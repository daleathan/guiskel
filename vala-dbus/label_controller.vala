using Gtk;

public class LabelController {
    
    private Label labelView;
    private DTextHolder model;
    
    public LabelController(string proxy_path, Label labelView) {
        this.labelView = labelView;
        this.model = Bus.get_proxy_sync(BusType.SESSION, DBUS_PROGID, proxy_path);
        this.model.update_text.connect(() => {
            this.labelView.set_text(this.model.text());
        });
    }
}
