import sublime
import sublime_plugin
import webbrowser


class UrlHighlighter(sublime_plugin.EventListener):
    # Thanks Jeff Atwood http://www.codinghorror.com/blog/2008/10/the-problem-with-urls.html
    # ^ that up here is a URL that should be matched
    URL_REGEX = "\\bhttps?://[-A-Za-z0-9+&@#/%?=~_()|!:,.;]*[-A-Za-z0-9+&@#/%=~_(|]"

    # TODO this amount should be configurable
    # TODO URL underlining should also be disableable from the config
    MAX_URLS = 200

    urls_for_view = {}
    scopes_for_view = {}
    ignored_views = []

    def on_load(self, view):
        self.update_url_highlights(view)

    def on_modified(self, view):
        self.update_url_highlights(view)

    def on_close(self, view):
        for map in [self.urls_for_view, self.scopes_for_view, self.ignored_views]:
            if view.id() in map:
                del map[view.id()]

    def update_url_highlights(self, view):
        if view.id() in UrlHighlighter.ignored_views:
            return

        self.remove_old_highlights(view)
        urls = view.find_all(UrlHighlighter.URL_REGEX)

        # Avoid slowdowns for views with too much URLs
        if len(urls) > UrlHighlighter.MAX_URLS:
            print("UrlHighlighter: ignoring view with %u URLs" % len(urls))
            UrlHighlighter.ignored_views.append(view.id())
            return

        UrlHighlighter.urls_for_view[view.id()] = urls

        # We need separate regions for each lexical scope for ST to use a proper color for the underline
        scope_map = {}
        for url in UrlHighlighter.urls_for_view[view.id()]:
            scope_name = view.scope_name(url.a)
            scope_map.setdefault(scope_name, [])
            if sublime.version() > '3000':
                scope_map[scope_name].append(sublime.Region(url.a, url.b))
            else:
                scope_map[scope_name] += [sublime.Region(pos, pos) for pos in range(url.a, url.b)]

        flags = sublime.DRAW_SOLID_UNDERLINE if sublime.version() > '3000' else sublime.DRAW_EMPTY_AS_OVERWRITE

        for scope_name in scope_map:
            view.add_regions(u'clickable-urls ' + scope_name, scope_map[scope_name], scope_name, flags=flags)
        UrlHighlighter.scopes_for_view[view.id()] = scope_map.keys()

    def remove_old_highlights(self, view):
        if view.id() in self.scopes_for_view:
            for scope_name in self.scopes_for_view[view.id()]:
                view.erase_regions(u'clickable-urls ' + scope_name)


class OpenUrlCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        if self.view.id() in UrlHighlighter.urls_for_view:
            selection = self.view.sel()[0]
            if selection.empty():
                selection = next((url for url in UrlHighlighter.urls_for_view[self.view.id()] if url.contains(selection)), None)
                if not selection:
                    return
            url = self.view.substr(selection)
            webbrowser.open(url)


class OpenAllUrlsCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        if self.view.id() in UrlHighlighter.urls_for_view:
            for url in set([self.view.substr(url_region) for url_region in UrlHighlighter.urls_for_view[self.view.id()]]):
                webbrowser.open(url)
