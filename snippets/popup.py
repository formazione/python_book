from tkinter import messagebox    

class Win:
    def popup(self,
        title="...",
        sentence="..."):

        #tk.Tk().withdraw()
        name = messagebox.showinfo(
            title=title, message=sentence)

Win().popup("Alert", "This is a message")













