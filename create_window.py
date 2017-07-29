import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class CreateWindow(Gtk.Dialog):
    def __init__(self, parent, title, message):
        Gtk.Dialog.__init__(self, title, parent, 0,
                            (Gtk.STOCK_OK, Gtk.ResponseType.OK))
        self.set_default_size(100, 100)

        label = Gtk.Label(message)

        box = self.get_content_area()
        box.add(label)
        self.show_all()
