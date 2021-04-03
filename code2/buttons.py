import tkinter as tk

def buttons(self):
    "Buttons to attach to _frame on the left below the listbox"
    
    def button(text, column, row, command):
        "The book chapter name list goes here"
        but1 = tk.Button(self._frame,
            text=text,
            bg="yellow",
            command=command)
        but1.grid(
            column=column,
            row=row,
            sticky="nswe"
            ) # adapt the listbox to the frame

    button("save", 0, 1, self.save)
    button("new", 0, 2, self.newfile2)
    button("delete", 0, 3, self.delete)
    button("open fld", 0, 4, self.open_folder)
    button("Files .py", 0, 5, lambda: self.new_file_extension(".py"))
    button("Files .txt", 0, 6, lambda: self.new_file_extension(".txt"))
    button("Join", 0, 7, self.join)
    button("CLEAR", 0, 8, self.clear)
    button("Copy", 0, 9, self.copy)