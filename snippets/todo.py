import tkinter as tk
import os
 
 
def add(event):
    "add item to listbox with entry when Return is pressed"
 
    lst.insert(tk.END, entry.get())
    v.set("")
    save("")
 
 
def delete(event):
    "deletes items in listbox with double click on item"
    lst.delete(tk.ANCHOR)
    save("")
 
 
def save(event):
    "saves memos in listbox"
    with open("data.txt", "w") as file:
        file.write("\n".join(lv.get()))
    label["text"] = "Data saved"
 
 
def getdata():
    "grab saved data"
    if "data.txt" in os.listdir():
        with open("data.txt") as file:
            for line in file:
                lst.insert(tk.END, line.strip())
 
 
root = tk.Tk()
root.geometry("400x400+500+10")
root.title("To do list in Python")
lab1 = tk.Label(
    root, text="Enter to add items, \nSelect to delete Items, ctr+s to save")
lab1.pack()
 
v = tk.StringVar()
entry = tk.Entry(root, textvariable=v)
entry.pack()
 
 
lv = tk.Variable()
lst = tk.Listbox(root, listvariable=lv)
lst.pack()
lst.bind("<Double-Button>", delete)
 
entry.bind("<Return>", add)
root.bind("<Control-s>", save)
 
label = tk.Label(root)
label.pack()
 
# Grab the saved data
getdata()
 
root.mainloop()






