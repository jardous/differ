from subprocess import Popen

from fman import DirectoryPaneCommand


DIFF_COMMAND = "meld"


class ShowDiff(DirectoryPaneCommand):
    def __call__(self):
        l_pane, r_pane = self.pane.window.get_panes()

        l_url = l_pane.get_file_under_cursor()
        if (l_pane.get_selected_files()):
            l_url = " ".join(l_pane.get_selected_files())

        r_url = r_pane.get_file_under_cursor()
        if (r_pane.get_selected_files()):
            r_url = " ".join(r_pane.get_selected_files())

        Popen([DIFF_COMMAND, l_url, r_url])
