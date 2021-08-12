import tkinter as tk
import os
from tkinter import simpledialog
from tkinter import messagebox
from PIL import Image, ImageTk
import time
# my own modules
from code.binding import binding
from code.window import window

# dependencies ############################################
#   binding.py        to control user inputs
    #   letter.py         to increase/decrease font-size
#   widows.py         shows the widgets (buttons made with buttons.py)
    #   buttons.py        display the buttons on the left
# #########################################################

''' 
2905 - you can open images
2902

        self.define_menu()
        self.menu_voices()

    def define_menu(self):
        "17.01.2021 - added menubar to the root"
        self.menubar = tk.Menu(self.root)
        self.root.config(menu=self.menubar)
        
    def add_menu(self, text, command=None):
        "17.01.2021 - self.add_menu to add a menu to the menubar"
        # ex: add_menu("New", self.new) # it adds a new menu called New
        self.menubar.add_command(label=text, command=command)

    def menu_voices(self):
        "List of all the voices of the menubar"
        self.add_menu(
            "Hello",
            lambda: popup(
                "Hello",
                "This is just an example",
                parent=self.root)
            )


'''

popup = messagebox.showinfo

class Win:
    def __init__(self, title, version, folder, extension):
        self.extension = extension
        self.letter_size = 16
        self.root = tk.Tk()
        self.filename= ""
        self.folder = folder
        self.root.title(f"Python_book ver. {version}")
        window(self)
        binding(self) # code/binding.py code/letters.py
        self.expand_widgets()
        self.define_menu()
        self.menu_voices()
        
    def define_menu(self):
        "17.01.2021 - added menubar to the root"
        self.menubar = tk.Menu(self.root)
        self.root.config(menu=self.menubar)

    def change_extension(self, ext):
        self.extension = ext
        self.showlistitems()

    def menu_voices(self):
        "List of all the voices of the menubar"

        voices = [
            # voice, command
            [ # popup with info about the app
            "About",
            lambda: popup("Credits", "pythonprogramming.altervista.org \nv.2.9.0.2", parent=self.root)], 
            # next voice
            ["Blog",
            lambda: os.startfile("https://pythonprogramming.altervista.org/wp-admin")],

                        ["PNG", lambda: self.change_extension(".png")]
        ]

        def show_voices():
            "Shows the menu items above in the list voices"
            for v in voices:
                self.menubar.add_command(label=v[0], command=v[1])
        show_voices()


    def get_text(self):
        _sel = self._text.selection_get()
        print(_sel)

    def expand_widgets(self):
        "Make the button and text expandable"
        tk.Grid.rowconfigure(self.root, 1, weight=1)
        tk.Grid.columnconfigure(self.root, 0, weight=1, minsize=100)

    def save(self):
        # "Saves the file selected in the listbox"
        if self.filename != "":
            try:
                with open(f"{self.folder}/{self.filename}", "w") as file:
                    file.write(self._text.get("0.0", tk.END))
            except:

                self.popup("Message", "Nothing selected")

    def delete(self):
        try:
            self.filename = self._lbx.get(self._lbx.curselection())
            os.remove(f"{self.folder}/{self.filename}")
            print(f"Deleted {self.folder}/{self.filename}")
            self.showlistitems()
        except OSError as e:
                    print("Failed with:" , e.sterror)
                    print("Error code:" , e.code)
        self._text.delete("0.0", tk.END)

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
        "Double click to run the python scripts"
        print("ok")
        print(f"{self.filename=}")
        print("Running: " + self.folder + "\\" + self.filename)
        if os.path.splitext(self.filename)[1] in ["py", "txt", "html"]:
            os.startfile(f"{self.folder}\\{self.filename}")
        else:
            print("open image code here...")
            path = f"{self.folder}\\{self.filename}"
            print(path)
            print(self.folder)
            print(self.filename)
            os.startfile(path)

    def open_folder(self):
        "Open the folder of the selected file"
        # print(self.filename)
        os.startfile(self.folder)

    def quit(self, evt=""):
        "Quit the window when press escape"
        self.save()
        self.root.destroy()

    def newfile(self, evt):
        "Create a new file"
        self.save()
        self.newfilename = self.input_filename()
        if self.newfilename != "":
            with open(f"snippets/{self.newfilename}", "w", encoding="utf-8") as file:
                pass
            self._lbx.insert(0, self.newfilename)

    def newfile2(self):
        "Create a new file"
        self.save()
        self.newfilename = self.input_filename()
        if self.newfilename != "":
            with open(f"{self.folder}/{self.newfilename}", "w", encoding="utf-8") as file:
                pass
            self._lbx.insert(0, self.newfilename)
        return self.newfilename

    def showlistitems(self):
        self._lbx.delete(0, tk.END)
        list_of_items = os.listdir(f"{self.folder}")
        list_of_items.sort(reverse=True)
        # print(list_of_items)
        for file in list_of_items:
            if file.endswith(self.extension.lower()) or file.endswith(self.extension.upper()):
                self._lbx.insert(0, file)
        self._lbx.focus()

    def write_in_text(self, text):
        self._text.delete("0.0", tk.END)
        self._text.insert(tk.END, text)

    def join(self):
        print("Joining all files")
        text = ""
        # self._lbx.config(state=tk.DISABLED)
        # self._lbx.selection_clear(0, tk.END)
        self.filename = ""
        if "ALL.txt" in os.listdir("snippets"):
            os.remove("snippets/ALL.txt")
        list_files = [f for f in os.listdir("snippets/") if f.endswith(self.extension)]
        print(list_files)
        list_files.sort()
        for file in list_files:
            with open(f"snippets/{file}", "r", encoding="utf-8") as file_to_add:
                text += file.split(".")[0] + "\n=========\n"
                text += file_to_add.read()
        with open("snippets/ALL.txt", "w", encoding="utf-8") as file:
            file.write(text)
        self._lbx.insert(0, "ALL.txt")
        # self.write_in_text()
        self.showlistitems()
        self._lbx.select_set(tk.END)
        self.write_in_text(text)

        # self.nf = self.newfile2()
        self.save()

    def new_file_extension(self, ext):
        self.extension = ext
        self.showlistitems()

    def show_img_win2(self):
        "Shows the image when you select from showcontent"
        img = ImageTk.PhotoImage(file=f"snippets/{self.filename}")
        self.imgviewer = tk.Label(
            self.win2,
            image = img)
        self.imgviewer.grid(column=0, row=0, sticky="n")
        self.win2.geometry(f"{img.width()}x{img.height()}")
        self.image = img

    def showcontent(self, evt):
        if self.extension != ".png":
            # self.save()
            try:
                filenum = self._lbx.curselection()
                self.filename = self._lbx.get(filenum)
                with open(f"{self.folder}/{self.filename}", "r", encoding="utf-8") as file:
                    content = file.read()
                self._text.delete("0.0", tk.END)
                self._text.insert(tk.END, content)
            except:
                pass
                # self.save()
        else:
            filenum = self._lbx.curselection()
            self.filename = self._lbx.get(filenum)
            try:
                if self.win2.state() == "normal":
                    self.show_img_win2()
            except:     
                self.win2 = tk.Toplevel(self.root)
                self._lbx.focus_set()
                print("You selected and image" + self.filename)
                self.show_img_win2()
        self.lb_under_banner["text"] = "File selected: " + self.filename

    def clear(self):
        self._text.delete("0.0", tk.END)
        self.save()

    def copy(self):
        pass



def create_chapters_folder(folder):
    "Create snippets folder in case it does not exist"
    if folder not in os.listdir():
        os.mkdir(folder)
        print("Created a folder named chatpters")


# ================ main ============
if __name__ == "__main__":
    # This is where the files in the list are
    FOLDER_FOR_FILES = "snippets"
    # This is the extension that you see in the list first
    FILE_EXTENSION = ".py"
    # in case there is not the folder in the root 
    create_chapters_folder(FOLDER_FOR_FILES)
    ver = "2.9.0.2"
    win = Win(__file__, ver,
        folder=FOLDER_FOR_FILES,
        extension=FILE_EXTENSION)
    win.root.mainloop()

