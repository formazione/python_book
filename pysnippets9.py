# tkinter advanced: pybookgen

'''
Started: 03.12.2020 - v. 0.1

- chapter
    - chapter1.txt
    - chapter1img1.png

GUI
---------------------------------
PyEbookGen
---------------------------------
 chapter1  | text
           |

'''
# module for the gui
import tkinter as tk
# module to check files
import os
from tkinter import simpledialog
from tkinter import messagebox


class Win:
    def __init__(self, title, version, extension):
        self.extension = extension
        self.letter_size = 16
        self.root = tk.Tk()
        self.root.title(f"{title}.{version}")
        self.window()
        self.controls()

    # ==== This are for adjusting characters inside _text
    def big_letters(self):
        if self.letter_size < 72:
            self.letter_size += 2
        self._text['font'] = "Arial " + str(self.letter_size)

    def small_letters(self):
        if self.letter_size > 8:
            self.letter_size -= 2
        self._text['font'] = "Arial " + str(self.letter_size)

    def wheel(self, event):
        if event.delta == 120:
            self.big_letters()
        else:
            self.small_letters()


    def save(self):
        try:
            with open(f"snippets/{self.filename}", "w") as file:
                file.write(self._text.get("0.0", tk.END))
        except:
            self.popup("Message", "Nothing selected")


    def delete(self):
        try:
            self.filename = self._lbx.get(self._lbx.curselection())
            print(self.filename)
            ask = messagebox.askyesno(title="Delete this file",message=f"You will delete {self.filename}")
            print(ask)
            if ask:
                os.remove(f"snippets/{self.filename}")
                self.showlistitems()
        except:
            self.popup("Beware", "You must select the file to delete")

    def input_filename(self,
        title="Enter a new name",
        sentence="Do not put the extension"):

        #tk.Tk().withdraw()
        name = simpledialog.askstring(title, sentence)
        try:
            if name != "":
                return name + self.extension
        except TypeError:
            return ""

    def popup(self,
        title="",
        sentence=""):

        tk.Tk().withdraw()
        name = messagebox.showinfo(
                title=title,
                message=sentence)

    def controls(self):
        self.root.bind("<Control-n>", self.newfile)
        self._lbx.bind("<<ListboxSelect>>", self.showcontent)
        self._text.bind("<Control-s>", lambda x: self.save())
        self._text.bind("<Control-MouseWheel>", self.wheel)

    def newfile(self, evt):
        newfilename = self.input_filename()
        if newfilename != "":
            with open(f"snippets/{newfilename}", "w") as file:
                pass
            self._lbx.insert(0, newfilename)

    def newfile2(self):
        newfilename = self.input_filename()
        if newfilename != "":
            with open(f"snippets/{newfilename}", "w") as file:
                pass
            self._lbx.insert(0, newfilename)

    def showlistitems(self):
        self._lbx.delete(0, tk.END)
        for file in os.listdir("snippets"):
            if file.endswith(self.extension):
                self._lbx.insert(0, file)
    
    def window(self):
        "Contains all the widgets"
        
        def frame0():
            "Contains the text"
            self._frame0 = tk.Frame(self.root, bg="gold")
            self._frame0.grid(column=0, columnspan=2, row=0)
        
        def frame():
            "Contains the list of chapter names in listbox"
            self._frame = tk.Frame(self.root, bg="gray")
            self._frame.grid(column=0, row=1,
                sticky="NESW")
            self._frame.grid_columnconfigure(0, weight=0)
        
        def frame2():
            "Contains the text"
            self._frame2 = tk.Frame(self.root, bg="gold")
            self._frame2.grid(column=1, row=1)
        
        def label_banner():
            img = tk.PhotoImage(file="snippets/banner.png")
            self.lb_banner = tk.Label(self._frame0, image=img, bg="yellow")
            self.lb_banner.image = img
            self.lb_banner.grid(column=0, columnspan=2, row=0)

        def listbox():
            "The book chapter name list goes here"
            self._lbx = tk.Listbox(self._frame, bg="yellow")
            self._lbx.grid(
                column=0,
                row=0,
                sticky="NESW"
                ) # adapt the listbox to the frame
            
            self.showlistitems()

        def button(text, column, row, command):
            "The book chapter name list goes here"
            but1 = tk.Button(self._frame,
                text=text,
                bg="yellow",
                command=command)
            but1.grid(
                column=column,
                row=row,
                sticky="NESW"
                ) # adapt the listbox to the frame

        def scrollbars():
            self.scrollbar = tk.Scrollbar(self._frame2)
            self.scrollbar.grid(column=2, row=0,
                sticky="NESW")

        def text():
            "Contains the text of selected chapter in listbox"
            self._text = tk.Text(self._frame2, wrap=tk.WORD)
            self._text.grid(column=1, row=0)
            self._text.config(yscrollcommand=self.scrollbar.set)
            self.scrollbar.config(command=self._text.yview)
            
        def widgets_order():
            "The widgets on the screen"
            frame0()
            frame()
            frame2()
            label_banner()
            listbox()
            button("save", 0, 1, self.save)
            button("new", 0, 2, self.newfile2)
            button("delete", 0, 3, self.delete)
            scrollbars()
            text()

        widgets_order()

    def showcontent(self, evt):
        try:
            filenum = self._lbx.curselection()
            self.filename = self._lbx.get(filenum)
            with open(f"snippets/{self.filename}") as file:
                content = file.read()
            self._text.delete("0.0", tk.END)
            self._text.insert(tk.END, content)
        except:
            pass


def create_chapters_folder():
    "Create the folder for the snippets if not exists"
    if "snippets" not in os.listdir():
        os.mkdir("snippets")
        print("Created a folder named chatpters")

def console_intro():
    print("""
Save your chapters in chapters folder
""")

# ================ main ============
if __name__ == "__main__":
    console_intro()
    create_chapters_folder()
    ver = "0.1"
    win = Win("PySnippets", "0.01", extension=".py")
    win.root.mainloop()