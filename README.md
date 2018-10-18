# Astroid Mail Processing Example Plugin

## Description

The purpose of this plugin is to demonstrate the capabilities of processing
mails arbitrarily before they are passed to Astroid. The plugin is given the
name of the file that contains the email, reads it, and passes the `GMimeStream`
to Astroid.

The example adds a `plain/text` part to emails that don't have it by rendering
the HTML part to text. This is only a basic plugin without checking whether an
HTML part exists, whether it is signed, etc.

In general, this plugin allows you to change arbitray things, e.g. rewrite
headers, or filter parts of the email.

## Installation

Clone the folder or repository of the plugin you want to install to your `~/.config/astroid/plugins/` directory.
