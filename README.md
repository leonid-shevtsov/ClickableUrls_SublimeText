# Clickable URLs

A plugin for [Sublime Text 2 and 3](http://sublimetext.com)

![Screenshot of a clickable URL](https://raw.github.com/leonid-shevtsov/ClickableUrls_SublimeText2/master/screenshot.png)

## Summary

This plugin underlines URLs in Sublime Text, and lets you open them with a keystroke (`Cmd+Option+Enter` by default).

After you put the cursor over an URL, you can either hit `Cmd+Option+Enter` (`Ctrl+Alt+Enter` on Windows & Linux), or select "Open URL under cursor" from the Command Palette. Instead of selecting an auto detected URL, you can select any block of text and it will also open in a browser as a URL.

If you actually want to use a mouse+key combination to open URLs, you'll have to part with one of the selection modes (likely the Option-selection, which is rectangular block selection and is not used very often). See [this issue](https://github.com/leonid-shevtsov/ClickableUrls_SublimeText2/issues/2) for details and examples on how to do it. Unfortunately Sublime Text's API is not flexible with mouse bindings.

There is also an "Open all URLs" command, which opens all URLs found in the current document.

**Performance warning.** The plugin is automatically disabled if the document has more than 200 URLs, in order to avoid a massive performance hit.

## Installation

With [Package Control](http://wbond.net/sublime_packages/package_control) (look for Clickable Urls), or just drop the plugin into Sublime Text's Packages folder.

## Customising the browser

By default, Clickable URLs uses some default system browser. If it doesn't work for you, you can change the browser by setting the `clickable_urls_browser` in the `ClickableUrls.sublime-settings`
file, to which you can get from the menu.

Anything from [this list](https://docs.python.org/2/library/webbrowser.html#webbrowser.register) will work, for example:

    {
        "clickable_urls_browser": "firefox"
    }

* * *

By [Leonid Shevtsov](http://leonid.shevtsov.me)

[![Bitdeli Badge](https://d2weczhvl823v0.cloudfront.net/leonid-shevtsov/clickableurls_sublimetext/trend.png)](https://bitdeli.com/free "Bitdeli Badge")

