import tkinter as tk
from code.buttons import buttons


def window(self):
    "Contains all the widgets"
    
    def frame0():
        "Contains the text"
        self._frame0 = tk.Frame(self.root, bg="coral")
        self._frame0.grid(
            column=0,
            row=0,
            columnspan=2,
            sticky="nswe"
            )
        self._frame0.grid_rowconfigure(0, weight=0)
        self._frame0.grid_columnconfigure(0, weight=0)
        self._frame0.grid_columnconfigure(1, weight=0)
    
    def label_banner():
        "This is at 0,0 and occupies 2 column"
        img = tk.PhotoImage(file=f"{self.folder}/banner.PNG")
        self.lb_banner = tk.Label(
            self._frame0,
            image=img,
            bg="coral")
        self.lb_banner.image = img
        self.lb_banner.grid(
            column=0,
            row=0,
            columnspan=2,
            sticky="nswe"
            )

    def label_under_banner():
        "Contains the name of the file selected in the listbox on the left"
        # v. 2903 19.01.2021
        self.lb_under_banner = tk.Label(self._frame0, text=self.filename, bg="yellow")
        self.lb_under_banner.grid(
            column=0,
            row=1,
            columnspan=2,
            sticky="nswe"
            )

    def frame():
        "Contains the list of chapter names in listbox"
        self._frame = tk.Frame(self.root, bg="gray")
        self._frame.grid(column=0, row=1, sticky="nswe")
        for n in range(9):
            self._frame.grid_rowconfigure(n, weight=1)
        self._frame.grid_columnconfigure(0, weight=1)
        # self._frame.grid_columnconfigure(1, weight=1)
    
    def frame2():
        "Contains the text"
        self._frame2 = tk.Frame(self.root, bg="coral")
        self._frame2.grid(column=1, row=1, sticky="nswe" )
        self._frame2.grid_rowconfigure(0, weight=1)
        # self._frame2.grid_rowconfigure(1, weight=1)
        self._frame2.grid_columnconfigure(0, weight=1, minsize=1)
    

    def listbox():
        "The book chapter name list goes here"
        self._lbx = tk.Listbox(
            self._frame,
            bg="yellow",
            exportselection=False # To mantain the selection in the listbox when you select in the text box
            # selectmode=tk.MULTIPLE
            )
        self._lbx.grid(
            column=0,
            row=0,
            sticky="nswe"
            ) # adapt the listbox to the frame
        # self._lbx.configure(selectmode="")
        self.showlistitems()

    def scrollbars():
        self.scrollbar = tk.Scrollbar(self._frame2)
        self.scrollbar.grid(column=2, row=0,
            sticky="nswe")

    def text():
        "Contains the text of selected chapter in listbox"
        self._text = tk.Text(self._frame2, wrap=tk.WORD)
        self._text.grid(column=0, row=0, sticky="nswe")
        self._text.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self._text.yview)
        
    def widgets_order():
        "The widgets on the screen"
        frame0()
        frame()
        frame2()
        label_banner()
        label_under_banner()
        listbox()
        buttons(self) # code/buttons.py
        scrollbars()
        text()
        
    widgets_order()