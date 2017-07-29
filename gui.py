import os
import gi
from wol import Wol
from create_window import CreateWindow

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class Gui(Gtk.Window):
    save_path = os.environ['HOME'] + '/.config/wol/'

    def onCreateWindow(self, *args):
        mac_address_value = builder.get_object("MacAddress")
        if os.path.exists(self.save_path) and os.path.isfile(self.save_path + 'history'):
            file = open(self.save_path + 'history', 'r')
            with file as f:
                lines = f.readlines()
                lines = [x.strip() for x in lines]
                mac_address_value.set_text(lines[0])

    def onDeleteWindow(self, *args):
        Gtk.main_quit(*args)

    def WakeUpButton_clicked_cb(self, button):
        mac_address_value = builder.get_object("MacAddress")
        ip_address_value = builder.get_object("IpAddress")

        wol = Wol()
        if mac_address_value.get_text():
            wol.send_magic_packet(mac_address_value.get_text())
            self.save_last_used(mac_address_value.get_text(), ip_address_value.get_text())
        else:
            dialog = CreateWindow(self, "Error", "You didn't enter a MAC address.")
            dialog.run()
            dialog.destroy()

    def save_last_used(self, macaddress, ip=""):
        if not os.path.exists(self.save_path):
            os.mkdir(self.save_path)

        file = open(self.save_path + 'history', 'w')
        file.write(macaddress + "\n")
        file.write(ip + "\n")


builder = Gtk.Builder()
builder.add_from_file("main_window.glade")

builder.connect_signals(Gui())

window = builder.get_object("MainWindow")
window.set_title("Wake on lan")
window.set_resizable(False)
window.show_all()

Gtk.main()
