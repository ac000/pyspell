#!/usr/bin/env python
#
# 2009-08-22
# Andrew Clayton <andrew@digital-domain.net>
#
# pyspell.py - A simple python frontend to hunspell
#
# License: GNU GPLv2. See COPYiNG
#

import pygtk
pygtk.require('2.0')
import gtk, pango
from subprocess import Popen, PIPE

class Display:

	def close_application(self, widget):
		gtk.main_quit()

	def read_file(self, widget, entry, textbuffer, textview):
		word = entry.get_text()	

		pipe = Popen("echo "+word+" | hunspell -d en_GB", 
			shell=True, bufsize=0, stdout=PIPE, close_fds=True)
		pfd = pipe.stdout
		textbuffer.set_text(pfd.read())

	def __init__(self):
		window = gtk.Window(gtk.WINDOW_TOPLEVEL)
		window.set_resizable(True)  
		window.connect("destroy", self.close_application)
		window.set_border_width(0)
	
		window.resize(800, 200)
		window.set_title("pyspell")


		box1 = gtk.VBox(False, 0)
		window.add(box1)
		box1.show()

		box2 = gtk.VBox(False, 10)
		box2.set_border_width(10)
		box1.pack_start(box2, True, True, 0)
		box2.show()

		sw = gtk.ScrolledWindow()
		sw.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_AUTOMATIC)
		textview = gtk.TextView()
		textview.set_editable(False)
		textview.set_cursor_visible(False)
		textbuffer = textview.get_buffer()
		sw.add(textview)
		sw.show()
		textview.show()

		box2.pack_start(sw)

		hbox = gtk.HButtonBox()
		box2.pack_start(hbox, False, False, 0)
		hbox.show()

		hbox3 = gtk.HBox()
		hbox3.show()
		hbox.pack_start(hbox3, False, False, 0)
       
		frame = gtk.Frame()
		label = gtk.Label("Lookup: ")
		frame.add(label)
		hbox3.pack_start(frame, False, False, 0)
		frame.show()
		label.show()

		entry = gtk.Entry()
		entry.set_max_length(25)
		entry.connect("activate", self.read_file, entry, 
							textbuffer, textview)
		hbox3.pack_start(entry, True, True, 0)
		entry.grab_focus()
		entry.show()
		
		vbox = gtk.VBox()
		vbox.show()
		hbox.pack_start(vbox, False, False, 0)
		
		separator = gtk.HSeparator()
		box1.pack_start(separator, False, True, 0)
		separator.show()

		box2 = gtk.HBox()
		box2.set_border_width(10)
		box1.pack_start(box2, False, True, 0)
		box2.show()

		button = gtk.Button("close")
		button.connect("clicked", self.close_application)
		box2.pack_end(button, False, False, 0)
		button.set_flags(gtk.CAN_DEFAULT)
		button.grab_default()
		button.show()

		textview.modify_font(pango.FontDescription("Monospace"))
	
		window.show()
	

def main():
	gtk.main()
	return 0       


if __name__ == "__main__":
	Display()
	main()
