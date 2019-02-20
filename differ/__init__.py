from subprocess import Popen

from fman import DirectoryPaneCommand


DIFF_COMMAND = "meld"


class ShowDiff(DirectoryPaneCommand):
    def __call__(self):
        l_url = self.pane.get_file_under_cursor()
        if (self.pane.get_selected_files()):
            l_url = " ".join(self.pane.get_selected_files())

        r_url = self._get_opposite_pane().get_file_under_cursor()
        if (self._get_opposite_pane().get_selected_files()):
            r_url = " ".join(self._get_opposite_pane().get_selected_files())

        Popen([DIFF_COMMAND, l_url, r_url])

    def _get_opposite_pane(self):
        panes = self.pane.window.get_panes()
        return list(filter(lambda p: p != self.pane, panes))[0]
