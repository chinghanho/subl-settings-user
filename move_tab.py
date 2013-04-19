import sublime_plugin


class MoveTab(sublime_plugin.TextCommand):
    def run(self, edit, mod):
        view = self.view
        window = view.window()
        group_index, tab_index = window.get_view_index(view)
        view.window().set_view_index(view, group_index,
            (tab_index + int(mod)) % len (
                view.window().views_in_group(group_index)) )
