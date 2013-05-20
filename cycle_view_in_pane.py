import sublime
import sublime_plugin


class NextViewInPaneCommand(sublime_plugin.TextCommand):
    """
    Switch to the next tab in the active pane, in the order that the
    tabs are open in the pane, cycling to the first tab if called on the
    last tab. Note that this is different than the "next_view" function
    available in the ST2 API because it only cycles through tabs in the
    *active pane* rather than through all tabs in the current window.
    """
    def run(self, view):
        change_tab(self, view, 1)


class PrevViewInPaneCommand(sublime_plugin.TextCommand):
    """
    Switch to the previous tab in the active pane, in the order that the
    tabs are open in the pane, cycling to the first tab if called on the
    last tab. Note that this is different than the "prev_view" function
    available in the ST2 API because it only cycles through tabs in the
    *active pane* rather than through all tabs in the current window.
    """
    def run(self, view):
        change_tab(self, view, -1)


def change_tab(self, view, direction):
    """
    Cycle through to the next/previous tab in the active pane, in the
    order that the tabs are open in the pane.

    @param direction: 1 to navigate to next tab, -1 to navigate to
                        previous tab
    """
    window = self.view.window()
    group_index, view_index = window.get_view_index(window.active_view())
    views = window.views_in_group(group_index)
    window.focus_view(views[(view_index + direction) % len(views)])
