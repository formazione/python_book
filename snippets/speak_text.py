# create the mp3 letters audio files
import os
from gtts import gTTS
import tkinter as tk
from pygame import mixer
import tkinter.ttk as ttk
from time import sleep

def speak(word):
    print("looking for word in dictionary")
    # print(os.listdir("audio/"))
    word = word.lower()
    if f"{word}.mp3" not in os.listdir("audio/"):
        if word != "":
            print("This is not present... creating")
            t = gTTS(word, "it")
            t.save(f"audio/{word}.mp3")
            sleep(1)
            play(word)
            print("created " + word)
            show_list()
            lbx.focus(word)
    else:
        play(word)


def show_list():
    global lbx

    lbx.delete("0", "end")
    elenco = os.listdir("audio")
    elenco.sort(reverse=False)
    for file in elenco:
        if len(file[:-4]) == 1:
            lbx.insert("end", f"")
            lbx.insert("end", f"=== [ {file[:-4]} ] ====")
        else:
            lbx.insert("end", file)

def delete(evt):
    "with control+d it deletes the sound selected"
    global Lbx

    name = lbx.get(lbx.curselection())
    print(name)
    os.remove("audio/" + name)
    lbx.delete("anchor")

def play(word):
    mixer.music.load("audio/" + word + ".mp3")
    mixer.music.play()

def start():
    global word, lbx, text

    mixer.init()
    word = ""
    def audiokey(event):
        global word

        word = word.lower()
        print(event.char)
        # mixer.music.load("audio/" + str(event.char) + ".mp3")
        # mixer.music.play()
        try:
            if event.char  in " ,.!?\n":
                speak(word)
                play(word)
                word = ""
            else:
                word += str(event.char)

        except:
            word=""

    def indietro(event):
        global word
        
        word = word[:-1]
      
    root = tk.Tk()
    root.title("Type to hear the pc reading the text when press space")
    root.geometry("600x400+200+400")
    
    # text widget where you write
    lbx = tk.Listbox(
        root,
        bg="black",
        fg="white"
        )
    lbx.pack(side="left", fill="both")
    lbx.bind("<Double-Button>", add_word_to_text)
    lbx.bind("<Control-d>", delete)
    scrollbar = ttk.Scrollbar(root, orient=tk.VERTICAL, command=lbx.yview)
    scrollbar.pack(side="left", fill=tk.Y)
    lbx.config(yscrollcommand=scrollbar.set)
    show_list()

    lab = tk.Label(root, text="write and press return").pack()
    e = tk.Entry(root)
    e.pack()
    e.bind("<Return>", lambda evt: save_text(e.get()))

    text = tk.Text(root)
    text.pack()


    text.focus()
    text.bind("<Key>", audiokey)
    text.bind("<BackSpace>", indietro)
    # text.bind("<Return>", _return)
    root.mainloop()

def save_text(text):
    speak(text)

def add_word_to_text(evt):
    global lbx, text

    word = lbx.get(lbx.curselection())
    word = word[:-4]
    text.insert("end", word)
    mixer.music.load("audio/" + word + ".mp3")
    mixer.music.play()
    text.insert("end", " ")


start()
