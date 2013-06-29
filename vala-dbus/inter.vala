
const string DBUS_PROGID = "org.hardcodedsoftware.guiskel";

[DBus (name = "org.hardcodedsoftware.guiskel.EntryPoint")]
interface DEntryPoint : Object {
    public abstract string new_main_window() throws IOError;
}

[DBus (name = "org.hardcodedsoftware.guiskel.MainWindow")]
interface DMainWindow : Object {
    public abstract string namebox_path() throws IOError;
    public abstract string hellolabel_path() throws IOError;
    public abstract void say_hello() throws IOError;
    public abstract void select_random_name() throws IOError;
}

[DBus (name = "org.hardcodedsoftware.guiskel.TextHolder")]
interface DTextHolder : Object {
    public abstract string text() throws IOError;
    public abstract void set_text(string s) throws IOError;
    
    public signal void update_text();
}
