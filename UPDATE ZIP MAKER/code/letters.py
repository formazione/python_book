def big_letters(self):
    if self.letter_size < 72:
        self.letter_size += 2
    self._text['font'] = "Arial " + str(self.letter_size)

def small_letters(self):
    if self.letter_size > 8:
        self.letter_size -= 2
    self._text['font'] = "Arial " + str(self.letter_size)

def wheel(self, event):
    "Font size change when scroll up or down"
    if event.delta == 120:
        big_letters(self)
    else:
        small_letters(self)