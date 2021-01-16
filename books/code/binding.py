from code.letters import *


def binding(self):
    self.root.protocol("WM_DELETE_WINDOW", self.quit)
    self.root.bind("<Control-n>", self.newfile)
    self.root.bind("<Escape>", self.quit)
    self._lbx.bind("<<ListboxSelect>>", self.showcontent)
    self._lbx.bind("<Double-Button-1>", self.run)
    self._text.bind("<Control-s>", lambda x: self.save())

    # MOUSE WHELL = CONTROLS FONT SIZE (code/letters.py)
    self._text.bind("<Control-MouseWheel>", lambda evt: wheel(self, evt))