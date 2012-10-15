# Clickable URLs

A plugin for [Sublime Text 2](http://sublimetext.com)

![Screenshot of a clickable URL](https://raw.github.com/leonid-shevtsov/ClickableUrls_SublimeText2/master/screenshot.png)

## Summary

*(Technically the URLs are not clickable per se, but openable with a key combination. Close enough!)*

This plugin underlines URLs in Sublime Text 2, and lets you open them with a keystroke (`Cmd+Enter` by default).

After you put the cursor over an URL, you can either hit `Cmd+Enter` (`Ctrl+Enter` on Windows & Linux), or select "Open URL under cursor" from the Command Palette. Instead of selecting an auto detected URL, you can select any block of text and it will also open in a browser as a URL.

There is also an "Open all URLs" command, which opens all URLs found in the current document.

**Behavior warning.** This plugin doesn't really let you *click* on a URL, and won't, until Sublime Text provides a civilized API for handling mouse clicks.

**Performance warning.** The plugin is automatically disabled if the document has more than 200 URLs, in order to avoid a massive performance hit.

## Installation

Drop the plugin into Sublime Text's Packages folder.

* * *

By [Leonid Shevtsov](http://leonid.shevtsov.me)