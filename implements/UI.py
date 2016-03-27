#!/usr/bin/env python

import sys
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
builder = Gtk.Builder()
builder.add_from_file("UI.glade")
window = builder.get_object("Main")
window.show_all()
Gtk.main()
