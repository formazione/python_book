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
import time

class Win:
    def __init__(self, title, version, folder, extension):
        self.extension = extension
        self.letter_size = 16
        self.root = tk.Tk()
        self.filename= ""
        self.folder = folder
        self.root.title(f"{title}.{version}")
        self.window()
        self.binding()
        self.expand_widgets()

    def expand_widgets(self):
        # tk.Grid.rowconfigure(self.root, 0, weight=1)
        tk.Grid.rowconfigure(self.root, 1, weight=1)
        tk.Grid.columnconfigure(self.root, 0, weight=1)

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

    def popup(self,
        title="",
        sentence=""):
        "Simple wrapper function for messagebox.showinfo"

        tk.Tk().withdraw()
        name = messagebox.showinfo(
                title=title,
                message=sentence)

    def save(self):
        "Saves the file selected in the listbox"
        if self.filename != "":
            try:
                with open(f"{self.folder}/{self.filename}", "w") as file:
                    file.write(self._text.get("0.0", tk.END))
            except:

                self.popup("Message", "Nothing selected")


    def delete(self):
        try:
            cur = self._lbx.curselection()
            for i in cur:
                self.filename = self._lbx.get(i)
                os.remove(f"{self.folder}/{self.filename}")
                print(f"Deleted {self.folder}/{self.filename}")
            self.showlistitems()
        except OSError as e:
                    print("Failed with:" , e.sterror)
                    print("Error code:" , e.code)


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

    def run(self, evt):
        print("ok")
        print("Running: " + self.folder + "\\" + self.filename)
        os.startfile(f"{self.folder}\\{self.filename}")


    def binding(self):
        self.root.protocol("WM_DELETE_WINDOW", self.quit)
        self.root.bind("<Control-n>", self.newfile)
        self.root.bind("<Escape>", self.quit)
        self._lbx.bind("<<ListboxSelect>>", self.showcontent)
        self._lbx.bind("<Double-Button-1>", self.run)
        self._lbx.bind("<B1-Motion>", self.multiple_select)
        self._text.bind("<Control-s>", lambda x: self.save())
        self._text.bind("<Control-MouseWheel>", self.wheel)

    def multiple_select(self, evt):
        print("Hello")

    def open_folder(self):
    	# print(self.filename)
    	os.startfile(self.folder)

    def quit(self, evt=""):
    	#self.save()
    	self.root.destroy()

    def newfile(self, evt):
        "Create a new file"
        self.save()
        self.newfilename = self.input_filename()
        if newfilename != "":
            with open(f"snippets/{self.newfilename}", "w") as file:
                pass
            self._lbx.insert(0, self.newfilename)


    def newfile2(self):
        "Create a new file"
        self.save()
        newfilename = self.input_filename()
        if newfilename != "":
            with open(f"{self.folder}/{newfilename}", "w") as file:
                pass
            self._lbx.insert(0, newfilename)
        return newfilename

    def showlistitems(self):
        self._lbx.delete(0, tk.END)
        list_of_items = os.listdir(f"{self.folder}")
        list_of_items.sort()
        for file in list_of_items:
            if file.endswith(self.extension):
                self._lbx.insert(0, file)
        self._lbx.focus()
    
    def window(self):
        "Contains all the widgets"
        
        def frame0():
            "Contains the text"
            self._frame0 = tk.Frame(self.root, bg="gold")
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
            img = tk.PhotoImage(file=f"{self.folder}/banner.png")
            self.lb_banner = tk.Label(self._frame0, image=img, bg="yellow")
            self.lb_banner.image = img
            self.lb_banner.grid(
                column=0,
                row=0,
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
            self._frame2 = tk.Frame(self.root, bg="gold")
            self._frame2.grid(column=1, row=1, sticky="nswe" )
            self._frame2.grid_rowconfigure(0, weight=1)
            # self._frame2.grid_rowconfigure(1, weight=1)
            self._frame2.grid_columnconfigure(0, weight=1)
        

        def listbox():
            "The book chapter name list goes here"
            self._lbx = tk.Listbox(
                self._frame,
                bg="yellow",
                selectmode=tk.MULTIPLE)
            self._lbx.grid(
                column=0,
                row=0,
                sticky="nswe"
                ) # adapt the listbox to the frame
            self._lbx.configure(selectmode="")
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
                sticky="nswe"
                ) # adapt the listbox to the frame

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
            listbox()
            button("save", 0, 1, self.save)
            button("new", 0, 2, self.newfile2)
            button("delete", 0, 3, self.delete)
            button("open fld", 0, 4, self.open_folder)
            button("Files .py", 0, 5, lambda: self.new_file_extension(".py"))
            button("Files .txt", 0, 6, lambda: self.new_file_extension(".txt"))
            button("Join", 0, 7, self.join)
            button("CLEAR", 0, 8, self.clear)
            scrollbars()
            text()
            
        widgets_order()

    def write_in_text(self, text):
        self._text.delete("0.0", tk.END)
        self._text.insert(tk.END, text)
        # self._lbx.config(state="normal")

    def join(self):
        print("Joining all files")
        text = ""
        # self._lbx.config(state=tk.DISABLED)
        list_files = [f for f in os.listdir("snippets/") if f.endswith(self.extension)]
        print(list_files)
        list_files.sort()
        for file in list_files:
            with open(f"snippets/{file}") as file_to_add:
                text += file.split(".")[0] + "\n=========\n"
                text += file_to_add.read()
            text += "\n\n\n\n\n"
        self.write_in_text(text)
        # self.nf = self.newfile2()
        # self.save()

    
    def exension(self, ext):
        self.extension = ext
        self.showlistitems()

    def showcontent(self, evt):
        self._lbx.focus_set()
        #self.save()
        try:
            filenum = self._lbx.curselection()
            self.filename = self._lbx.get(filenum)
            with open(f"{self.folder}/{self.filename}") as file:
                content = file.read()
            self._text.delete("0.0", tk.END)
            self._text.insert(tk.END, content)
        except:
            self.save()

    def clear(self):
        self._text.delete("0.0", tk.END)
        self.save()

def create_chapters_folder(folder):
    "Create the folder for the snippets if not exists"
    if folder not in os.listdir():
        os.mkdir(folder)
        print("Created a folder named chatpters")

def console_intro():
    print("""
Save your chapters in chapters folder
""")

# ================ main ============
if __name__ == "__main__":
    console_intro()
    ###########################################################
    # CHOOSE TYPE OF FILE AND THE FOLDER WHERE YOU STORE THEM #
    #
    #  In case you want to store txt files change to .txt the
    #  FILE_EXTENSION costant.
    #  If you need to change the name of the folder where to
    #  search or save the files change the FOLDER_FOR_FILES
    #  value to the name of the folder you want
    #  
    #                  https://pythonprogramming.altervista.org
    #°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°
    FOLDER_FOR_FILES = "snippets"
    FILE_EXTENSION = ".txt"
    #°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°
    create_chapters_folder(FOLDER_FOR_FILES)
    ver = "0.1"
    win = Win(__file__, "1.1",
        folder=FOLDER_FOR_FILES,
        extension=FILE_EXTENSION)
    win.root.mainloop()