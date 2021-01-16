#!/bin/sh

# An example hook script to verify what is about to be pushed.  Called by "git
# push" after it has checked the remote status, but before anything has been
# pushed.  If this script exits with a non-zero status nothing will be pushed.
#
# This hook is called with the following parameters:
#
# $1 -- Name of the remote to which the push is being done
# $2 -- URL to which the push is being done
#
# If pushing without using a named remote those arguments will be equal.
#
# Information about the commits which are being pushed is supplied as lines to
# the standard input in the form:
#
#   <local ref> <local sha1> <remote ref> <remote sha1>
#
# This sample shows how to prevent push of commits where the log message starts
# with "WIP" (work in progress).

remote="$1"
url="$2"

z40=0000000000000000000000000000000000000000

while read local_ref local_sha remote_ref remote_sha
do
	if [ "$local_sha" = $z40 ]
	then
		# Handle delete
		:
	else
		if [ "$remote_sha" = $z40 ]
		then
			# New branch, examine all commits
			range="$local_sha"
		else
			# Update to existing branch, examine new commits
			range="$remote_sha..$local_sha"
		fi

		# Check for WIP commit
		commit=`git rev-list -n 1 --grep '^WIP' "$range"`
		if [ -n "$commit" ]
		then
			echo >&2 "Found WIP commit in $local_ref, not pushing"
			exit 1
		fi
	fi
done

exit 0
                                                                                                                                                                                            up("Message", "Nothing selected")

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
        "Double click to run the python scripts"
        print("ok")
        print("Running: " + self.folder + "\\" + self.filename)
        os.startfile(f"{self.folder}\\{self.filename}")

    def open_folder(self):
        "Open the folder of the selected file"
        # print(self.filename)
        os.startfile(self.folder)

    def quit(self, evt=""):
        "Quit the window when press escape"
        # self.save()
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
            with open(f"snippets/{file}") as file_to_add:
                text += file.split(".")[0] + "\n=========\n"
                text += file_to_add.read()
        with open("snippets/ALL.txt", "w") as file:
            file.write(text)
        self._lbx.insert(0, "ALL.txt")
        # self.write_in_text()
        self.showlistitems()
        self._lbx.select_set(tk.END)
        self.write_in_text(text)

        # self.nf = self.newfile2()
        # self.save()

    def new_file_extension(self, ext):
        self.extension = ext
        self.showlistitems()

    def showcontent(self, evt):
        self._lbx.focus_set()
        self.save()
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

    def copy(self):
        pass


def create_chapters_folder(folder):
    "Create snippets folder in case it does not exist"
    if folder not in os.listdir():
        os.mkdir(folder)
        print("Created a folder named chatpters")


# ================ main ============
if __name__ == "__main__":
    FOLDER_FOR_FILES = "snippets"
    FILE_EXTENSION = ".py"

    create_chapters_folder(FOLDER_FOR_FILES)
    ver = "0.1"
    win = Win(__file__, "1.1",
        folder=FOLDER_FOR_FILES,
        extension=FILE_EXTENSION)
    win.root.mainloop()

