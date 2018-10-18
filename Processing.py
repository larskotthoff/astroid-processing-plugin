#!/usr/bin/env python3

import gi
gi.require_version ('Astroid', '0.2')
gi.require_version ('Gtk', '3.0')
gi.require_version ('GMime', '2.6')

from gi.repository import GObject
from gi.repository import Gtk
from gi.repository import Astroid
from gi.repository import GMime

import email
import os
import mimetypes
import re
import html2text

from email.policy import default

class ProcessingPlugin(GObject.Object, Astroid.Activatable):
  def do_activate(self):
    print('Processing Plugin: activated', __file__)

  def do_deactivate(self):
    print('Processing Plugin: deactivated')

  def do_process(self, fname):
    with open(fname, 'rb') as fp:
      msg = email.message_from_binary_file(fp, policy = default)
      

      plain = msg.get_body("text/plain")
      # add a text/plain part with the rendered HTML part if there is nonw
      if plain == None:
        html = msg.get_body("text/html")
        html.add_alternative(html2text.html2text(html.get_content()), subtype = "plain")
        plain = msg.get_body("text/plain")
        plain.replace_header("Content-Type", "text/plain; charset=\"utf-8\"")

      return GMime.StreamMem.new_with_buffer(msg.as_bytes());
