import tkinter as tk
from PIL import Image, ImageTk
from PIL import Image, ImageSequence
from tkinter import filedialog
import os
import sys



def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(
        sys,
        '_MEIPASS',
        os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


def unpack_gif(src):
    "If disposal == 2 (unclomplete) it copies it on the previous"
    image = Image.open(src)
    frames = []
    disposal = []
    for gifFrame in ImageSequence.Iterator(image):
        disposal.append(gifFrame.disposal_method)
        frames.append(gifFrame.convert('P'))
    output = []
    lastFrame = None
    thisFrame = None
    for i, loadedFrame in enumerate(frames):
        thisFrame = loadedFrame
        if disposal[i] == 2:
            if i != 0:
                lastFrame.paste(thisFrame, mask=thisFrame.convert('RGBA'))
                output.append(lastFrame)
            else:
                output.append(thisFrame)
        elif disposal[i] == 1 or disposal[i] == 0:
            output.append(thisFrame)
        else:
            raise ValueError('Disposal Methods other than 2:Restore to Background,\
             1:Do Not Dispose, and 0:No Disposal are supported at this time')
        lastFrame = loadedFrame
    return output


def save_all_frames(file):
    "Saves all the frames of the gif as numbered png files"
    name = os.path.splitext(file[0])[0]
    im = unpack_gif(file[0])
    for n, i in enumerate(im):
        if n<10:
            zero = "0"
        else:
            zero = ""
        i.save(f"{name}{zero}{n}.png")
    print(im)


# root.withdraw()
def getfile():
    global filename

    filename = filedialog.askopenfilenames(
        parent=root,
        initialdir=".",
        initialfile='tmp',
        filetypes=[("GIF", "*.gif"),
                ("All files", "*")]
        )
    print(filename)
    img = Image.open(resource_path(filename[0]))
    img = img.resize((150, 150))
    img = ImageTk.PhotoImage(img)
    getfile.image = img
    label["image"] = img
    button2.pack()

filename = ""
root = tk.Tk()
img2 = tk.PhotoImage(file=resource_path("gif_split.png"))
label1 = tk.Label(master=root,
    image=img2)
label1.pack()
button = tk.Button(
    master=root,
    bg="pink",
    text="Open Gif",
    command=getfile)
button.pack()
# Label with the image of the gif (after you choose it)

img3 = ImageTk.PhotoImage(file=resource_path("arrowup.png"))
label = tk.Label(master=root,
    image=img3,
    )
label.pack()
button2 = tk.Button(
    master=root,
    bg="gold",
    text="Save png files out of the gif",
    command=lambda: save_all_frames(filename))
# button2.pack()

root.mainloop()
# save_all_frames(filename)

