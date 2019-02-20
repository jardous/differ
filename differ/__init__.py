import os
from subprocess import Popen

from fman import DirectoryPaneCommand


DIFF_COMMAND = "meld"


class ShowDiff(DirectoryPaneCommand):
	def __call__(self):
		l_url = self.pane.get_file_under_cursor()
		r_url = os.path.join(self._get_opposite_pane().get_path(), os.path.basename(l_url))
		Popen([DIFF_COMMAND, l_url, r_url])
	
	def _get_opposite_pane(self):
		panes = self.pane.window.get_panes()
		this_pane = panes.index(self.pane)
		return panes[(this_pane + 1) % len(panes)]