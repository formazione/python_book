def input_filename(self,
    title="Enter a new name",
    sentence="Do not put the extension"):

    #tk.Tk().withdraw()
    name = simpledialog.askstring(title, sentence)
    try:
        if name != "":
            return name + ".py"
    except TypeError:
        return ""
