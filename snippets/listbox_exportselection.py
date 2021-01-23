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

''' this is how you avoid losing selection in tkinter listbox '''
