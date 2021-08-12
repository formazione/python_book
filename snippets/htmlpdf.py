import tkinter as tk
import pdfkit
import os


def pdf(event=""):
    filename = "my.pdf"
    content = txbx.get("0.0", tk.END)
    content = content.replace("\n", "<br>")
    pdfkit.from_string(content, filename)
    print("pdf created")
    os.startfile("my.pdf")


root = tk.Tk()
# WIDGETS: text box => Text class of tkinter (tk)

# MENU
menubar = tk.Menu(root)
menubar.add_command(label="Create pdf", command=pdf)
root.config(menu=menubar)

# LABEL
label = tk.Label(root, text="CTRL + b to make a page (use also html)")
label.pack()

# TEXT BOX
txbx = tk.Text(root, height=20, insertbackground="white")
txbx['font'] = "Arial 14"
txbx['bg'] = "black"
txbx['fg'] = "white"
txbx['borderwidth'] = 2
txbx.pack(fill=tk.BOTH, expand=1)
txbx.focus()
# Command that creates the pdf from the text
txbx.bind("<Control-b>", pdf)

root.mainloop()